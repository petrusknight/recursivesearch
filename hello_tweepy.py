import tweepy
import json
import pymongo

print("hello_tweepy.py Loaded")

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client.twit_ids
if db == None:
    print ('kaaskoek')


# sirColgrevance
auth = tweepy.OAuthHandler("npb4vI5OhwkXyxY8ixvZ2qAHx","SR10qi0e2nLcl4a2cXDZ8ZNeM3MyaCdm31fVmD0Nm1MYhs8nB0")
auth.set_access_token("971671773933645824-B4U9gTzabJFqB7SjiMWKtjcisqPIvpL","0iDxzvlar7OIDH0RiJ4JL30muWBdzcc6OVudTuxA9MUC9")


#SirConstantine
# auth = tweepy.OAuthHandler("zqievuaw5A4ByVVtrVvcjGd5z","UZJ4X75Na20t80kxlEdfiVcvCrMVv9iFC7LURuU80TWo4yvBzs")
# auth.set_access_token("971671773933645824-ieJQ3Gifvwdtnl13EAgyQ9QFYrd865m","EQccniXzaQ48zKqvOo4jwOlXi50rj5zAF1yHrzFO55P0a")

ids = open("ids.json",'w')
nodelist = open("nodelist.json", 'a')
edgelist = open("edgelist.json",'w')
api = tweepy.API(auth)
source_id = ('209564656')
user = api.get_user(source_id)
ids_list = set()
node_list = set()
edgelist_dict = {'Source': [], 'Target': []}

print(user.id)
print(user.followers_count)
for friend in tweepy.Cursor(api.followers_ids, user_id='209564656').items():
    print(friend)
    ids_list.add(friend)
    node_list.add(friend)
    edgelist_dict["Source"].append(str(source_id))
    edgelist_dict["Target"].append(str(friend))

json.dump(edgelist_dict,edgelist)
json.dump(list(ids_list),ids)
json.dump(list(node_list),nodelist)
ids.close()
edgelist.close()
nodelist.close()
