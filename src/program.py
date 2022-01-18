import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.master('spark://host.docker.internal:7077').appName('myapp').getOrCreate()

print(spark.version)