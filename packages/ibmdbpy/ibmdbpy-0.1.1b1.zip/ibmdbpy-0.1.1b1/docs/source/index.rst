.. Ibmdbpy documentation master file, created by
   sphinx-quickstart on Tue Jul 14 13:18:19 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. Ibmdbpy documentation master file, created by
   sphinx-quickstart on Tue Jul 14 13:18:19 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ibmdbpy
*******

Accelerating Python Analytics by In-Database Processing
=======================================================

The ibmdbpy project provides a Python interface for data manipulation and access to in-database algorithms in IBM dashDB and IBM DB2. It accelerates Python analytics by seamlessly pushing operations written in Python into the underlying database for execution, thereby benefitting from in-database performance-enhancing features, such as columnar storage and parallel processing.

IBM dashDB is a database management system available on IBM Bluemix, the cloud application development and analytics platform powered by IBM. The ibmdbpy project can be used by Python developers with very little additional knowledge, because it copies the well-known interface of the Pandas library for data manipulation and the Scikit-learn library for the use of machine learning algorithms.

The ibmdbpy project is compatible with Python releases 2.7 up to 3.4 and can be connected to dashDB or DB2 instances via ODBC or JDBC.

The project is still at an early stage and many of its features are still in development. However, several experiments have already demonstrated that it provides significant performance advantages when operating on medium or large amounts of data, that is, on tables of 1 million rows or more.

The latest version of ibmdbpy is available on the `Python Package Index`__.

__ https://pypi.python.org/pypi/ibmdbpy

How ibmdbpy works
-----------------

The ibmdbpy project translates Pandas-like syntax into SQL and uses a middleware API (pypyodbc/JayDeBeApi) to send it to an ODBC or JDBC-connected database for execution. The results are fetched and formatted into the corresponding data structure, for example, a Pandas.Dataframe or a Pandas.Series.

The following scenario illustrates how ibmdbpy works.

Assuming that all ODBC connection parameters are correctly set, issue the following statements to connect to a database (in this case, a dashDB instance named DASHDB) via ODBC:

>>> from ibmdbpy import IdaDataBase, IdaDataFrame
>>> idadb = IdaDataBase('DASHDB')

A few sample data sets are included in ibmdbpy for you to experiment. We can firstly load the well-known IRIS table into this dashDB instance.

>>> from ibmdbpy.sampledata import iris
>>> idadb.as_idadataframe(iris, "IRIS")
<ibmdbpy.frame.IdaDataFrame at 0x7ad77f0>

Next, we can create an IDA data frame that points to the table we just uploaded. Let’s use that one:

>>> idadf = IdaDataFrame(idadb, 'IRIS')

Note that to create an IDA data frame using the IdaDataFrame object, we need to specify our previously opened IdaDataBase object, because it holds the connection.

Now let us compute the correlation matrix:

>>> idadf.corr()

In the background, ibmdbpy looks for numerical columns in the table and builds an SQL request that returns the correlation between each pair of columns. Here is the SQL request that was executed for this example::

   SELECT CORRELATION("sepal_length","sepal_width"),
   CORRELATION("sepal_length","petal_length"),
   CORRELATION("sepal_length","petal_width"),
   CORRELATION("sepal_width","petal_length"),
   CORRELATION("sepal_width","petal_width"),
   CORRELATION("petal_length","petal_width")
   FROM IRIS

The result fetched by ibmdbpy is a tuple containing all values of the matrix. This tuple is formatted back into a Pandas.DataFrame and then returned::

                 sepal_length  sepal_width  petal_length  petal_width
   sepal_length      1.000000    -0.117570      0.871754     0.817941
   sepal_width      -0.117570     1.000000     -0.428440    -0.366126
   petal_length      0.871754    -0.428440      1.000000     0.962865
   petal_width       0.817941    -0.366126      0.962865     1.000000

Et voilà !

Geospatial Functions
====================

The ibmdbpy package now supports geospatial functions! It provides a Python interface for data manipulation and access to in-database algorithms in IBM dashDB and IBM DB2 Spatial Extender.
It accelerates Python analytics by seamlessly pushing spatial operations written in Python into the underlying database for execution,
thereby benefitting from in-database performance-enhancing features, such as columnar storage and parallel processing.

The ibmdbpy spatial functions can be used by geospatial analysts with very little additional knowledge, because it copies the well-known interface of the geopandas library for data manipulation.

These functions are compatible with Python releases 2.7 up to 3.4 and can be connected to dashDB or DB2 instances via ODBC or JDBC.

Table of Contents
=================

.. highlight:: python

.. toctree::
   :maxdepth: 2

   install.rst
   start.rst
   base.rst
   frame.rst
   ml.rst
   geospatial.rst
   utils.rst
   legal.rst

Project Roadmap
===============

* Full test coverage (a basic coverage is already provided)
* Add more functions and improve what already exists.
* Add wrappers for several ML-Algorithms (Linear regression, Sequential patterns...)
* Add more wrappers for spatial functions
* Feature selection extension
* Add Spark as computational engine


Contributors
============

The ibmdbpy project was initiated in April 2015, and developed by Edouard Fouché and the geospatial features were added in March 2016,
and contributed by Rafael Rodriguez Morales and Avipsa Roy at IBM Deutschland Reasearch & Development.

Indexes and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


