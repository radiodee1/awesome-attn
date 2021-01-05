#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from itertools import islice, repeat

from onmt.utils.logging import init_logger
from onmt.utils.misc import split_corpus
#from onmt.translate.translator import build_translator
from translator import build_translator

import onmt.opts as opts
from onmt.utils.parse import ArgumentParser



def split_xcorpus(path, shard_size, default=None):
    """yield a `list` containing `shard_size` line of `path`,
    or repeatly generate `default` if `path` is None.
    """
    if path is not None:
        return _split_xcorpus(path, shard_size)
    else:
        return repeat(default)


def _split_xcorpus(path, shard_size):
    """Yield a `list` containing `shard_size` line of `path`.
    """
    if True: #with open(path, "rb") as f:
        if shard_size <= 0:
            yield [path for _ in range(shard_size)] #f.readlines()
        else:
            while True:
                shard = [path for _ in range(shard_size)] # list(islice(f, shard_size))
                if not shard:
                    break
                yield shard


def translate(opt):
    ArgumentParser.validate_translate_opts(opt)
    logger = init_logger(opt.log_file)

    #print(opt.tgt)
    if isinstance(opt.tgt, str):
        tgt_shards = split_xcorpus(opt.tgt, opt.shard_size)
        print(opt.tgt)
    else:
        tgt_shards = split_corpus(opt.tgt, opt.shard_size)

    #print(tgt_shards, 'tgt')
    translator = build_translator(opt, logger=logger, report_score=True)
    src_shards = split_corpus(opt.src, opt.shard_size)
    #tgt_shards = split_xcorpus(tmp_tgt, opt.shard_size, default)
    shard_pairs = zip(src_shards, tgt_shards)

    print(src_shards, 'src')
    for i, (src_shard, tgt_shard) in enumerate(shard_pairs):
        logger.info("Translating shard %d." % i)
        translator.translate(
            src=src_shard,
            tgt=tgt_shard,
            batch_size=opt.batch_size,
            batch_type=opt.batch_type,
            attn_debug=opt.attn_debug,
            align_debug=opt.align_debug
            )


def _get_parser():
    parser = ArgumentParser(description='translate.py')

    opts.config_opts(parser)
    opts.translate_opts(parser)
    return parser


def main():
    parser = _get_parser()

    opt = parser.parse_args()
    translate(opt)


if __name__ == "__main__":
    main()
