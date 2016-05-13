# Economic Analysis of the Correlation of Industries

## About

This library provides scripts and tools to analyze the Census' County
Business Patterns (CBP) dataset.

This framework is still under development, and will _not_ work out of the box
just yet (mostly because the data is not stored in the REPO -- it is too large
to put in git).

## Author

Tomas Reimers, 2016

## TODO

 - Write a script to automatically download the dataset
 - Add documentation

## File structure

This project is still in development, for that reason, I've released the file
structure for anyone who has stumbled upon this code base and is trying to
get it to work for themselves.

..
../data
../data/county_business_patterns
../data/county_business_patterns/csv
../data/county_business_patterns/csv/1986.csv
../data/county_business_patterns/csv/1987.csv
../data/county_business_patterns/csv/1988.csv
../data/county_business_patterns/csv/1989.csv
../data/county_business_patterns/csv/1990.csv
../data/county_business_patterns/csv/1991.csv
../data/county_business_patterns/csv/1992.csv
../data/county_business_patterns/csv/1993.csv
../data/county_business_patterns/csv/1994.csv
../data/county_business_patterns/csv/1995.csv
../data/county_business_patterns/csv/1996.csv
../data/county_business_patterns/csv/1997.csv
../data/county_business_patterns/csv/1998.csv
../data/county_business_patterns/csv/1999.csv
../data/county_business_patterns/csv/2000.csv
../data/county_business_patterns/csv/2001.csv
../data/county_business_patterns/csv/2002.csv
../data/county_business_patterns/csv/2003.csv
../data/county_business_patterns/csv/2004.csv
../data/county_business_patterns/csv/2005.csv
../data/county_business_patterns/csv/2006.csv
../data/county_business_patterns/csv/2007.csv
../data/county_business_patterns/csv/2008.csv
../data/county_business_patterns/csv/2009.csv
../data/county_business_patterns/csv/2010.csv
../data/county_business_patterns/csv/2011.csv
../data/county_business_patterns/csv/2012.csv
../data/county_business_patterns/csv/2013.csv
../data/county_business_patterns/csv/2014.csv
../data/county_business_patterns/csv/README.txt
../data/county_business_patterns/db
../data/county_business_patterns/db/db.db
../data/fips
../data/fips/2012.csv
../data/naics
../data/naics/1998.csv
../data/naics/2002.csv
../data/naics/2007.csv
../data/naics/2012.csv
../data/naics/README.txt
../data/shape_files
../data/shape_files/README.txt
../data/shape_files/us_counties
../data/shape_files/us_counties/us_counties.cpg
../data/shape_files/us_counties/us_counties.dbf
../data/shape_files/us_counties/us_counties.prj
../data/shape_files/us_counties/us_counties.shp
../data/shape_files/us_counties/us_counties.shp.ea.iso.xml
../data/shape_files/us_counties/us_counties.shp.iso.xml
../data/shape_files/us_counties/us_counties.shp.xml
../data/shape_files/us_counties/us_counties.shx
../scripts
../scripts/cbp_corr.py
../scripts/cbp_corr_from_pickle.py
../scripts/cbp_corr_graph_from_pickle.py
../scripts/cbp_corr_mem.py
../scripts/cbp_corr_to_pickle.py
../scripts/cbp_csv2sqlite.py
../scripts/cbp_db_connect.py
../scripts/cbp_graph_naics.py
../scripts/cbp_naics_stats.py
../scripts/cbp_order_naics.py
../scripts/cbp_sum_naics.py
../scripts/cbp_unique_naics_count.py
../scripts/convert_csv.py
../scripts/lib
../scripts/lib/.DS_Store
../scripts/lib/__init__.py
../scripts/lib/county_mapper
../scripts/lib/county_mapper/__init__.py
../scripts/lib/county_mapper/graph.py
../scripts/lib/county_mapper/graph_demo.py
../scripts/lib/sms
../scripts/lib/sms/__init__.py
../scripts/lib/sms/sms.py
../scripts/search_fips.py
../scripts/search_naics.py
../tmp
../tmp/naics_1999.pickle
../tmp/naics_2004.pickle
../tmp/naics_2009.pickle
../tmp/naics_2014.pickle
../tmp/naics_in_mem.pickle
