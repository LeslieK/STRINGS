from twitter import TwitterStream, OAuth
from KnuthMorrisPratt import KMP

########################################################
if __name__ == "__main__":
    CREDS = {
        "consumer_key": "fill-in-your-key",
        "consumer_secret": "fill-in-your-secret",
        "token": "fill-in-your-token",
        "token_secret": "fill-in-your-token-secret"
    }

    auth = OAuth(
        consumer_key=CREDS["consumer_key"],
        consumer_secret=CREDS["consumer_secret"],
        token=CREDS["token"],
        token_secret=CREDS["token_secret"]
    )

    pat = "weapons"
    kmp = KMP(pat)
    pattern_index = 0

    id_dict = {
        "wikileaks": "16589206",
        "aljazeera": "76067316",
        "NYFBI": "211635204",
        "reutersiran": "47633485",
        "WhiteHouse": "30313925"
    }

    public_stream = TwitterStream(auth=auth, domain='stream.twitter.com')
    iterator = public_stream.statuses.filter(language="en",
                                             follow=','.join(id_dict.values()),
                                             track="terrorism, weapons, \
                                             drone attack, i wantill")
    for item in iterator:
        if item['retweeted'] is False:
            try:
                text = item['text']
                print text
                for c in text.encode():
                    #print c
                    pattern_index = kmp.dfa.next(c, pattern_index)
                    if int(pattern_index) == len(pat):
                        print "MATCH!!!!!"
            except:
                continue
