# Smart_Playlist
What is this?

    It is a playlist generation service that takes user input in the form of a seed track and finds tracks 
    with similar acoustic features.

How does it work?

    It uses Spotify's API to extract audio features of the seed track. From there, it finds songs from related 
    artists and extracts their audio features. It then employs a gaussian mixture model to determine if the tracks 
    are similar to the seed track. If they are, then they are added to a playlist.

Status:

    Playlist generating software is currently operational. I am currently working on the front end aspects of 
    development to make to user input more fluid. After this, my collaborator Jacob Sides will take over for the 
    web development aspects. Future plans include an expansion of the available services, i.e. more playlist creation
    options.
