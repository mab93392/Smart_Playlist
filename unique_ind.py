import numpy as np
# generates array of indices that do not repeat
def unique_ind(size,max_index):
    out = [] # intializes output
    uniq = [] # intializes uniquness test value

    # makes array of indices
    for i in range(0,size):
        ind = np.random.randint(size) # generates index

        # tests for uniqueness of index
        for j in range(0,len(out)):
            if ind == out[j]:
                uniq = False
            else:
                uniq = True
        
        # changes index to unique value
        while uniq == False: 
            ind = np.random.randint(max_index)
            for j in range(0,len(out)):
                if ind == out[j]:
                    uniq = False
                else:
                    uniq = True

        out = np.append(out,ind) # builds array
    
    return out

