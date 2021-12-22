import requests
import numpy as np
import json
from spot_auth import spot_auth
from client_id import client_id
from client_secret_id import client_secret_id
from unique_ind import unique_ind
from track_data_extract import track_data_exctract
class track_data():

    def __init__(self):
        self.token = spot_auth()
        self.header = header = {
                "Authorization": "Bearer " + self.token
            }


        def get_seed_artist(self, song_id):
            
            art_url = 'https://api.spotify.com/v1/tracks/%s' % song_id
            art_id_req = requests.get(art_url,headers= self.header).content
            artist_resp = json.loads(art_id_req)
            art_id = artist_resp['album']['artists'][0]['id']
            

            return art_id


        def similar_artists(self, artist):
            # pulls related artist info
            related_url = 'https://api.spotify.com/v1/artists/%s/related-artists' % artist
            rlt_req = requests.get(related_url, headers= self.header).content
            rlt_resp = json.loads(rlt_req)

            art_list = np.array(artist)
            for i in range(0,len(rlt_resp['artists'])):
                art_list = np.append(art_list,rlt_resp['artists'][i]['id'])

            return art_list

        def get_albums(self, artist):
            # gets albums made by artists
            album_url = 'https://api.spotify.com/v1/artists/%s/albums' % artist
            album_id_req = requests.get(album_url,headers=self.header).content
            album_resp = json.loads(album_id_req)


            for alb in album_resp['items']:
                album_list = np.append(album_list,alb['id'])



            return album_list

        def track_list(self, album_list):
            track_list = []

            # cycles through album list
            for album in album_list:
                tracks_url = 'https://api.spotify.com/v1/albums/%s/tracks' % album
                track_req = requests.get(tracks_url, headers= self.header).content
                track_resp = json.loads(track_req)
            
            for track_ids in track_resp['items']:
                
                track_list = np.append(track_list,track_ids['id'])
        

        return track_list
    # def track_data(token,song_id): # retreives id of artist of song of interest 
    #     # establishes header
    #     header = {
    #         "Authorization": "Bearer " + token
    #     }
        
    #     # gets artist from track
    #     artist_ep = 'https://api.spotify.com/v1/tracks/%s' % song_id
    #     art_id_req = requests.get(artist_ep,headers=header).content
    #     artist_resp = json.loads(art_id_req)
    #     art_id = artist_resp['album']['artists'][0]['id']
    #     art_list = np.array(art_id)

    #     # gets similar artists
    #     rlt_ep = 'https://api.spotify.com/v1/artists/%s/related-artists' % art_id
    #     rlt_req = requests.get(rlt_ep, headers=header).content
    #     rlt_resp = json.loads(rlt_req)

    #     for i in range(0,len(rlt_resp['artists'])):
    #         art_list = np.append(art_list,rlt_resp['artists'][i]['id'])
        
    #     album_list = []
    #     for ids in art_list:
            
    #         # gets albums made by artists
    #         album_ep = 'https://api.spotify.com/v1/artists/%s/albums' % ids
    #         album_id_req = requests.get(album_ep,headers=header).content
    #         album_resp = json.loads(album_id_req)

    #         for alb in album_resp['items']:
    #             album_list = np.append(album_list,alb['id'])

    #     track_list = []
    #     alb_inds = unique_ind(len(album_list),len(album_list))
    #     # for alb_id in album_list:
    #     for i in range(0,len(album_list)):
    #         album_ind = int(alb_inds[i])
    #         # gets track ids for an album
    #         tracks_ep = 'https://api.spotify.com/v1/albums/%s/tracks' % album_list[album_ind]
    #         track_req = requests.get(tracks_ep, headers=header).content
    #         track_resp = json.loads(track_req)
            
    #         for track_ids in track_resp['items']:
                
    #             track_list = np.append(track_list,track_ids['id'])

    #     ind = unique_ind(100,len(track_list))
    #     for j in range(0,100):
    #         track = int(ind[j])
        
    #         feature_set = track_data_exctract(token,track_list[track])
            
    #         if j == 0:
    #             feature_list = feature_set
    #             id_list = track_list[track]
    #         else:
    #             feature_list = np.vstack((feature_list,feature_set))
    #             id_list = np.append(id_list,track_list[track])
        
    #     return [feature_list,id_list]


