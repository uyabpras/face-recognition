import tweepy
import datetime
ckey = 'xA9chfPK3sgQyCwMXPWMuf3kN'
csecret ='YKxl4GKKrlsq0cOugrKQny14PreC8xLo0baX0kpgf8C6cABWDX'
akey ='319032353-cv3RvSf6uGSWpUhypC7qgbl9uGuWYzDEojW08fD9'
asecret ='ABi9lJ6xeHJGXQoNZMdDCErb8MmkfiwQWFxoNx9EquSMI'

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)
api =tweepy.API(auth)

user = api.me()
print(user.name)
print(user.location)


#ink = input("Masukan Tweet")
#api.update_status(ink)
def posting_tamu():
    date = datetime.datetime.now()
    reg_format_date = date.strftime("%d-%m-%Y %I:%M:%S %p")
    api.update_with_media('my-image.png',"Tamu yang tidak dikenal, " + str(reg_format_date))

def posting_owner(owner):
    date = datetime.datetime.now()
    reg_format_date = date.strftime("%d-%m-%Y %I:%M:%S %p")
    api.update_with_media('my-image.png',"selamat datang ",owner + str(reg_format_date))
