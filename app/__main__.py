# __main__.py
import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession

from app.core.conf_reader import read_config


def main():
    # load config
    read_config()
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    java_home = os.getenv('JAVA_HOME')
    spark_home = os.getenv('SPARK_HOME')

    print(f"JAVA_HOME: {java_home}")
    print(f"SPARK_HOME: {spark_home}")

    # Create Spark session
    spark = SparkSession.builder \
        .appName("MyPySparkApp") \
        .getOrCreate()

    # Your PySpark code here
    data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
    columns = ["Name", "Age"]

    df = spark.createDataFrame(data, columns)
    df.show()

    spark.stop()
