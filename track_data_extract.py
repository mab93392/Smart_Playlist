import numpy as np
import requests
import json

def track_data_exctract(token,song_id):

    # establishes request header
    header = {
        "Authorization": "Bearer " + token
    }

    # actually extracts data
    sng_data_ep = 'https://api.spotify.com/v1/audio-features/%s' % song_id
    sng_data_req = requests.get(sng_data_ep,headers=header).content
    sng_data_resp = json.loads(sng_data_req)
    
    #  pulls the seperate audio features
    d = sng_data_resp['danceability'] 
    en = sng_data_resp['energy']
    ld = sng_data_resp['loudness']
    spch = sng_data_resp['speechiness']
    act = sng_data_resp['acousticness']
    inst = sng_data_resp['instrumentalness']
    lv = sng_data_resp['liveness']
    val = sng_data_resp['valence']
    tmp = sng_data_resp['tempo']

    feature_set = [d,en,ld,spch,act,inst,lv,val,tmp]

    return feature_set