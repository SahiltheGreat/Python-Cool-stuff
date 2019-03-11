import json
import urllib.request
key="AIzaSyBWzzwpgRwDak7YQgOII5OH6stk6oI3PqA"
#name="PewDiePie"
#d= urllib.request.urlopen
pew_url= "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=PewDiePie&key="+key
tseries_url="https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+key
pew_data=urllib.request.urlopen(pew_url).read()
tseries_data=urllib.request.urlopen(tseries_url).read()
#subs=json.loads(data
pew_subs=json.loads(pew_data)["items"][0]["statistics"]["subscriberCount"]
tseries_subs=json.loads(tseries_data)["items"][0]["statistics"]["subscriberCount"]
x=int(pew_subs,10)
y=int(tseries_subs,10)
k=x-y
#print(k)
print("PewDiePie has "+pew_subs+" subscribers")
#diff=(int)pew_subs-(int)tseries_subs
print("Tseries has "+tseries_subs+" subscribers")
print("Difference in their subscribers=")
print(k)
#print(name + "has" + "{:,d}".format(int(pewdi)) + "subscribers!")
