import tweepy #API Stuff
import json

#Scheduling
import schedule
import time

with open("auth.json", "r") as file:
    data = json.load(file)

#Keys
consumer_key = data['consumer_key']
consumer_secret = data['consumer_secret']
access_token = data['access_token']
access_token_secret = data['access_token_secret']
#To log any error with the tweet function (MUST NEED OR IT'LL CRASH PROGRAM!!!)
ownerid = data['owner_id']

#Main course
def tweet():
    #Login
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    #Upload video to the site
    media = api.media_upload("MariDay.mp4")
    try:
        api.update_status(status="", media_ids=[media.media_id])
        print("Successfully posted video")
    except Exception as exception:
        print("Failed to post video, Logging information to Owner's DMs.")
        api.send_direct_message(recipient_id=ownerid, text="An error happened.\nFull info:\n%s" % exception) #Log error to your DMs

#Make sure it's actually running since it's running in docker
def checkifrunning():
    #Login
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    #lol
    api.send_direct_message(recipient_id=ownerid, text="This message is to ensure the program is running correctly!")

#Actually post the video to the site
if __name__ == '__main__':
    #But check if docker is running the app first,
    checkifrunning()
    #then NOW run this once so it runs every mondays
    schedule.every().monday.at("09:00").do(tweet)
    while True:
        schedule.run_pending()
        time.sleep(1)