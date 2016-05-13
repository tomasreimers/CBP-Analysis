from search_fips import search_fips
from search_naics import search_naics
import matplotlib.pyplot as plt
import peewee as pw
import numpy as np
import pickle
import csv
import sys
import os

# define constants

# SEARCH_NAICS = "54171/" # Scientific R&D
NAICS_1 = "5417//" # finance
NAICS_2 = "334419"
# SEARCH_NAICS = "71111/" # theaters
# NAICS_1 = "518///" # software
# NAICS_2 = "6113//" # universities
# NAICS_1 = "315///" # clothing (fashion)
# NAICS_2 = "315///" # clothing (fashion)
DATABASE_FILE = '../data/county_business_patterns/db/db.db'
CURR_YEAR = 2014
TIMESHIFT = 0 # years until the time we're comparing against
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

query_1 = Entry.select().where(Entry.year == CURR_YEAR, Entry.naics == NAICS_1)
data_dict_1 = query2dd(query_1)

query_2 = Entry.select().where(Entry.year == CURR_YEAR, Entry.naics == NAICS_2)
data_dict_2 = query2dd(query_2)

x = []
y = []

for key in data_dict_1.keys():
    if key in data_dict_2:
        x.append(data_dict_1[key])
        y.append(data_dict_2[key])

corr_matrix = np.corrcoef(np.array(x), np.array(y))
corr = corr_matrix[0, 1]

print "Correlation", corr

plt.scatter(x, y)
plt.xlabel(search_naics(NAICS_1, year=CURR_YEAR) + "(" + str(NAICS_1) + ")", fontsize=12)
plt.ylabel(search_naics(NAICS_2, year=CURR_YEAR) + "(" + str(NAICS_2) + ")", fontsize=12)
plt.show()
