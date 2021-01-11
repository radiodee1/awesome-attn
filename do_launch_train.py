#!/usr/bin/env python3.6

import sys
import os
import argparse

#print(sys.argv, len(sys.argv))

CONFIG="yaml/train_config.yaml"
CONFIG_EXTRA="yaml/train_config_extra.yaml"
CORPUS_EXTRA="data/bpe/extra.src"

GPU="--world_size 1 --gpu_ranks 0"

if os.path.isfile(CORPUS_EXTRA):
    CONFIG=CONFIG_EXTRA

#print(CONFIG)

parser = argparse.ArgumentParser(description='Start training run.')
parser.add_argument('--gpu', help='Launch with gpu.', action="store_true")
parser.add_argument('trainfrom', help='Train from this saved checkpoint.', nargs="?")
args = parser.parse_args()

print(args)

if not args.gpu:
    GPU=''

if args.trainfrom != None and os.path.isfile(str(args.trainfrom)):
    print("train from", str(args.trainfrom))
    os.system("onmt_train --config " + CONFIG +" --train_from " + str(args.trainfrom) + " " + GPU)
    exit()

os.system("onmt_train --config " + CONFIG + " " + GPU)

'''
#onmt_train --config yaml/train_config.yaml
onmt_train --config $CONFIG

'''

