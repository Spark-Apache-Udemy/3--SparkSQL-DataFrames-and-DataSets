
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as func


spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("./data/fakefriends-header.csv")

# Select only age and numFriends columns
friendsByAge = people.select("age", "friends")

# From friendsByAge we group by "age" and then compute average
friendsByAge.groupBy("age").avg("friends").show()

#Sorted 
friendsByAge.groupBy("age").avg("friends").sort("age").show()

# With a custom column name
friendsByAge.groupBy("age").agg(func.round(func.avg("friends"), 2)
  .alias("friends_avg")).sort("age").show()

spark.stop()