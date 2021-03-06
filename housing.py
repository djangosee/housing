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
from datascrapping import *
print("Connected!")

def main():
    """Main"""

    parser = argparse.ArgumentParser(
        prog='Housing challenge script')

    parser.add_argument('code', nargs="?",type=str, help='OpenDataBcn code, example:Est_Mercat_Immobiliari_Lloguer_Mitja_Mensual')
    parser.add_argument('-m','--map', action="store_true", help="Open Bcn map example")
    parser.add_argument('-d','--dataset',action="store_true", help="Create csv file from code dataset")
    parser.add_argument('-s','--scrapping',action="store_true", help="Merge different datasets from codes")

    args = parser.parse_args()

    if args.map:
        print("Generating Map from OpenDataBcn...")
        openMapExample()
    if args.dataset:
        print("Saving dataset with code: "+ str(args.code))
        df = loadFiles([args.code])
        print("DataSet.csv generated!")
        df.to_csv("DataSet.csv")
    if args.scrapping:
        print("Loading datasets...")
        getScrapping()
        print("Data.csv generated!")

main()
