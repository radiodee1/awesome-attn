#!/usr/bin/env python3

import requests
import os
import sys
import argparse

HOST="127.0.0.1"
PORT=5000
URL_ROOT="/OpenNMT-py"

'''
curl -i -X POST -H "Content-Type: application/json" \
    -d '[{"src": "this is a test for model 0", "id": 100}]' \
    http://$HOST:$PORT$URL_ROOT/translate 
'''


query_1 = '[{"src": "this is a test for model 0", "id": 100}]' ## must be string!!
headers_1 = {"Content-Type": "application/json"}               ## must be dictionary!!

response = requests.post('http://'+ HOST + ':' + str(PORT) + URL_ROOT + '/translate', headers=headers_1,  data=query_1)
print(response)
print(response.json())
print('-----')
print(response.json()[0][0]['tgt'])


