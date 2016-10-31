# Ebooker
Allows anyone to make their own Horse Ebooks clone easily!

## How To Use

The repo consists of 5 main files. This let's you scrape tweets, pickle them, test them, then print them on twitter.

1. apiconfig.py 
Use this to enter credentials from twitter.com to allow the script to get the tweets

2. scraper.py
Scrapes the tweets from the user name entered into the field

3. pickler.py
Compiles the tweets so they can be chained together

4. tweeter.py
Tweets the markov chains made from tweets

5. markovprinter.py
Runs the script, like it will be run in tweeter.py but does not post it to twitter

### Requirments

+ Python3
+ Tweepy
+ A twitter account with the API details saved
