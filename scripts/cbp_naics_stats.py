from search_fips import search_fips
import peewee as pw
import csv
import sys
import os

# define constants

DATABASE_FILE = '../data/county_business_patterns/db/db.db'
CURR_YEAR = 2014

# utility functions

def log(s):
    print s

def log_ephemeral(s):
    sys.stdout.write("\r" + s)
    sys.stdout.flush()

# open the database and construct model

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

total_rows = Entry.select().count()
total_naics = Entry.select(Entry.naics).distinct().count()
total_counties = Entry.select(Entry.fipstate, Entry.fipscty).distinct().count()
total_year = Entry.select(Entry.year).distinct().count()

print "total_rows", total_rows
print "total_naics", total_naics
print "total_counties", total_counties
print "total_year", total_year
