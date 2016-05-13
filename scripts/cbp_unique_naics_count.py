from search_fips import search_fips
from lib.sms.sms import send
import peewee as pw
import numpy as np
import csv
import sys
import os

# define constants

SEARCH_NAICS = "54----"
DATABASE_FILE = '../data/county_business_patterns/db/db.db'
CURR_YEAR = 2014
TIMESHIFT = 0 # years until the time we're comparing against
SMS_EVERY = 100

OTHER_YEAR = CURR_YEAR - TIMESHIFT

# utility functions

def log(s, sms=False):
    print s
    if sms:
        send(s)

def log_ephemeral(s):
    sys.stdout.write("\r" + s)
    sys.stdout.flush()

def query2dd(query):
    data_dict = {}
    for row in query:
        data_dict[(row.fipstate, row.fipscty)] = row.emp
    return data_dict

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

log(Entry.select(Entry.naics).distinct().where(Entry.year == OTHER_YEAR).count())
