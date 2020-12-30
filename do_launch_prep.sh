./pyonmttok_mod.py

CONFIG="yaml/train_config.yaml"
CONFIG_EXTRA="yaml/train_config_extra.yaml"
CORPUS_EXTRA="data/bpe/extra.src"

if [[ -f "$CORPUS_EXTRA" ]] ; then
    CONFIG=$CONFIG_EXTRA
    echo "'extra' files detected..."
fi


onmt_build_vocab --config $CONFIG -bpe_model_path ./data/bpe/bpe-model-32k  -size 8000 #-n_sample 80000 

#onmt_build_vocab --config $CONFIG -model_path ./data/mod/mod-model-32k  -size 8000 --overwrite True --src_vocab ./data/mod/vocab.src #-n_sample 80000 


