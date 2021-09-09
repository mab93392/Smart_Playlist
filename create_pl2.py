# the script that actually takes input from web app and publishes 
# playlist to spotify
from create_playlist import playlist
from data_analysis import data_analysis
import json
import requests
from client_id import client_id
from client_secret_id import client_secret_id
import sys
import time
import numpy as np


class smart_playlist:
    # inits variables
    def __init__(self): 
        self.id = sys.argv[1]
        self.url = 'http://127.0.0.1:5500/users/' + self.id 
        req = requests.get(self.url).json()
        self.user = req
        self.playlist = []
        self.pl_name = ''
        self.pl_id = ''
        
    
    # gets token if one is not already in the user's data i.e they're new
    def token_request(self):
        # communicates w/ Spotify API
        url = 'https://accounts.spotify.com/api/token'

        body = {
        "grant_type": "authorization_code",
        "code": self.user['user']['code'],
        "redirect_uri": 'http://127.0.0.1:5500/register',
        "client_id": client_id(),
        "code_verifier" : self.user['user']['code_verifier'],
        "client_secret" : client_secret_id()
        }

        req = requests.post(url,data = body).json()

        # # extracts relevant data from response &  updates
        # # the user data 
        self.user['user']['tokens']['current'] = req['access_token']
        self.user['user']['tokens']['refresh'] = req['refresh_token']
        self.user['user']['tokens']['grant_time'] = time.time()

        # # communicates w/Smart Playlist API
        self.json_update(self.user['user']['tokens']['grant_time'],self.user['user']['tokens']['current'],self.user['user']['tokens']['refresh'])

        # # updates user variable
        req = requests.get(self.url).json()
        self.user = req

    #  updates Smart Playlist API
    def json_update(self,gt,cr,rf):
        url = 'http://127.0.0.1:5500/update/%s/%s/%s/%s' % (self.id,gt,cr,rf)
        req = requests.put(url)
        
    def refresh_token(self):
        url = 'https://accounts.spotify.com/api/token'
        enc = client_id() + ':' + client_secret_id()
    
        body = {
        "grant_type" : "refresh_token",
        "refresh_token": self.user['user']['tokens']['refresh'],
        "client_id": client_id(),
        "client_secret": client_secret_id()
        }

        req = requests.post(url,data= body).json()
        print(req)
        # extracts relevant data from response &  updates
        # the user data 
        self.user['user']['tokens']['current'] = req['access_token']
        # # self.user['user']['tokens']['refresh'] = req['refresh_token']
        self.user['user']['tokens']['grant_time'] = time.time()

        # # communicates w/Smart Playlist API
        self.json_update(self.user['user']['tokens']['grant_time'],self.user['user']['tokens']['current'],self.user['user']['tokens']['refresh'])

        #updates user variable
        req = requests.get(self.url).json()
        self.user = req
        print('ran: %s' % time.time())
        
    def make_playlist(self):
        header = {
            "Authorization" : "Bearer " + self.user['user']['tokens']['current']
        }

        # gets current song
        song_url = 'https://api.spotify.com/v1/me/player/currently-playing' 
        song_req = requests.get(song_url, headers= header).json()

        seed_track = song_req['item']['id']
        self.pl_name = song_req['item']['name']
        
        

        # # makes playlist
        # Da = data_analysis()
        # self.playlist = Da.playlist_make(seed_track)
        # print(self.playlist[0]['playlist 1'])
        
        # posts playlist
        post_url = 'https://api.spotify.com/v1/users/%s/playlists' % self.user['user']['id']
        post_header = {
            "Authorization" : "Bearer " + self.user['user']['tokens']['current']
        }
        post_body = {
            "name" : self.pl_name
        }
        req = requests.post(post_url, headers= post_header, json= post_body).json()
        print(req['id'])
        print('ran: %s' % time.time())


        
        #populates playlist


        print('ran: %s' % time.time())
sp = smart_playlist()

# sp.refresh_token()
# sp.token_request()
sp.make_playlist()
# sp.get_pl()