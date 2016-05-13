import csv
import sys
import os

# define constants

FIPS_FILE = '../data/fips/2012.csv'

# utility functions

def log(s):
    print s

def log_ephemeral(s):
    sys.stdout.write("\r" + s)
    sys.stdout.flush()

# open the naics file

with open(FIPS_FILE, 'r') as fips_file:
    fips_dr = csv.DictReader(fips_file)
    fips_list = list(fips_dr)

def search_fips(fips_state, fips_cty):
    for fips_row in fips_list:
        if fips_row['fipstate'] == fips_state and fips_row['fipscty'] == fips_cty:
            return fips_row['ctyname']
    return "<UNKNOWN>"

if __name__ == "__main__":
    while True:
        search_term = raw_input("Query: ")

        if search_term == "exit":
            sys.exit()

        matching_terms = [fips_row for fips_row in fips_list if search_term.lower() in fips_row['ctyname'].lower()]
        for matching_term in matching_terms:
            print matching_term['ctyname'], ":", matching_term['fipstate'], ",", matching_term['fipscty']
