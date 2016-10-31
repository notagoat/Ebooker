#!/usr/bin/env python
import tweepy, time, re, sys
import apiconfig

t = open('Tweets.txt', 'w') #Default file name

def limithandler(cursor): #Handles limits and pagination
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("Limit hit. Sleeping")
            time.sleep(60)

def scraper():
    i = 0 #Counts loops to print status
    api = get_api()
    namecheck = False

    while namecheck == False:
        name = input("Name for Scraping: ")
        try:
            check = api.get_user(id = name)
            print("Name: " + check.name)
            print("Tweet Count: %d "% check.statuses_count)
            print("\n")
            namecheck = True
        except Exception as e:
            print("Name is not valid. Please retry.")
            pass

    RTcheck = re.compile('.*RT @.*') #Removes RT's
    Usercheck = re.compile('\s*\.?(@\w*):?') #Removes @names
    Linkcheck = re.compile('(https?:\/\/.* )') #Removes Links (http or https)
    for status in limithandler(tweepy.Cursor(api.user_timeline, screen_name=name).items()):
    #TODO: Add check for valid name else fail (loop and var?)
        tweet = status.text #Gets the text
        tweet = "BEGIN NOW " + tweet + " END" # Forms it for the markov
        tweet = tweet.replace('\n', ' ') #Removes New lines from tweets
        #Run regex checks
        tweet = RTcheck.sub('',tweet)
        tweet = Usercheck.sub('',tweet)
        tweet = Linkcheck.sub('',tweet)

        if tweet != "\n" or "":
            t.write("\n"+tweet) #Writes to file
            i += 1
            if i % 100 == 0: #Checks status and shows it's still running
                temp = i / 100
                print("%d : Scraping..." % temp )
    print("\n%d Tweet's scraped." %i)
def get_api():
    #Handles API requests
    auth = tweepy.OAuthHandler(apiconfig.cfg['consumer_key'], apiconfig.cfg['consumer_secret'])
    auth.set_access_token(apiconfig.cfg['access_token'], apiconfig.cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    scraper()

if __name__ == "__main__":
    main()
