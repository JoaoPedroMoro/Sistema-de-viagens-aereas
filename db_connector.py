import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession


class spark_conn:
    def __init__(self):
        load_dotenv()
        self.session = None
        self.database = os.getenv('database')
        self.collection = os.getenv('collection')
        self.host_address = os.getenv('host_address')
        self._start_session()

    def _start_session(self):
        self.session = SparkSession.builder \
            .master("local") \
            .appName("MongoDB") \
            .config("spark.mongodb.read.connection.uri", self.host_address) \
            .config("spark.mongodb.write.connection.uri", self.host_address) \
            .getOrCreate()

    def stop_session(self):
        if self.session is not None: self.session.stop()

    def read(self,columns = []):
        df = self.session.read.format("mongodb") \
                .option("uri", "mongodb://localhost:27017/") \
                .option("database", self.database) \
                .option("collection", self.collection) \
                .load()
        if columns:
            df = df.select([col for col in columns])
        return df
    
    def write(self,df):
        df.write.format("mongodb") \
            .mode("append") \
            .option("database", self.database) \
            .option("collection", self.collection) \
            .save()

    