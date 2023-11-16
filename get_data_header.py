# get_data_header.py
# Mason Sipe
#
# The purpose of this file is to read the dataset and to automatically gather the header information, along with any datatypes that may be
# useful to know upon first glance of retrieving the data.
#

# need to import for session creation
from pyspark.sql import SparkSession

# creating the session
spark = SparkSession.builder.appName("GetHeaderInformation").getOrCreate()

# read data from a specific file
df = spark.read.option("Header",True).option("InferSchema",True).csv("./DDoS_Dataset.csv")

# print the assumed header information
df.printSchema()