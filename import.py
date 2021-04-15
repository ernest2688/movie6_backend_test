import pandas as pd
import json
from datetime import datetime
import pytz
from datetime import timezone
import uuid
from pymongo import MongoClient
import math

#read the CSV
df = pd.read_csv ('movies.csv')

#turn to json
data = df.to_json(orient ='records',force_ascii=False)
#turn to dictionary
movie_list = json.loads(data)


#print(movie_list)

# create both timezone objects
old_timezone = pytz.timezone('Asia/Shanghai')
new_timezone = pytz.timezone('UTC')

for i in movie_list:
    i['_id'] = str(uuid.uuid4())
    
    
    odate = i['open_date']
    #turn to datetime object
    reviewDate = datetime.fromisoformat(odate)
    #print(reviewDate)

    #turn to timestamp with changing timezone from UTC+8 to UTC+0
    # two-step process
    localized_timestamp = old_timezone.localize(reviewDate)
    new_timezone_timestamp = localized_timestamp.astimezone(new_timezone)

    # or alternatively, as an one-liner
    new_timezone_timestamp = old_timezone.localize(reviewDate).astimezone(new_timezone) 

    #print(new_timezone_timestamp)

    timestamp = new_timezone_timestamp.replace(tzinfo=timezone.utc).timestamp()
    
    #save the modified opendate
    i['open_date'] = math.trunc(timestamp)
#print(movie_list)

#upload the movielist to the mongodb
client = MongoClient('localhost', port=27017)
db = client.newdb
record = db.movies
for m in movie_list:
    record.insert_one(m)

    
