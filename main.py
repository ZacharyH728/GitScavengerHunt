import tweepy, json, time, random

class TwitterStreamListener(tweepy.streaming.StreamListener):
    ''' Handles data received from the stream. '''
    def on_status(self, status):
        # print(status.id)
        # print(status.user.name)
        # print(status.text)
        if len(status.text) < 200:
            if "RT" in status.text[:30]:
                print(status.user.name + " just tweeted with the #christmas saying " + status.text[(status.text.find(":")+1)::], "\n")
            else:
                print(status.user.name + " just tweeted with the #christmas saying " + status.text, "\n")
        else:
            print(status.user.name + " just printed with the #christmas", "\n")
        
        with open('PerHour.json') as f:
            data = json.load(f)
            dict2 = {'timevalue' + str(time.time()): time.time()}
            data.update(dict2)
            json.dump(data, open("PerHour.json","w"), indent=6)
            for timevalue in data:
                if time.time() - data[timevalue] > 1800:
                    del data[timevalue]
                    json.dump(data, open("PerHour.json","w"), indent=6)
                    break
            print("Number of tweets using #Christmas in the past halfhour: " + str(len(data)) + "\n")

        with open('PerMinute.json') as f:
            data = json.load(f)
            dict2 = {'timevalue' + str(time.time()): time.time()}
            data.update(dict2)
            json.dump(data, open("PerMinute.json","w"), indent=6)
            for timevalue in data:
                if time.time() - data[timevalue] > 60:
                    del data[timevalue]
                    json.dump(data, open("PerMinute.json","w"), indent=6)
                    break
            if len(data) > 0:
                christmas_spirit_value = "|~|~|~|~|~|~|~|~|~|~|"
                if len(data) > 10:
                    christmas_spirit_value = "|█|~|~|~|~|~|~|~|~|~|"
                    if len(data) > 20:
                        christmas_spirit_value = "|█|█|~|~|~|~|~|~|~|~|"
                        if len(data) > 30:
                            christmas_spirit_value = "|█|█|█|~|~|~|~|~|~|~|"
                            if len(data) > 40:
                                christmas_spirit_value = "|█|█|█|█|~|~|~|~|~|~|"
                                if len(data) > 50:
                                    christmas_spirit_value = "|█|█|█|█|█|~|~|~|~|~|"
                                    if len(data) > 60:
                                        christmas_spirit_value = "|█|█|█|█|█|█|~|~|~|~|"
                                        if len(data) > 70:
                                            christmas_spirit_value = "|█|█|█|█|█|█|█|~|~|~|"
                                            if len(data) > 80:
                                                christmas_spirit_value = "|█|█|█|█|█|█|█|█|~|~|"
                                                if len(data) > 90:
                                                    christmas_spirit_value = "|█|█|█|█|█|█|█|█|█|~|"
                                                    if len(data) > 100:
                                                        christmas_spirit_value = "|█|█|█|█|█|█|█|█|█|█|"
            print("The number of tweets using the #Christmas per minute is " + str(len(data)))
            #print("This means that the christmas spririt is " + christmas_spirit_value )
        # lightning(pastHalfHour)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening


listener = TwitterStreamListener()
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
stream = tweepy.streaming.Stream(auth, listener)
stream.filter(track=["#christmas"])
