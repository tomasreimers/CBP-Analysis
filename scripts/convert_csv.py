import csv

FROM_FILE = "../data/naics/2007.orig.csv"
TO_FILE = "../data/naics/2007.csv"

with open(FROM_FILE, "r") as fromfile:
    with open(TO_FILE, "w") as tofile:
        towriter = csv.writer(tofile)

        lines = fromfile.readlines()
        for line in lines:
            line_parts = line.split("  ")
            towriter.writerow([line_parts[0].strip(), line_parts[1].strip()])
