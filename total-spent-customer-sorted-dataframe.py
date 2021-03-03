from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

#Create session
spark = SparkSession.builder.appName("TotalSpentByCustomer").master("local[*]").getOrCreate()

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")



# Create schema when reading customer-orders
schema = StructType([ StructField("cust_id", IntegerType(), True),
                      StructField("item_id", IntegerType(), True),
                     StructField("amount_spent", FloatType(), True)])


# Load up the data into spark dataset
customerDF = spark.read.schema(schema).csv("./data/customer-orders.csv")

customerDF.printSchema()


totalByCustomer = customerDF.groupBy("cust_id").agg(func.round(func.sum("amount_spent"),2).alias('total_spent') )

totalByCustomerSorted = totalByCustomer.sort("total_spent")

totalByCustomerSorted.show(totalByCustomerSorted.count())

totalByCustomerSorted.show(totalByCustomerSorted.count())

spark.stop()


