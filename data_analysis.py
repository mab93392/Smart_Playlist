import numpy as np
import matplotlib.pyplot as plt
from track_data import track_data
from spot_auth import spot_auth
from song_list import song_list
from sklearn.mixture import GaussianMixture 

class data_analysis:
    def __init__(self):
        # listing value names allows for easier chart labeling
        self.stat_names = ['danceability','energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
        self.seed_track = song_list()
        self.token = spot_auth()
        


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
    def GMM(self,trait_num):
        features = track_data(self.token,self.seed_track[4,0])
        means = []
        vars = []

        
        data = features[:,trait_num].reshape(-1,1)
        # this block optimizes the number of components 
        n_comps = 10 # starts with 10 components
        gm_1 = GaussianMixture(n_components = n_comps,random_state=0).fit(data)
        gm_2 = GaussianMixture(n_components = n_comps + 1, random_state = 0).fit(data)
        print('gm_1 bic: %s' % gm_1.aic(data))
        print('gm_2 bic: %s' % gm_2.aic(data))

        if gm_2.aic(data) > gm_1.aic(data):
            while gm_2.bic(data) > gm_1.bic(data) and n_comps > 1:
                gm_2 = gm_1
                n_comps = n_comps - 1
                gm_1 = GaussianMixture(n_components = n_comps, random_state = 0).fit(data)
                print('gm_1 bic: %s' % gm_1.aic(data))
                print('gm_2 bic: %s' % gm_2.aic(data))
        else: 
            while gm_2.aic(data) < gm_1.aic(data):
                gm_1 = gm_2
                n_comps = n_comps + 1
                gm_2 = GaussianMixture(n_components = n_comps, random_state = 0).fit(data)
                print('gm_1 bic: %s' % gm_1.aic(data))
                print('gm_2 bic: %s' % gm_2.aic(data))

        # block that constructs the final analysis of data set
        gm_out = GaussianMixture(n_components = n_comps, random_state = 0).fit(data)


        for j in range(0,n_comps):
            means = np.append(means,gm_out.means_[j])
            vars = np.append(vars,gm_out.covariances_[j])

           
                       
        
        

        return [means,vars]


    
        




