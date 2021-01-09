#!/usr/bin/env python3

import pyonmttok
import os

print("## bpe ##")

print('make learner')
tokenizer = pyonmttok.Tokenizer("aggressive", joiner_annotate=True, segment_numbers=True)
learner = pyonmttok.BPELearner(tokenizer=tokenizer, symbols=32000)

print('ingest train')
learner.ingest_file("./data/train.from")
learner.ingest_file("./data/train.to")

if os.path.isfile("./data/extra.src") and os.path.isfile("./data/extra.tgt"):
    learner.ingest_file("./data/extra.src")
    learner.ingest_file("./data/extra.tgt")

if not os.path.isdir('./data/bpe/'): os.mkdir('./data/bpe/')

print('learner learn')

if not os.path.isfile('./data/bpe/bpe-model-32k'):
    token = learner.learn("./data/bpe/bpe-model-32k")
else:
    print('make tokenizer from "bpe_model_path".')
    token = pyonmttok.Tokenizer('aggressive',
                                joiner_annotate=True,
                                segment_numbers=True,
                                bpe_model_path="./data/bpe/bpe-model-32k")

print("tokenize train")
token.tokenize_file("./data/train.from","./data/bpe/train.src")
token.tokenize_file("./data/train.to","./data/bpe/train.tgt")
print("tokenize valid")
token.tokenize_file("./data/valid.from","./data/bpe/valid.src")
token.tokenize_file("./data/valid.to","./data/bpe/valid.tgt")
print("tokenize test")
token.tokenize_file("./data/test.from","./data/bpe/test.src")
token.tokenize_file("./data/test.to","./data/bpe/test.tgt")

print('check for extra corpus')
if os.path.isfile("./data/extra.src"):
    token.tokenize_file("./data/extra.src","./data/bpe/extra.src")
if os.path.isfile("./data/extra.tgt"):
    token.tokenize_file("./data/extra.tgt","./data/bpe/extra.tgt")

exit()
###########################
