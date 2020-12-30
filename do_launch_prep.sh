./bpe_pyonmttok.py

CONFIG="yaml/train_config.yaml"
CONFIG_EXTRA="yaml/train_config_extra.yaml"
CORPUS_EXTRA="data/bpe/extra.src"

if [[ -f "$CORPUS_EXTRA" ]] ; then
    CONFIG=$CONFIG_EXTRA
    echo "'extra' files detected..."
fi


onmt_build_vocab --config $CONFIG -n_sample 8000 


