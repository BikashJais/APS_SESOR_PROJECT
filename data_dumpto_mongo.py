import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
database_name = "APS"

# Collection  Name
collection_name = "sensor"
#data file path
data_path= "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":
    df=pd.read_csv(data_path)
    print(f"rows and columns: {df.shape}")


#convert dataframe to json so that it can be dumpt into mongodb

df.reset_index(drop=True,inplace=True)
json_record=list(json.loads(df.T.to_json()).values())

#insert concerted record to mongo db

client[database_name][collection_name].insert_many(json_record)
