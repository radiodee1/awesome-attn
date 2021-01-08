#!/usr/bin/env python3

import requests
import os
import sys
import argparse
import pyonmttok
import datetime
from do_make_corpus_tab import make_single_context

HOST="127.0.0.1"
PORT=5000
URL_ROOT="/"  #"/OpenNMT-py"

def client_request(q_str, detokenize=False, to_screen=True, lrg_context=True):

    if lrg_context:
        q_str = 'question: ' + q_str

    if True:
        tokenizer = pyonmttok.Tokenizer(
                "conservative", 
                bpe_model_path="./data/bpe/bpe-model-32k",  
                joiner_annotate=True, 
                )
        q_str, _ = tokenizer.tokenize(q_str)
        q_str = ' '.join(q_str)
        
        now = datetime.datetime.now()

        time = now.strftime("%I:%M %p")
        date = now.strftime("%B %d, %Y")

        if lrg_context == False:
            time_str = "this is the time. " + time + ', ' + date + ' .'
        else:
            time_str = make_single_context() # 
            
        time_str, _ = tokenizer.tokenize(time_str)
        time_str = ' '.join(time_str)

    headers_1 = {"Content-Type": "application/json"}               ## must be dictionary!!
    query_1 = '[{"src":"' +  q_str + '" , "id": 100}]'              ## must be string!!
    query_2 = '[{"src":"' +  q_str + '", "tgt_prefix": "true" , "ref":  "' + time_str + '" ,   "id": 100}]'   ## must be string!!
    
    print(query_2)

    response = requests.post(
            'http://'+ HOST + ':' + str(PORT) + URL_ROOT + '/translate', 
            headers=headers_1,  
            data=query_2.encode('utf-8')
            )

    if to_screen:
        print(response)
        print(response.json())
        print('-----')
    try:
        response = response.json()[0][0]['tgt']
    except:
        pass

    if to_screen:
        print(response)
        print(len(response))
        print('-----')
    try:
        response = response.split(' ')
    except:
        pass

    if to_screen:
        #print(len(response), 'length')
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
    parser = argparse.ArgumentParser(description='Make rest client.')
    parser.add_argument('--no-context', help='No context for q/a pairs.', action="store_true")
    args = parser.parse_args()

    arg_no_context = False

    if args.no_context:
        arg_no_context = True

    client_request('hello there', detokenize=False, to_screen=True)
    detokenize_example()

    if True:
        while True:
            i = input('> ')
            client_request(i, detokenize=True, to_screen=True, lrg_context= not arg_no_context)
