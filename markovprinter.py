#!/usr/bin/env python
import pickle, random
chain = pickle.load(open("chain.p", "rb"))

tweet = []
sword1 = "BEGIN"
sword2 = "NOW"

while True:
    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
    if sword2 == "END":
        break
    tweet.append(sword2)

fintweet = ' '.join(tweet)

if len(fintweet) < 140:
    print(fintweet)
