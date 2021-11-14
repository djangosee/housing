#!/usr/bin/python3.7

print("Connecting with OpenDataBcn..")
import sys
import argparse
import configparser
import numpy as np
from argparse import ArgumentDefaultsHelpFormatter
from loadFiles import *
import os
from examples.plotHousingPricesExample import *
from src.timeseries import *
print("Connected!")

def main():
    """Main"""

    parser = argparse.ArgumentParser(
        prog='Housing challenge script')

    parser.add_argument('code', nargs="?",type=str, help='OpenDataBcn code, example:Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual')
    parser.add_argument('-m','--map', action="store_true", help="Open Bcn map example")
    parser.add_argument('-d','--dataset',type=bool, action="store", help="Create csv file from code dataset")

    args = parser.parse_args()

    if args.map:
        print("Generating Map from OpenDataBcn...")
        openMapExample()
#    if args.dataset:
#        print("Saving dataset wth code:"+ args.code +"...")
#        saveCodeAsCsv()

main()
