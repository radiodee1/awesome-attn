#!/usr/bin/env python3

import pyonmttok
import os

tokenizer = pyonmttok.Tokenizer(
        "aggressive", 
        joiner_annotate=True, 
        segment_numbers=True,
        bpe_model_path="./data/bpe/bpe-model-32k"
        )


