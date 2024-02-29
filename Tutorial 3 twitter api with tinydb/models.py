from fastapi import HTTPException
from datetime import date
from tinydb import TinyDB, Query
db = TinyDB('twitter.json')
tweet_table = db.table('tweet')

class User:
    def __init__(self,u,p):
        self.user_id = None
        self.userName=u
        self.password=p
        self.followers=[]
        self.following=[]
        self.joinedDate = date.today().strftime("%Y-%m-%d")

class tweet:
    def __init__(self,id,u,tweet):
        self.user_id = id
        self.userName=u
        self.tweet=tweet
        self.date=date.today().strftime("%Y-%m-%d")


u=User("farhan 1", "test")
print(vars(u))



def throwThisExcption(a="",status=""):
    print(f"{a}.")
    raise  HTTPException(status_code=status,detail=a)


def insertUser(a):
    a=vars(a)
    users_table = db.table('users')
    result=users_table.search(Query().userName==a['userName'])
    if len(result)==0:
        a['id']=len(users_table.all())
        users_table.insert(a)
        print("data was inserted:"+str(a))
    else:
        throwThisExcption("cant create duplicate data",404)



def searchUser(userName):
    users_table = db.table("users")
    result = users_table.search(Query().userName == userName)
    if len(result) == 0:
        throwThisExcption("no data found",404)
    return result

def followUser(currentUserName,userNametoFollow):
    users_table = db.table("users")
    current = users_table.search(Query().userName == currentUserName)
    userTofollow = users_table.search(Query().userName == userNametoFollow)
    current['following'].append(userTofollow.user_id)
    userTofollow['followers'].append(current.user_id)
    records.update(current,  Query().user_id == current.user_id)
    records.update(userTofollow,  Query().user_id == userTofollow.user_id)


def fetchTweets(ids_to_search):
    records = db.table('tweets')
    result = records.search(Query().id.one_of(ids_to_search))
    sorted_records = sorted(records.all(), key=lambda x: x['joinedDate']).reverse()
    return sorted_records

def fetchFollowedTweets(userName):
    users_table = db.table("users")
    user = users_table.search(Query().userName == userName)
    return fetchTweets(user['following'])




# insertUser(User( 'farhan1',  25))
# insertUser(User( 'farhan',  25))
# insertUser(User( 'zabir',  25))
# insertUser(User( 'tanvir',  25))
# insertUser(User( 'raisul',  25))
# insertUser(User( 'tibro',  25))
#
#
# records = db.table('users')
# sorted_records = sorted(records.all(), key=lambda x: x['joinedDate'])
# print(sorted_records)
# print(records)
#
#
# print(searchUser("farhan"))