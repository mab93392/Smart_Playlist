import numpy as np
import matplotlib.pyplot as plt
from track_data import track_data
from spot_auth import spot_auth

class data_vis:
    def __init__(self):
        # listing value names allows for easier chart labeling
        self.stat_names = ['track_id','danceability','energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
        self.seed_track = '7tFiyTwD0nx5a1eklYtX2J' # hard coded only until robust input system developed
        self.token = spot_auth()
        


    
    def hist(self):
        data = track_data(self.token,self.seed_track)
        plt.figure(figsize=(8,8))
        plt.suptitle('Data for Bohemian Rhapsody')
        for i in range(0,np.shape(data)[1]):
            plt.subplot(len(self.stat_names),1,i+1)
            plt.title('%s'% self.stat_names[i+1],fontsize=12)
            plt.hist(data[:][:,i],50)

        plt.subplots_adjust(top=.85)
        plt.subplots_adjust(bottom=.05)
        plt.subplots_adjust(hspace=1.75)
        
        plt.show()   

vis = data_vis()

vis.hist()