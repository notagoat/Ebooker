#!/usr/bin/env python
import tweepy, time, re
import apiconfig

t = open('Tweets.txt', 'w') #Default file name

def limithandler(cursor): #Handles limits and pagination
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("Limit hit. Sleeping")
            time.sleep(60)

def scraper(api):
    i = 0 #Counts loops to print status
    c = 0 #Counts times of loop
    RTcheck = re.compile('.*RT @.*') #Removes RT's
    Usercheck = re.compile('\s*\.?(@\w*):?') #Removes @names
    Linkcheck = re.compile('(https?:\/\/.* )') #Removes Links (http or https)
    for status in limithandler(tweepy.Cursor(api.user_timeline, screen_name="realDonaldTrump").items()):
        tweet = status.text #Gets the text
        tweet = "BEGIN NOW " + tweet + " END" # Forms it for the markov
        tweet = tweet.replace('\n', ' ') #Removes New lines from tweets
        #Run regex checks
        tweet = RTcheck.sub('',tweet)
        tweet = Usercheck.sub('',tweet)
        tweet = Linkcheck.sub('',tweet)

        if tweet == "\n" or "":
            break #Removes blanks
        t.write("\n"+tweet) #Writes to file
        i += 1
        if i > 100: #Checks status and shows it's still running
            c +=1
            print("%d: Scraping..."% c)
            i = 0

def get_api():
    #Handles API requests
    auth = tweepy.OAuthHandler(apiconfig.cfg['consumer_key'], apiconfig.cfg['consumer_secret'])
    auth.set_access_token(apiconfig.cfg['access_token'], apiconfig.cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    api = get_api()
    scraper(api)

if __name__ == "__main__":
    main()
