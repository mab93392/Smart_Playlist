import numpy as np
import matplotlib.pyplot as plt
from track_data import track_data
from spot_auth import spot_auth
from song_list import song_list
from sklearn.mixture import GaussianMixture 
from track_data_extract import track_data_exctract
from unique_ind import unique_ind
class data_analysis:
    def __init__(self):
        # listing value names allows for easier chart labeling
        self.stat_names = ['danceability','energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
        self.seed_track = song_list()[int(unique_ind(1,len(song_list()[0])))][0]
        self.token = spot_auth()
        self.seed_track_data = track_data_exctract(self.token,self.seed_track)


    # plots histogram of data
    def hist(self): 
        for i in range(0,np.shape(self.seed_track)[0]):
            data = track_data(self.token,self.seed_track[i,0])
            plt.figure(figsize=(6.5,7))
            plt.suptitle('Data for %s' % self.seed_track[i,1])
            for j in range(0,np.shape(data)[1]):
                plt.subplot(len(self.stat_names),1,j+1)
                plt.title('%s'% self.stat_names[j],fontsize=10)
                plt.hist(data[:][:,j],75)

            plt.subplots_adjust(top=.9)
            plt.subplots_adjust(bottom=.05)
            plt.subplots_adjust(hspace=1.75)
            
            plt.show()   

    # performs the actual guassian mixture model analysis
    def GMM(self):
        data_pull = track_data(self.token,self.seed_track)
        data = data_pull[0]
        tracks = data_pull[1]
        means = []
        vars = []

        
        
        # this block optimizes the number of components 
        n_comps = 36 # starts with 36 components
        gm_1 = GaussianMixture(n_components = n_comps,random_state=0).fit(data)
        gm_2 = GaussianMixture(n_components = n_comps + 1, random_state = 0).fit(data)
       

        if gm_2.aic(data) > gm_1.aic(data):
            while gm_2.bic(data) > gm_1.bic(data) and n_comps > 1:
                gm_2 = gm_1
                n_comps = n_comps - 1
                gm_1 = GaussianMixture(n_components = n_comps, random_state = 0).fit(data)

        else: 
            while gm_2.aic(data) < gm_1.aic(data):
                gm_1 = gm_2
                n_comps = n_comps + 1
                gm_2 = GaussianMixture(n_components = n_comps, random_state = 0).fit(data)


        # block that constructs the final analysis of data set
        gm_out = GaussianMixture(n_components = n_comps, random_state = 0).fit(data)


        for i in range(0,n_comps):
    
            vars_i = []

            for j in range(0,len(self.stat_names)):

                for k in range(0,len(self.stat_names)):
                    if k == j:
                        vars_i = np.append(vars_i,gm_out.covariances_[i][j][k])
            
            if i == 0:
                means = gm_out.means_[i]
                vars = vars_i
            else:
                means = np.vstack((means,gm_out.means_[i]))
                vars = np.vstack((vars,vars_i))        

        return [means,vars,n_comps,tracks,data]


    # actually makes the playlists
    def playlist_make(self):
        #  initializes needed variables
        data = self.GMM()
        playlists = {}
        pl_cnt = 0

        for i in range(0,data[2]): #itirates through all the componenents
            
            # determines if seed track fit within ith distribution
            diff = np.subtract(self.seed_track_data,data[0][i])
            score = 0
            for j in range(0,len(diff)):
                if np.abs(diff[j]) > data[1][i][j]:
                    score = score + 1
        
            # determines if the pulled tracks fit within shared distributions with seed track
            if score > 8: 
                pl_cnt = pl_cnt + 1
                playlist_i = self.seed_track
                playlist_name = 'playlist %s' % pl_cnt
                
                for k in range(0,len(data[3])):
                    diff_k = np.subtract(data[4][k],data[0][i])
                    score_k = 0
                    for j in range(0,len(diff)):
                        if np.abs(diff_k[j]) > data[1][i][j]:
                            score_k = score_k + 1
                    if score_k > 8:
                        playlist_i = playlist_i + '%s' % data[3][k] + ', '
                playlists[playlist_name] = playlist_i

        return [playlists,pl_cnt] #pl_cnt = # of playlists
                
        
              




