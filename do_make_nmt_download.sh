git clone https://github.com/OpenNMT/OpenNMT-py.git
cd OpenNMT-py
pip install -e .

pip install -r requirements.opt.txt

cd ..
wget https://s3.amazonaws.com/opennmt-models/sum_transformer_model_acc_57.25_ppl_9.22_e16.pt


