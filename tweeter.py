#!/usr/bin/env python
import tweepy,pickle,random,time
import apiconfig

#TODO: Check if api fails retry

def markov():
    chain = pickle.load(open("chain.p", "rb"))
    tweet = []
    sword1 = "BEGIN"
    sword2 = "NOW"
    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        tweet.append(sword2)
    fintweet = " ".join(tweet)
    if tweetcheck(fintweet) == True:
        return fintweet
    else:
        main() #This is shitty af but whatever. Needs a fix

def tweetcheck(tweet):
    if len(tweet) < 140:
        return True
    tweet = "BEGIN NOW " + tweet + " END"
    with open("Tweets.txt") as t:
        for line in t:
            if line == tweet:
                return True
        return False

def get_api():
    auth = tweepy.OAuthHandler(apiconfig.cfg['consumer_key'], apiconfig.cfg['consumer_secret'])
    auth.set_access_token(apiconfig.cfg['access_token'], apiconfig.cfg['access_token_secret'])
    return tweepy.API(auth)
    #Sorts API Requests

def main():
    api = get_api()
    while True:
        fintweet = markov()
        api.update_status(status=fintweet)
        time.sleep(3600)

if __name__ == "__main__":
    main()
