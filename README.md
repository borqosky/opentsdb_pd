# opentsdb_pd
This module provides way to get data from OpenTSDB HTTP API and transform it to Pandas Timeseries in an efficient way.

opentsdb_pd
===============

This module is able to get data from [OpenTSDB](http://opentsdb.net/) through HTTP interface and convert them into pandas [Timeseries](http://pandas.pydata.org/pandas-docs/stable/timeseries.html). 
Basic structure is based mostly on [opentsdbr](https://github.com/holstius/opentsdbr/) and [opentsdb_pandas](https://github.com/wiktorski/opentsdb_pandas) libraries.

Initial goal is to get python3 compatibility, improve performance and bump to existing pandas version

Example usage
-------------
