# cython: language_level=3

# The contents of this file are subject to the BitTorrent Open Source License
# Version 1.1 (the License).  You may not copy or use this file, in either
# source code or executable form, except in compliance with the License.  You
# may obtain a copy of the License at http://www.bittorrent.com/license/.
#
# Software distributed under the License is distributed on an AS IS basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.  See the License
# for the specific language governing rights and limitations under the
# License.

# Based on https://github.com/karamanolev/bencode3/blob/master/bencode.py

__version__ = '1.1.2'

import sys
IS_PY2 = sys.version[0] == '2'

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

if IS_PY2:
    END_CHAR = 'e'
else:
    END_CHAR = ord('e')


class BTFailure(Exception):
    pass


def decode_int(bytes x, int f):
    f += 1
    new_f = x.index(b'e', f)
    n = int(x[f:new_f])
    if x[f] == b'-'[0]:
        if x[f + 1] == b'0'[0]:
            raise ValueError()
    elif x[f] == b'0'[0] and new_f != f + 1:
        raise ValueError()
    return n, new_f + 1


def decode_string(bytes x, int f):
    colon = x.index(b':', f)
    n = int(x[f:colon])
    if x[f] == b'0'[0] and colon != f + 1:
        raise ValueError()
    colon += 1
    return x[colon:colon + n], colon + n


def decode_list(bytes x, int f):
    r, f = [], f + 1
    while x[f] != END_CHAR:
        v, f = decode_func[x[f]](x, f)
        r.append(v)
    return r, f + 1


def decode_dict(bytes x, int f):
    r, f = OrderedDict(), f + 1
    while x[f] != END_CHAR:
        k, f = decode_string(x, f)
        r[k], f = decode_func[x[f]](x, f)
    return r, f + 1


decode_func = dict()

for func, keys in [
    (decode_list, 'l'),
    (decode_dict, 'd'),
    (decode_int, 'i'),
    (decode_string, [str(x) for x in range(10)])
]:
    for key in keys:
        if IS_PY2:
            decode_func[key] = func
        else:
            decode_func[ord(key)] = func


def bdecode(bytes x):
    try:
        r, l = decode_func[x[0]](x, 0)
    except (IndexError, KeyError, ValueError):
        raise BTFailure("not a valid bencoded string")
    if l != len(x):
        raise BTFailure("invalid bencoded value (data after valid prefix)")
    return r


def encode(v, r):
    tp = type(v)
    if tp in encode_func:
        return encode_func[tp](v, r)
    else:
        for tp, func in encode_func.items():
            if isinstance(v, tp):
                return func(v, r)
    raise BTFailure(
        "Can't encode {0}(Type: {1})".format(v, type(v))
    )


def encode_int(x, list r):
    r.extend((b'i', str(x).encode(), b'e'))


def encode_bool(x, list r):
    if x:
        encode_int(1, r)
    else:
        encode_int(0, r)


def encode_string(x, list r):
    if isinstance(x, str):
        x = x.encode()
    r.extend((str(len(x)).encode(), b':', x))


def encode_list(x, list r):
    r.append(b'l')
    for i in x:
        encode(i, r)
    r.append(b'e')


def encode_dict(x, list r):
    r.append(b'd')
    item_list = list(x.items())
    item_list.sort()
    for k, v in item_list:
        if isinstance(k, str):
            k = k.encode()
        r.extend((str(len(k)).encode(), b':', k))
        encode(v, r)
    r.append(b'e')


encode_func = {
    int: encode_int,
    long: encode_int,
    bytes: encode_string,
    str: encode_string,
    list: encode_list,
    tuple: encode_list,
    dict: encode_dict,
    OrderedDict: encode_dict,
    bool: encode_bool,
}


def bencode(x):
    r = []
    encode(x, r)
    return b''.join(r)
