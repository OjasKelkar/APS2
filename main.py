from sensor2.exception import SensorException
from sensor2.logger import logging
import os
import sys
#from sensor2.utills import dump_csv_file_to_mongo_db
from sensor2.configuration.mongo_db import MongoDBClient
from sensor2.pipeline.training_pipeline import TrainPipeline

# def test_exception():
#     try:
#         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 



if __name__ == "__main__":

    # file_path="/Users/myhome/Downloads/sensorlive/aps_failure_training_set1.csv"
    # database_name="ineuron"
    # collection_name ="sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()


