#!/usr/bin/env python3

import requests
import os
import sys
import argparse
import pyonmttok

HOST="127.0.0.1"
PORT=5000
URL_ROOT="/OpenNMT-py"


query_1 = '[{"src": "this is a test for model 100", "id": 100}]' ## must be string!!
headers_1 = {"Content-Type": "application/json"}               ## must be dictionary!!
try:
    response = requests.post('http://'+ HOST + ':' + str(PORT) + URL_ROOT + '/translate', headers=headers_1,  data=query_1)

    print(response)
    print(response.json())
    print('-----')
    response = response.json()[0][0]['tgt']
    print(response)
    print('-----')
    response = response.split(' ')
    print(len(response), 'length')
    print('-----')
    print(response)
    print('-----')
    tokenizer = pyonmttok.Tokenizer("conservative", bpe_model_path="./data/bpe/bpe-codes.src",  joiner_annotate=True, joiner_new=True)

    response = tokenizer.detokenize(response)

    print(response)

except:
    print('no server running?')
    response = ''

#'''
########################

tokenizer_in = pyonmttok.Tokenizer("conservative", bpe_model_path="./data/bpe/bpe-codes.src", joiner_annotate=True, joiner_new=True)
print('-----')
hello = "Hello World!"
print(hello)
hello_tokens, _ = tokenizer_in.tokenize(hello)
print(hello_tokens)
tokenizer_out = pyonmttok.Tokenizer("conservative") #, bpe_model_path="./data/bpe/bpe-codes.src", joiner_annotate=True, joiner_new=True)
print('-----')
hello_tokens = tokenizer_out.detokenize(hello_tokens)

print(hello_tokens)
#'''

