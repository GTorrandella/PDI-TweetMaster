'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import Tweet as tweet
import Campaign

lastId = "967824267948770000"

campaign = Campaign.Campaign("idC", "emailDueño", ["mars"], ["mars"], date.today(), date.today())

hastag = {
        "statuses": [
                {
                        "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                        "id_str": "967824267948773377",
                        "entities": {
                                "hashtags": ["mars"],
                                "symbols": [],
                                "user_mentions": [],
                                },
                        "user": {
                                "id_str": "11348282",
                                "name": "NASA"
                                }
                },
                {
                        "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                        "id_str": "967824267948773378",
                        "entities": {
                                "hashtags": ["mars"],
                                "symbols": [],
                                "user_mentions": [],
                                },
                        "user": {
                                "id_str": "11348282",
                                "name": "NASA"
                                }
                }
            ]
}

mention = {
        "statuses": [
                {
                        "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                        "id_str": "967824267948773377",
                        "entities": {
                                "hashtags": [],
                                "user_mentions": ["mars"],
                                },
                        "user": {
                                "id_str": "11348282",
                                "name": "NASA"
                                }
                },
                {
                        "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                        "id_str": "967824267948773378",
                        "entities": {
                                "hashtags": [],
                                "user_mentions": ["mars"],
                                },
                        "user": {
                                "id_str": "11348282",
                                "name": "NASA"
                                }
                }
            ]
}

responseHastag = [tweet.Tweet(hastag["statuses"][0]), tweet.Tweet(hastag["statuses"][1])]
responseMention = [tweet.Tweet(mention["statuses"][0]), tweet.Tweet(mention["statuses"][1])]