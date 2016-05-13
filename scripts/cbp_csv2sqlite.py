import peewee as pw
import csv
import sys
import os

# define constants

DATABASE_FILE = '../data/county_business_patterns/db/db.db'
CSV_PATH = '../data/county_business_patterns/csv'

def get_csv_name(year):
    return os.path.join(CSV_PATH, str(year) + '.csv')

START_YEAR = 1998 # prior to 1998, the data uses SIC instead of NAICS
END_YEAR = 2014
DISPLAY_NUM = 10000

expected_fields = [
    'fipstate',
    'fipscty',
    'naics',
    'empflag',
    'emp',
    'qp1',
    'ap',
    'est',
    'n1_4',
    'n5_9',
    'n10_19',
    'n20_49',
    'n50_99',
    'n100_249',
    'n250_499',
    'n500_999',
    'n1000',
    'n1000_1',
    'n1000_2',
    'n1000_3',
    'n1000_4',
    'censtate',
    'cencty'
]

# utility functions

def log(s):
    print s

def log_ephemeral(s):
    sys.stdout.write("\r" + s)
    sys.stdout.flush()

# open the database and construct model

if os.path.exists(DATABASE_FILE):
    log("Old database found, deleting.")
    os.remove(DATABASE_FILE)

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
db.create_tables([Entry])

# iterate through years
for year in xrange(START_YEAR, END_YEAR + 1):
    log("[Importing year " + str(year) + "]")

    # open file
    with open(get_csv_name(year), 'r') as csvfile:
        # open the csv
        dr = csv.DictReader(csvfile)

        # verify integrity
        if not (set(expected_fields) <= set(dr.fieldnames)):
            log(" -> Year " + str(year) + " could not be imported.")
            log(" -> Missing: " + str( set(expected_fields) - set(dr.fieldnames) ))
            continue

        # import
        num_imported = 0
        with db.transaction() as txn:
            for row in dr:
                if num_imported % DISPLAY_NUM == 0:
                    log_ephemeral("Importing "  + str(num_imported) + "          ")
                    txn.commit()

                curr = Entry(
                    fipstate=row['fipstate'],
                    fipscty=row['fipscty'],
                    naics=row['naics'],
                    empflag=row['empflag'],
                    emp=int(row['emp']),
                    qp1=int(row['qp1']),
                    ap=int(row['ap']),
                    est=int(row['est']),
                    n1_4=int(row['n1_4']),
                    n5_9=int(row['n5_9']),
                    n10_19=int(row['n10_19']),
                    n20_49=int(row['n20_49']),
                    n50_99=int(row['n50_99']),
                    n100_249=int(row['n100_249']),
                    n250_499=int(row['n250_499']),
                    n500_999=int(row['n500_999']),
                    n1000=int(row['n1000']),
                    n1000_1=int(row['n1000_1']),
                    n1000_2=int(row['n1000_2']),
                    n1000_3=int(row['n1000_3']),
                    n1000_4=int(row['n1000_4']),
                    censtate=row['censtate'],
                    cencty=row['cencty'],
                    year=year
                )
                curr.save()

                num_imported += 1
