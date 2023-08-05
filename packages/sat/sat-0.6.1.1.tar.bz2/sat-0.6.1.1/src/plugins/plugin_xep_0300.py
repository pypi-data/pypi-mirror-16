#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# SAT plugin for Hash functions (XEP-0300)
# Copyright (C) 2009-2016 Jérôme Poisson (goffi@goffi.org)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sat.core.i18n import _
from sat.core.log import getLogger
log = getLogger(__name__)
from sat.core import exceptions
from twisted.words.xish import domish
from twisted.words.protocols.jabber.xmlstream import XMPPHandler
from twisted.internet import threads
from twisted.internet import defer
from zope.interface import implements
from wokkel import disco, iwokkel
from collections import OrderedDict
import hashlib


PLUGIN_INFO = {
    "name": "Cryptographic Hash Functions",
    "import_name": "XEP-0300",
    "type": "XEP",
    "protocols": ["XEP-0300"],
    "main": "XEP_0300",
    "handler": "yes",
    "description": _("""Management of cryptographic hashes""")
}

NS_HASHES = "urn:xmpp:hashes:1"
NS_HASHES_FUNCTIONS = u"urn:xmpp:hash-function-text-names:{}"
BUFFER_SIZE = 2**12
ALGO_DEFAULT = 'sha-256'


class XEP_0300(object):
    ALGOS = OrderedDict((
            (u'md5', hashlib.md5),
            (u'sha-1', hashlib.sha1),
            (u'sha-256', hashlib.sha256),
            (u'sha-512', hashlib.sha512),
            ))

    def __init__(self, host):
        log.info(_("plugin Hashes initialization"))

    def getHandler(self, profile):
        return XEP_0300_handler()

    def getHasher(self, algo):
        """Return hasher instance

         /!\\ blocking method, considere using calculateHashElt
         if you want to hash a big file
         @param algo(unicode): one of the XEP_300.ALGOS keys
         @return (hash object): same object s in hashlib.
            update method need to be called for each chunh
            diget or hexdigest can be used at the end
        """
        return self.ALGOS[algo]()

    @defer.inlineCallbacks
    def getBestPeerAlgo(self, to_jid, profile):
        """Return the best available hashing algorith of other peer

         @param to_jid(jid.JID): peer jid
         @parm profile: %(doc_profile)s
         @return (D(unicode, None)): best available algorithm,
            or None if hashing is not possible
        """
        for algo in reversed(XEP_0300.ALGOS):
            has_feature = yield self.host.hasFeature(NS_HASHES_FUNCTIONS.format(algo), to_jid, profile)
            if has_feature:
                log.debug(u"Best hashing algorithm found for {jid}: {algo}".format(
                    jid=to_jid.full(),
                    algo=algo))
                defer.returnValue(algo)

    def calculateHashBlocking(self, file_obj, hasher):
        """Calculate hash in a blocking way

        @param file_obj(file): a file-like object
        @param hasher(callable): the method to call to initialise hash object
        @return (str): the hex digest of the hash
        """
        hash_ = hasher()
        while True:
            buf = file_obj.read(BUFFER_SIZE)
            if not buf:
                break
            hash_.update(buf)
        return hash_.hexdigest()

    def calculateHashElt(self, file_obj=None, algo=ALGO_DEFAULT):
        """Compute hash and build hash element

        @param file_obj(file, None): file-like object to use to calculate the hash
        @param algo(unicode): algorithme to use, must be a key of XEP_0300.ALGOS
        @return (D(domish.Element)): hash element
        """
        def hashCalculated(hash_):
            return self.buildHashElt(hash_, algo)
        hasher = self.ALGOS[algo]
        hash_d = threads.deferToThread(self.calculateHashBlocking, file_obj, hasher)
        hash_d.addCallback(hashCalculated)
        return hash_d

    def buildHashElt(self, hash_=None, algo=ALGO_DEFAULT):
        """Compute hash and build hash element

        @param hash_(None, str): hash to use, or None for an empty element
        @param algo(unicode): algorithme to use, must be a key of XEP_0300.ALGOS
        @return (domish.Element): computed hash
        """
        hash_elt = domish.Element((NS_HASHES, 'hash'))
        if hash_ is not None:
            hash_elt.addContent(hash_)
        hash_elt['algo']=algo
        return hash_elt

    def parseHashElt(self, parent):
        """Find and parse a hash element

        if multiple elements are found, the strongest managed one is returned
        @param (domish.Element): parent of <hash/> element
        @return (tuple[unicode, str]): (algo, hash) tuple
            both values can be None if <hash/> is empty
        @raise exceptions.NotFound: the element is not present
        """
        algos = XEP_0300.ALGOS.keys()
        hash_elt = None
        best_algo = None
        best_value = None
        for hash_elt in parent.elements(NS_HASHES, 'hash'):
            algo = hash_elt.getAttribute('algo')
            try:
                idx = algos.index(algo)
            except ValueError:
                log.warning(u"Proposed {} algorithm is not managed".format(algo))
                algo = None
                continue

            if best_algo is None or algos.index(best_algo) < idx:
                best_algo = algo
                best_value = str(hash_elt) or None

        if not hash_elt:
            raise exceptions.NotFound
        return best_algo, best_value


class XEP_0300_handler(XMPPHandler):
    implements(iwokkel.IDisco)

    def getDiscoInfo(self, requestor, target, nodeIdentifier=''):
        hash_functions_names = [disco.DiscoFeature(NS_HASHES_FUNCTIONS.format(algo)) for algo in XEP_0300.ALGOS]
        return [disco.DiscoFeature(NS_HASHES)] + hash_functions_names

    def getDiscoItems(self, requestor, target, nodeIdentifier=''):
        return []
