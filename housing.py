#!/usr/bin/python3.7

import sys
import argparse
import configparser
import numpy as np
from argparse import ArgumentDefaultsHelpFormatter
from loadFiles import *
import os
from src.timeseries import *

def main():
    """Main"""

    parser = argparse.ArgumentParser(
        prog='Housing challenge script')

    parser.add_argument('code', type=str, help='OpenDataBcn code, example:Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual')
    args = parser.parse_args()

    df = loadFiles([args.code])
    print("Se esta abriendo el mapa..")

main()
