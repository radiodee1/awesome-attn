#git clone https://github.com/OpenNMT/OpenNMT-py.git
git submodule init
git submodule update
cd OpenNMT-py
#pip install -e .
python setup.py install
pip install -r requirements.opt.txt
cd ..

#cd Tokenizer
#git submodule update --init
#mkdir build
#cd build
#cmake ..
#make
#cd ../..

pip install -r requirements.amd64.txt

#cd ..
mkdir raw
mkdir data
cd raw

#wget https://s3.amazonaws.com/opennmt-models/sum_transformer_model_acc_57.25_ppl_9.22_e16.pt

cd ..
