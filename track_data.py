import requests
import numpy as np
import json
from spot_auth import spot_auth
from client_id import client_id
from client_secret_id import client_secret_id
from unique_ind import unique_ind


def track_data(token,song_id): # retreives id of artist of song of interest 
    # establishes header
    header = {
        "Authorization": "Bearer " + token
    }
    
    # gets artist from track
    artist_ep = 'https://api.spotify.com/v1/tracks/%s' % song_id
    art_id_req = requests.get(artist_ep,headers=header).content
    artist_resp = json.loads(art_id_req)
    art_id = artist_resp['album']['artists'][0]['id']
    art_list = np.array(art_id)

    # gets similar artists
    rlt_ep = 'https://api.spotify.com/v1/artists/%s/related-artists' % art_id
    rlt_req = requests.get(rlt_ep, headers=header).content
    rlt_resp = json.loads(rlt_req)

    for i in range(0,len(rlt_resp['artists'])):
        art_list = np.append(art_list,rlt_resp['artists'][i]['id'])
    
    album_list = []
    for ids in art_list:
        
        # gets albums made by artists
        album_ep = 'https://api.spotify.com/v1/artists/%s/albums' % ids
        album_id_req = requests.get(album_ep,headers=header).content
        album_resp = json.loads(album_id_req)

        for alb in album_resp['items']:
            album_list = np.append(album_list,alb['id'])

    track_list = []
    for alb_id in album_list:
        # gets track ids for an album
        tracks_ep = 'https://api.spotify.com/v1/albums/%s/tracks' % alb_id
        track_req = requests.get(tracks_ep, headers=header).content
        track_resp = json.loads(track_req)

        for track_ids in track_resp['items']:
            track_list = np.append(track_list,track_ids['id'])

    ind = unique_ind(1500,len(track_list))
    for j in range(0,1500):
        track = ind[j]
        sng_data_ep = 'https://api.spotify.com/v1/audio-features/%s' % track_list[int(track)]
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

        if j == 0:
            feature_list = feature_set
            id_list = track_list[int(track)]
        else:
            feature_list = np.vstack((feature_list,feature_set))
            id_list = np.append(id_list,track_list[int(track)])
    return feature_list


