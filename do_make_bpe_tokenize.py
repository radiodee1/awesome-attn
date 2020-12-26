#!/usr/bin/env python3

import pyonmttok
import os
import sys

if len(sys.argv) == 1: 
    print('Enter name of file to convert as first parameter.')
    exit()

print(sys.argv[1])

z = sys.argv[1]
z = z.split('/')[-1]

tokenizer = pyonmttok.Tokenizer(
        "aggressive", 
        joiner_annotate=True, 
        segment_numbers=True,
        bpe_model_path="./data/bpe/bpe-model-32k"
        )


print("tokenize")
tokenizer.tokenize_file(sys.argv[1],"./data/bpe/"+ z+ ".bpe.txt")

print("File moved to ./data/bpe/" + z + '.bpe.txt')


