import botometer
import json
import pymongo
import numpy
import tweepy

print("Search.py Loaded")

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client.twit_ids
db_bot = client.bot_ids
db_notbot = client.notbot_ids
if db == None:
    print ('kaaskoek')

# user = {"_id":164628182, "id_str":str(164628182), "friends_ids": ["164628183", "164628184", "164628185"] }
#
user_database = db.twit_ids
# handle_return = user_database.insert_one(user).inserted_id
# print (handle_return)

for user in user_database.find():
    print(user["friends_ids"])
mashape_key = "BSFpXdyE3FmshqYT7Muon7z6Sj6Dp1LSM4gjsnXqR6SYFhd93q"

# #SirBredbeddle
# twitter_app_auth = {
#     'consumer_key': 'TvBda1gItC98cdU9iSXY8cM65',
#     'consumer_secret': 'zcVRxr0to7mgu9FBtkD2fRJE7FAGU3uak8xS2MYStlzibeBxqu',
#     'access_token': '971671773933645824-FmDlseKdoHxqOkEuWJD9NvfcEfCLDOj',
#     'access_token_secret': 'ZGadThrGEqi5l5kJT3pqMpMAA0o4DO2YIFhPgwdFuRMzc',
# }

#SirConstantine
twitter_app_auth = {
    'consumer_key': 'zqievuaw5A4ByVVtrVvcjGd5z',
    'consumer_secret': 'UZJ4X75Na20t80kxlEdfiVcvCrMVv9iFC7LURuU80TWo4yvBzs',
    'access_token': '971671773933645824-ieJQ3Gifvwdtnl13EAgyQ9QFYrd865m',
    'access_token_secret': 'EQccniXzaQ48zKqvOo4jwOlXi50rj5zAF1yHrzFO55P0a',
}

auth = tweepy.OAuthHandler("npb4vI5OhwkXyxY8ixvZ2qAHx","SR10qi0e2nLcl4a2cXDZ8ZNeM3MyaCdm31fVmD0Nm1MYhs8nB0")
auth.set_access_token("971671773933645824-B4U9gTzabJFqB7SjiMWKtjcisqPIvpL","0iDxzvlar7OIDH0RiJ4JL30muWBdzcc6OVudTuxA9MUC9")


bom = botometer.Botometer(wait_on_ratelimit=True,
mashape_key=mashape_key,
**twitter_app_auth)

print ("blah")
def search_run():
    pass

    # ids = open("ids.json",'r')
    # api = tweepy.API(auth)
    # data = ids.read()
    # item_dict = json.loads(data)
    # count_ids = len(item_dict)
    # details_file = open("full_detail.json", 'w')
    # data_file = open("data.json", 'w')
    # alleg_bot = open("abot_ids.json", 'w')
    # alleg_notbot = open("anotbot_ids.json", 'w')
    # attributelist = open("attributelist.json", 'w')
    # abot_ids = list()
    # anotbot_ids = list()
    # attributelist_dict = {'ID': [], 'BS': []}
    #
    # for x in range(0, count_ids):
    #     print("Busy with:", item_dict[x])
    #     user = api.get_user(item_dict[x])
    #     if user.protected == False:
    #         result = bom.check_account(item_dict[x])
    #         data_file.write(str(item_dict[x]))
    #         score_mean = numpy.mean(list(result["categories"].values()))
    #         temporal = result["categories"]["temporal"]
    #         data_file.write(" " + str(score_mean) + "\n")
    #         attributelist_dict["ID"].append(str(item_dict[x]))
    #         attributelist_dict["BS"].append(str(score_mean))
    #         if score_mean >= 0.65 or temporal >=0.7:
    #             abot_ids.append(item_dict[x])
    #         else:
    #             anotbot_ids.append(item_dict[x])
    #         json.dump(result,details_file)
    #         details_file.write(" " + str(score_mean)+ "\n")
    #
    # json.dump(attributelist_dict,attributelist)
    # json.dump(abot_ids,alleg_bot)
    # json.dump(anotbot_ids,alleg_notbot)
    # alleg_bot.close()
    # alleg_notbot.close()
    # data_file.close()
    # details_file.close()
