#!/usr/bin/env python3

import pyonmttok
import os

print('make learner')
tokenizer = pyonmttok.Tokenizer("aggressive", joiner_annotate=True, segment_numbers=True)
learner = pyonmttok.BPELearner(tokenizer=tokenizer, symbols=32000)

print('ingest train')
learner.ingest_file("./data/train.from")
learner.ingest_file("./data/train.to")

if not os.path.isdir('./data/bpe/'): os.mkdir('./data/bpe/')

print('learner learn')
token = learner.learn("./data/bpe/bpe-model-32k")

print("tokenize train")
token.tokenize_file("./data/train.from","./data/bpe/train.src")
token.tokenize_file("./data/train.to","./data/bpe/train.tgt")
print("tokenize valid")
token.tokenize_file("./data/valid.from","./data/bpe/valid.src")
token.tokenize_file("./data/valid.to","./data/bpe/valid.tgt")
print("tokenize test")
token.tokenize_file("./data/test.from","./data/bpe/test.src")
token.tokenize_file("./data/test.to","./data/bpe/test.tgt")
