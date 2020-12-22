echo "bpe files"
zip transformer_bpe.zip data/bpe/vocab.src data/bpe/bpe-model-32k
zip transformer_bpe.zip data/bpe/train.src data/bpe/train.tgt
zip transformer_bpe.zip data/bpe/valid.src data/bpe/valid.tgt
zip transformer_bpe.zip data/bpe/test.src data/bpe/test.tgt

echo "raw files"
#zip transformer_raw.zip data/bpe-model-32k
zip transformer_raw.zip data/train.from data/train.to
zip transformer_raw.zip data/valid.from data/valid.to
zip transformer_raw.zip data/test.from data/test.to




