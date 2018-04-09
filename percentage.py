#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("primeiro", help="calcula o crescimento em % desse numero para o proximo", type=int)
parser.add_argument("segundo", help="calcula o crescimento do primeiro numero para este em %", type=int)
args = parser.parse_args() 

print(((args.segundo - args.primeiro) / abs(args.segundo)) * 100)
