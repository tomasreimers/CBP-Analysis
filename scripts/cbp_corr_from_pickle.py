from search_fips import search_fips
from search_naics import search_naics
import peewee as pw
import numpy as np
import pickle
import csv
import sys
import os

# define constants

SEARCH_NAICS = "5417//" # Scientific R&D
# SEARCH_NAICS = "541711"
# SEARCH_NAICS = "52----" # finance
# SEARCH_NAICS = "71111/" # theaters
# SEARCH_NAICS = "518///" # software
# SEARCH_NAICS = "6113//" # universities
# SEARCH_NAICS = "315///" # clothing (fashion)
DATABASE_FILE = '../data/county_business_patterns/db/db.db'
CURR_YEAR = 2014
TIMESHIFT = 15 # years until the time we're comparing against
SMS_EVERY = 1000

OTHER_YEAR = CURR_YEAR - TIMESHIFT

# utility functions

def log(s, sms=False):
    print s

def log_ephemeral(s):
    sys.stdout.write("\r" + s)
    sys.stdout.flush()

def query2dd(query):
    data_dict = {}
    for row in query:
        data_dict[(row.fipstate, row.fipscty)] = row.emp
    return data_dict

def query2dds(query):
    data_dicts = {}
    total = query.count()
    completed = 0
    for row in query:
        if completed % SMS_EVERY == 0:
            log("(" + str(completed) + " complete, of " + str(total) + ")")

        if row.naics not in data_dicts:
            data_dicts[row.naics] = {}
        data_dicts[row.naics][(row.fipstate, row.fipscty)] = row.emp

        completed += 1
    return data_dicts

# open the database and construct model

log("[Setting up DB]")

db = pw.SqliteDatabase(DATABASE_FILE)

class Entry(pw.Model):
    fipstate = pw.CharField()
    fipscty = pw.CharField()
    naics = pw.CharField()
    empflag = pw.CharField()
    emp = pw.IntegerField()
    qp1 = pw.IntegerField()
    ap = pw.IntegerField()
    est = pw.IntegerField()
    n1_4 = pw.IntegerField()
    n5_9 = pw.IntegerField()
    n10_19 = pw.IntegerField()
    n20_49 = pw.IntegerField()
    n50_99 = pw.IntegerField()
    n100_249 = pw.IntegerField()
    n250_499 = pw.IntegerField()
    n500_999 = pw.IntegerField()
    n1000 = pw.IntegerField()
    n1000_1 = pw.IntegerField()
    n1000_2 = pw.IntegerField()
    n1000_3 = pw.IntegerField()
    n1000_4 = pw.IntegerField()
    censtate = pw.CharField()
    cencty = pw.CharField()
    year = pw.IntegerField()

    class Meta:
        database = db

db.connect()

# get distinct naics for the YEAR
log("[Getting Distinct NAICS]")

query = Entry.select(Entry.naics).distinct().where(Entry.year == OTHER_YEAR)
distinct_naics_list = [row.naics for row in query]

# Join where
log("[Fetching data]")

query = Entry.select().where(Entry.year == CURR_YEAR, Entry.naics == SEARCH_NAICS)
data_dict = query2dd(query)

other_data_dicts = pickle.load(open("../tmp/naics_" + str(OTHER_YEAR) + ".pickle", "r"))

correlations = {}

complete = 0
for other_naics in distinct_naics_list:
    if complete % SMS_EVERY == 0:
        log(str(complete) + " complete")

    x = []
    y = []

    other_data_dict = other_data_dicts[other_naics]

    for key in data_dict.keys():
        if key in other_data_dict:
            x.append(data_dict[key])
            y.append(other_data_dict[key])

    corr_matrix = np.corrcoef(np.array(x), np.array(y))
    corr = corr_matrix[0, 1]

    if np.isnan(corr):
        continue

    if (corr_matrix[0, 1] != corr_matrix[1, 0]):
        log("HUH? Correlations don't match: " + str(corr_matrix[0, 1]) + ", " + str(corr_matrix[1, 0]))

    assert(other_naics not in correlations)
    correlations[other_naics] = corr

    complete += 1

correlations_list = list(correlations.iteritems())
correlations_list.sort(key=lambda x: x[1])

for naics, corr in correlations_list:
    print search_naics(naics, year=OTHER_YEAR), "(", naics, ")", ":", corr
