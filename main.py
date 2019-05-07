import argparse
from process.load_data import download_data
from process.processing import *


def train(config):
    pass


def eval(config):
    pass


def test(config):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PyTorch Implementation of Region Embedding')
    parser.add_argument("--version", action='version', version=1.0)
    parser.add_argument('--action', '-a', required=True,
                        choices=['example', 'preprocess', 'train', 'eval', 'test'],
                        help='your action')
    parser.add_argument('--config', type=str,
                        default='conf/example.W.C.train.conf',
                        help='your configuration path')
    args = parser.parse_args()

    if args.action == 'example':
        print('=================  start downloading dataset =================')
        download_data()
        print('=================  start processing dataset  =================')
        process_data(args.config)
        print('=================       start training       =================')
        train(args.config)
        test(args.config)
        pass
    elif args.action == 'preprocess':
        while ensure not in ['Y', 'y', 'N', 'n'] and args.config == 'conf/example.W.C.train.conf':
            ensure = input("Are you sure to use the file '%s' as your config?[Y/N]" % args.config)
        if ensure == 'N' or 'n':
            exit(0)
        process_data(args.config)
    elif args.action == 'train':
        train(args.config)
    elif args.action == 'eval':
        eval(args.config)
    elif args.action == 'test':
        test(args.config)
    else:
        raise KeyError("this action not support")
