#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The MIT License (MIT)
    Copyright (c) 2014-2015 by Halfmoon Labs, Inc.
    Copyright (c) 2016 by Blocktatck.org

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

# use Blockstack Labs as a storage proxy

import os
import sys 
import traceback
import logging
import json
import requests

import blockstack_zones


from .common import get_logger, DEBUG

log = get_logger("blockstack-storage-driver-blockstack-s3-readonly")

RESOLVER_URL = "https://onename.com"

def get_zonefile( fqu, zonefile_hash ):
    """
    Try to get a zonefile, from onename.com
    Return the zonefile (serialized as a string) on success
    Return None on error
    """
    url = "%s/%s" % (RESOLVER_URL, fqu)
    req = requests.get(url)
    if req.status_code != 200:
        return None


def get_data( data_id, zonefile=False ):
    """
    Get data or a zonefile from onename.com or S3, depending on which is requested
    """

    if os.environ.get("BLOCKSTACK_RPC_PID", None) == str(os.getpid()):
        # don't talk to ourselves 
        log.debug("Do not get_data from ourselves")
        return None

    url = "http://%s:%s/RPC2" % (SERVER_NAME, SERVER_PORT)
    ses = xmlrpclib.ServerProxy( url, allow_none=True )
    
    if zonefile:
        res = ses.get_zonefiles( [data_id] )
        try:
            data = json.loads(res)
        except:
            log.error("Failed to parse zonefile from %s" % data_id)
            return None

        if 'error' in data:
            log.error("Get zonefile %s: %s" % (data_id, data['error']))
            return None
        else:
            try:
                return data['zonefiles'][0]
            except:
                log.error("Failed to parse zonefile")
                return None

    else:
        res = ses.get_profile( data_id )
        try:
            data = json.loads(res)
        except:
            log.error("Failed to parse profile from %s" % data_id)
            return None

        if 'error' in data:
            log.error("Get profile %s: %s" % (data_id, data['error']))
            return None 
        else:
            try:
                return data['profile']
            except:
                log.error("Failed to parse profile")
                return None


def put_data( data_id, data_txt, zonefile=False ):
    """
    Put data or a zoneflie to the server.
    """
    
    if os.environ.get("BLOCKSTACK_RPC_PID", None) == str(os.getpid()):
        # don't talk to ourselves 
        log.debug("Do not put_data to ourselves")
        return False

    url = "http://%s:%s/RPC2" % (SERVER_NAME, SERVER_PORT)
    ses = xmlrpclib.ServerProxy( url, allow_none=True )

    if zonefile:
        # must be a zonefile 
        try:
            zf = blockstack_zones.parse_zone_file( data_txt )
        except:
            log.error("Failed to parse zone file for %s" % data_id)
            return False

        res_json = ses.put_zonefiles( [data_txt] )
        try:
            res = json.loads(res_json)
        except:
            log.error("Invalid non-JSON response")
            return False

        if 'error' in res:
            log.error("Failed to put %s: %s" % (data_id, data_txt))
            return False
        elif len(res['saved']) != 1 or res['saved'][0] != 1:
            log.error("Server %s:%s failed to save %s" % (SERVER_NAME, SERVER_PORT, data_id))
            return False 

        else:
            return True

    else:
        res = ses.put_profile( data_id, data_txt )
        if 'error' in res:
            log.error("Failed to put %s: %s" % (data_id, res))
            return False
        else:
            return True


def storage_init(conf):
    return True

def handles_url( url ):
    if url.startswith("http://") and len(url.split("#")) == 2 and url.split("#")[1].endswith("/RPC2"):
        return True
    else:
        return False

def make_mutable_url( data_id ):
    # xmlrpc endpoint
    return "http://%s:%s/RPC2#%s" % (SERVER_NAME, SERVER_PORT, data_id)

def get_immutable_handler( key ):
    return get_data( key, zonefile=True )

def get_mutable_handler( url ):
    parts = url.split("#")
    if len(parts) != 2:
        log.error("Invalid url '%s'" % url)
        return None

    data_id = parts[1]
    return get_data( data_id, zonefile=False )


def put_immutable_handler( key, data, txid ):
    return put_data( key, data, zonefile=True )

def put_mutable_handler( data_id, data_bin ):
    return put_data( data_id, data_bin, zonefile=False )

def delete_immutable_handler( key, txid, sig_key_txid ):
    return True

def delete_mutable_handler( data_id, signature ):
    return True
