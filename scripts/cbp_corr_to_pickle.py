from search_fips import search_fips
from search_naics import search_naics
import peewee as pw
import numpy as np
import pickle
import csv
import sys
import os

# define constants

DATABASE_FILE = '../data/county_business_patterns/db/db.db'
SMS_EVERY = 10000
START_YEAR = 1998
END_YEAR = 2014
# YEARS = xrange(START_YEAR, END_YEAR + 1)
YEARS = [1999, 2004, 2009, 2014]

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
            log(" -> " + str(completed) + " complete (of " + str(total) + ")")

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

for year in YEARS:

    log("Processing data for year " + str(year))

    # get distinct naics for the YEAR

    query = Entry.select(Entry.naics).distinct().where(Entry.year == year)
    distinct_naics_list = [row.naics for row in query]

    # Join where

    other_query = Entry.select().where(Entry.year == year)
    other_data_dicts = query2dds(other_query)

    pickle.dump(other_data_dicts, open("../tmp/naics_" + str(year) + ".pickle", "w"))
