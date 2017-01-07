# -*- coding: utf-8 -*-

__author__ = 'Rufeer'
import base64
def int2bin(n, count=8):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def bin2int(n):
    x   = 0
    num = 32
    for ch in n:
        x += int(ch)*num
        num /= 2
    return x

def str2bin(fstr, l):
    s = ''
    for ch in fstr:
        s += int2bin(ord(ch))
    if l%3 == 1:
        s += 2*'00000000'
    if l%3 == 2:
        s += '00000000'
    return s

base64_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


if __name__ == '__main__':
    source_str = raw_input()
    str_len    = len(source_str)
    str_8bit   = str2bin(source_str, str_len)
    goal_str = ''
    for i in range(6, len(str_8bit)+1, 6):
        if str_8bit[i-6:i] == '000000':
            goal_str += '='
        else:
            goal_str += base64_char[bin2int(str_8bit[i-6:i])]
    print 'my answer: ', goal_str
    print 'right:     ', base64.b64encode(source_str)