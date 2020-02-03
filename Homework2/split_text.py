"""
    @Author John Bonazzi
    @Date 2/3/2020
    @Note to use for MTH 312 - Homework 2
"""

import json

def vigenere_split(keyword_len, message):
    output = []
    for _ in range(0, keyword_len):
        output.append("")
    len_pos = 0
    while len_pos < len(message):
        endpoint = len_pos + keyword_len
        if endpoint >= len(message):
            endpoint = len_pos + (len(message) - len_pos)
        substring = message[len_pos:endpoint]
        for pos in range(0, len(substring)):
            output[pos] += substring[pos]
        len_pos += keyword_len
    return output

if __name__ == "__main__":
    fp = open("./vigenere.json", 'w')
    fr = open("./cipher.txt", 'r')
    message = fr.read()
    out = vigenere_split(4, message)
    json.dump(out, fp, separators=(",\n", " : "))
    for element in out:
        print(element)
        print("++++++++++++++++++")