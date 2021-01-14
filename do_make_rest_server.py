#!/usr/bin/env python3.6

import sys
import os
import argparse


IP="127.0.0.1"
PORT=str(5000)
URL_ROOT="/"  #"/OpenNMT-py"
CONFIG="json/server_conf_best.json"

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Start server.')
    parser.add_argument('--modified', help='Launch with modified source.', action="store_true")
    parser.add_argument('serve', help='Serve from this saved checkpoint.', nargs="?")
    args = parser.parse_args()
    print(sys.argv)

    if os.path.isfile(str(args.serve)):
        print('remove old best')
        try:
            os.system("rm data/transformer_movie_chat_step_best.pt")
        except:
            pass
        print("replace best")
        os.system("cp " + str(args.serve) + " data/transformer_movie_chat_step_best.pt")

    if args.modified == True:
        os.system("./bin/server.py --ip " + IP + " --port " + PORT + " --url_root " + URL_ROOT + " --config " + CONFIG)
        exit()
    else:
        URL_ROOT="/OpenNMT-py"
        os.system("onmt_server --ip " + IP + " --port " + PORT + " --url_root " + URL_ROOT + " --config " + CONFIG)
        exit()
    

