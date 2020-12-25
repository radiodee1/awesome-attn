#!/usr/bin/env python3

import requests
import os
import sys
import argparse
import pyonmttok

HOST="127.0.0.1"
PORT=5000
URL_ROOT="/OpenNMT-py"

def client_request(q_str, detokenize=False, to_screen=False):

    if True:
        tokenizer = pyonmttok.Tokenizer(
                "conservative", 
                bpe_model_path="./data/bpe/bpe-model-32k",  
                joiner_annotate=True, 
                )
        q_str, _ = tokenizer.tokenize(q_str)
        q_str = ' '.join(q_str)
        #q_str = q_str.encode('utf-8').decode('utf-8')

    if to_screen:
        print(q_str)

    query_1 = '[{"src":"' +  q_str + '", "id": 100}]'              ## must be string!!
    headers_1 = {"Content-Type": "application/json"}               ## must be dictionary!!
    
    response = requests.post(
            'http://'+ HOST + ':' + str(PORT) + URL_ROOT + '/translate', 
            headers=headers_1,  
            data=query_1.encode('utf-8')
            )

    if to_screen:
        print(response)
        print(response.json())
        print('-----')

    response = response.json()[0][0]['tgt']
    
    if to_screen:
        print(response)
        print('-----')
    response = response.split(' ')
    if to_screen:
        print(len(response), 'length')
        print('-----')
        print(response)
        print('-----')

    if detokenize:
        tokenizer = pyonmttok.Tokenizer(
                "conservative", 
                bpe_model_path="./data/bpe/bpe-model-32k",  
                joiner_annotate=True, 
                joiner_new=True
                )

        response = tokenizer.detokenize(response)

    if to_screen:
        print(response)

    return response

########################

def detokenize_example():
    tokenizer_in = pyonmttok.Tokenizer(
            "conservative", 
            bpe_model_path="./data/bpe/bpe-model-32k", 
            joiner_annotate=True, 
            joiner_new=True
            )
    print('-----')
    hello = "hello world!"
    print(hello)
    hello_tokens, _ = tokenizer_in.tokenize(hello)
    print(hello_tokens)
    tokenizer_out = pyonmttok.Tokenizer(
            "conservative", 
            bpe_model_path="./data/bpe/bpe-model-32k", 
            joiner_annotate=True, 
            joiner_new=True
            )
    print('-----')
    hello_tokens = tokenizer_out.detokenize(hello_tokens)

    print(hello_tokens)


if __name__ == '__main__':

    client_request('hello there', detokenize=True, to_screen=True)
    detokenize_example()

    if True:
        while True:
            i = input('> ')
            client_request(i, detokenize=True, to_screen=True)
