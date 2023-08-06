#!/usr/bin/env python
#

"""
Lookup an MX record and printout all the MX preference, target, and
associated IP addresses of the targets.
"""

import getdns, pprint, sys

extensions = { "return_both_v4_and_v6" : getdns.EXTENSION_TRUE }


def get_ip(ctx, qname):
    iplist = []
    try:
        results = ctx.address(name=qname, extensions=extensions)
    except getdns.error as e:
        print(str(e))
        sys.exit(1)

    if results.status == getdns.RESPSTATUS_GOOD:
        for addr in results.just_address_answers:
            iplist.append(addr['address_data'])
    else:
        print("getdns.address() returned an error: {0}".format(results.status))
    return iplist


if __name__ == '__main__':

    qname = sys.argv[1]

    ctx = getdns.Context()
    try:
        results = ctx.general(name=qname, request_type=getdns.RRTYPE_MX)
    except getdns.error as e:
        print(str(e))
        sys.exit(1)

    status = results.status

    hostlist = []
    if status == getdns.RESPSTATUS_GOOD:
        for reply in results.replies_tree:
            answers = reply['answer']
            for answer in answers:
                if answer['type'] == getdns.RRTYPE_MX:
                    iplist = get_ip(ctx, answer['rdata']['exchange'])
                    for ip in iplist:
                        hostlist.append( (answer['rdata']['preference'], \
                                          answer['rdata']['exchange'], ip) )
    elif status == getdns.RESPSTATUS_NO_NAME:
        print("{0}, {1}: no such name".format(qname, qtype))
    elif status == getdns.RESPSTATUS_ALL_TIMEOUT:
        print("{0}, {1}: query timed out".format(qname, qtype))
    else:
        print("{0}, {1}: unknown return code: {2}".format(qname, qtype, results["status"]))

    for (pref, mx, addr) in sorted(hostlist):
        print(pref, mx, addr)
