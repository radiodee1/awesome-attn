#!/usr/bin/env python3

import pyonmttok
import os

print('make learner')
tokenizer = pyonmttok.Tokenizer("aggressive", joiner_annotate=True, segment_numbers=True)
learner = pyonmttok.BPELearner(tokenizer=tokenizer, symbols=32000)

# SentencePiece can learn from raw sentences so a tokenizer in not required.
#learner = pyonmttok.SentencePieceLearner(vocab_size=32000, character_coverage=0.98)

print('ingest train')
learner.ingest_file("./data/train.from")
learner.ingest_file("./data/train.to")

os.mkdir('./data/bpe/')

print('learner learn')
tokenizer = learner.learn("./data/bpe/bpe-model-32k")

print("tokenize train")
tokenizer.tokenize_file("./data/train.from","./data/bpe/train.src")
tokenizer.tokenize_file("./data/train.to","./data/bpe/train.tgt")
print("tokenize valid")
tokenizer.tokenize_file("./data/valid.from","./data/bpe/valid.src")
tokenizer.tokenize_file("./data/valid.to","./data/bpe/valid.tgt")
print("tokenize test")
tokenizer.tokenize_file("./data/test.from","./data/bpe/test.src")
tokenizer.tokenize_file("./data/test.to","./data/bpe/test.tgt")
