#!/usr/bin/env python3

import argparse 
import yaml
from logger import logger


def main():
    parser = argparse.ArgumentParser(description='T1 CLI')
    parser.add_argument('--infile', type=argparse.FileType('r', encoding='UTF-8'), 
                      required=True)
    args = parser.parse_args()
    data_loaded = yaml.safe_load(args.infile)
    print(data_loaded)
    args.infile.close()

    
if __name__ == '__main__':
    main()