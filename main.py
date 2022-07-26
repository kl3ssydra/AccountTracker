from colorama import Fore
import requests
import time

username = input('[?] username : ')

instagram = f'https://www.instagram.com/{username}'
facebook = f'https://www.facebook.com/{username}'
twitter = f'https://www.twitter.com/{username}'
youtube = f'https://www.youtube.com/{username}'
blogger = f'https://{username}.blogspot.com'
google_plus = f'https://plus.google.com/s/{username}/top'
reddit = f'https://www.reddit.com/user/{username}'
wordpress = f'https://{username}.wordpress.com'
pinterest = f'https://www.pinterest.com/{username}'
github = f'https://www.github.com/{username}'
tumblr = f'https://{username}.tumblr.com'
flickr = f'https://www.flickr.com/people/{username}'
steam = f'https://steamcommunity.com/id/{username}'
vimeo = f'https://vimeo.com/{username}'
soundcloud = f'https://soundcloud.com/{username}'
disqus = f'https://disqus.com/by/{username}'
medium = f'https://medium.com/@{username}'
deviantart = f'https://{username}.deviantart.com'
vk = f'https://vk.com/{username}'
aboutme = f'https://about.me/{username}'
imgur = f'https://imgur.com/user/{username}'
flipboard = f'https://flipboard.com/@{username}'
slideshare = f'https://slideshare.net/{username}'
fotolog = f'https://fotolog.com/{username}'
spotify = f'https://open.spotify.com/user/{username}'
mixcloud = f'https://www.mixcloud.com/{username}'
scribd = f'https://www.scribd.com/{username}'
badoo = f'https://www.badoo.com/en/{username}'
patreon = f'https://www.patreon.com/{username}'
bitbucket = f'https://bitbucket.org/{username}'
dailymotion = f'https://www.dailymotion.com/{username}'
etsy = f'https://www.etsy.com/shop/{username}'
cashme = f'https://cash.me/{username}'
behance = f'https://www.behance.net/{username}'
goodreads = f'https://www.goodreads.com/{username}'
instructables = f'https://www.instructables.com/member/{username}'
keybase = f'https://keybase.io/{username}'
kongregate = f'https://kongregate.com/accounts/{username}'
livejournal = f'https://{username}.livejournal.com'
angellist = f'https://angel.co/{username}'
last_fm = f'https://last.fm/user/{username}'
dribbble = f'https://dribbble.com/{username}'
codecademy = f'https://www.codecademy.com/{username}'
gravatar = f'https://en.gravatar.com/{username}'
pastebin = f'https://pastebin.com/u/{username}'
foursquare = f'https://foursquare.com/{username}'
roblox = f'https://www.roblox.com/user.aspx?username={username}'
gumroad = f'https://www.gumroad.com/{username}'
newsground = f'https://{username}.newgrounds.com'
wattpad = f'https://www.wattpad.com/user/{username}'
canva = f'https://www.canva.com/{username}'
creative_market = f'https://creativemarket.com/{username}'
trakt = f'https://www.trakt.tv/users/{username}'
five_hundred_px = f'https://500px.com/{username}'
buzzfeed = f'https://buzzfeed.com/{username}'
tripadvisor = f'https://tripadvisor.com/members/{username}'
hubpages = f'https://{username}.hubpages.com'
contently = f'https://{username}.contently.com'
houzz = f'https://houzz.com/user/{username}'
blipfm = f'https://blip.fm/{username}'
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
hackernews = f'https://news.ycombinator.com/user?id={username}'
codementor = f'https://www.codementor.io/{username}'
reverb_nation = f'https://www.reverbnation.com/{username}'
designspiration = f'https://www.designspiration.net/{username}'
bandcamp = f'https://www.bandcamp.com/{username}'
colourlovers = f'https://www.colourlovers.com/love/{username}'
ifttt = f'https://www.ifttt.com/p/{username}'
ebay = f'https://www.ebay.com/usr/{username}'
slack = f'https://{username}.slack.com'
okcupid = f'https://www.okcupid.com/profile/{username}'
trip = f'https://www.trip.skyscanner.com/user/{username}'
ello = f'https://ello.co/{username}'
tracky = f'https://tracky.com/user/~{username}'
basecamp = f'https://{username}.basecamphq.com/login'

def banner():
    print(f"""
    \t\t\t\t             ██████  ██ ▄█▀▄▄▄     ▄▄▄█████▓
    \t\t\t\t           ▒██    ▒  ██▄█▒▒████▄   ▓  ██▒ ▓▒
    \t\t\t\t           ░ ▓██▄   ▓███▄░▒██  ▀█▄ ▒ ▓██░ ▒░
    \t\t\t\t             ▒   ██▒▓██ █▄░██▄▄▄▄██░ ▓██▓ ░ 
    \t\t\t\t           ▒██████▒▒▒██▒ █▄▓█   ▓██▒ ▒██▒ ░ 
    \t\t\t\t           ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒▒▒   ▓▒█░ ▒ ░░   
    \t\t\t\t           ░ ░▒  ░ ░░ ░▒ ▒░ ▒   ▒▒ ░   ░    
    \t\t\t\t           ░  ░  ░  ░ ░░ ░  ░   ▒    ░      
    \t\t\t\t                 ░  ░  ░        ░  ░        
    \t\t\t\t                                  
    \t\t\t\t  
    \t\t\t\t                     by pancake
    \t\t\t\t
    \t\t\t\t            https://github.com/kl3ssydra                \n\n\n\n""")


web = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
]

def search():
    print(f'[+] searching for username : {username}')
    time.sleep(0.5)
    print('------------')
    time.sleep(0.5)
    print('------------\n')
    time.sleep(0.5)

    print(f'[+] SKAT v0.5 is working\n')
    time.sleep(0.5)
    print('------------')
    time.sleep(0.5)
    print('------------\n')
    time.sleep(0.5)

    time.sleep(1)

    count = 0
    match = True
    for url in web:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                print(f'[+] found matches')
                match = False
            print(f'\n[-] link : {url} \n[-] status : {r.status_code}')
            if username in r.text:
                print(f'[PM] Username:{username} - text has been detected in url.')
            else:
                print(f'[PM] Username:{username} - text has not been detected in url, could be a false positive.')#
        count += 1

    total = len(web)
    print(f'a total of {count} matches found out of {total} websites.')



if __name__=='__main__':
    banner()
    search()