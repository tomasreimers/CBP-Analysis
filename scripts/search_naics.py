import csv
import sys
import os

# define constants

NAICS_DIR = '../data/naics'
DEFAULT_YEAR = 2012
YEARS = [1998, 2002, 2007, 2012]

# utility functions

def get_naics_file_for(year):
    return os.path.join(NAICS_DIR, str(year) + ".csv")

def log(s):
    print s

def log_ephemeral(s):
    sys.stdout.write("\r" + s)
    sys.stdout.flush()

def get_max_year_beneath(year):
    return max([x for x in YEARS if x < year])

# open the naics file

naics_lists = {}

def load_naics_year(year):
    if year not in naics_lists:
        with open(get_naics_file_for(year), 'r') as naics_file:
            naics_dr = csv.DictReader(naics_file)
            naics_list = list(naics_dr)
        naics_lists[year] = naics_list

    return naics_lists[year]

def search_naics(code, year=DEFAULT_YEAR):
    year = get_max_year_beneath(year)
    for naics_row in load_naics_year(year):
        if naics_row['NAICS'] == code:
            return naics_row['DESCRIPTION']
    return "<UNKNOWN>"

if __name__ == "__main__":
    # ask the user what they want to query for
    while True:
        search_term = raw_input("Query: ")

        if search_term == "exit":
            sys.exit()

        matching_terms = [naics_row for naics_row in load_naics_year(DEFAULT_YEAR) if search_term.lower() in naics_row['DESCRIPTION'].lower()]
        for matching_term in matching_terms:
            print matching_term['NAICS'], ":", matching_term['DESCRIPTION']
