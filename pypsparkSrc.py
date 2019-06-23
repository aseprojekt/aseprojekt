import numpy as np
import json

from pyspark.sql import types, functions, SQLContext, Row, Column
from pyspark import SparkContext


def convert_data(srcFilename, dstFilename):
    with open(srcFilename, 'r') as DataFile:
        collectedData = json.load(DataFile)['data']



if __name__ == '__main__':
    spark_ctx = SparkContext()
    sql_ctx = SQLContext

    types.StructType([types.StructField('id', types.StringType()), types.StructField('company', types.StringType()), \
                      types.StructField('city', types.StringType()), types.StructField('name', types.StringType())])
