import numpy as np
# list of songs to be used to get a generalized idea of
# the track data distrobutions. Songs will not be hard coded 
# when communication with player is established and software is 
# in its final form

def song_list():
    song_ids = ['2grjqo0Frpf2okIBiifQKs', 
            '7tFiyTwD0nx5a1eklYtX2J',   
            '2eDdFHgqNJltzlvlZFVDWd',   
            '6WqNv8uhWOgg7u3D71MKRu',   
            '2hwOoMtWPtTSSn6WHV7Vp5',   
            '2JSUHbuYs7K5YkFSMmngQt',   
            '0k664IuFwVP557Gnx7RhIl'] 
    song_names = ['September', 
                 'Bohemian Rhapsody', 
                 'Over the Hills and Far Away',
                 'Astral Weeks',
                 'Blue World',
                 'Mahler V Movement I',
                 'Juice']
    
    # puts name and track data into desired output format
    song_ids = np.reshape(song_ids,(len(song_ids),1))
    song_names = np.reshape(song_names,(len(song_names),1))

    
    return np.append(song_ids,song_names,1)









