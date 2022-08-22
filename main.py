from datetime import date #Important for pythonanywhere tasks
import tweepy #API Stuff
import json

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
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #Upload video to the site
    media = api.media_upload(filename="./Mari.mp4", chunked=True, media_category='tweet_video')
    try:
        api.update_status(status="", media_ids=[media.media_id])
        print("Successfully posted video")
    except Exception as exception:
        print("Failed to post video, Logging information to Owner's DMs.")
        api.send_direct_message(recipient_id=ownerid, text="An error happened.\nFull info:\n%s" % exception) #Log error to your DMs

#Make sure it's actually running since it's running in docker
def checkifrunning():
    #Login
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #Weekly message check up
    api.send_direct_message(recipient_id=ownerid, text="This weekly message is to ensure the pythonanywhere server is still running!")

#Actually post the video to the site
if __name__ == '__main__':
    #Check if today is monday
    if(date.today().weekday() == 0):
        tweet()
    elif(date.today().weekday() == 2):
        #Feel free to comment these three lines out if you're confident it is running still
        print("Update day, check up on bot owner")
        checkifrunning()
    else:
        print("Today is not a Monday or a Wednesday, Exit bot")
