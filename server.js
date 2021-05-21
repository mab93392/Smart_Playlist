// script that actually runs the server

// imports needed modules
const express = require('express')
const {spawn} = require('child_process')
const app = express()
const bodyParser = require('body-parser');
const ids = require('./auth_main.js')

// tells server to use public folder
app.use(express.static('public'))


// renders homepage
app.get('/', (req,res) => {
    res.sendFile(__dirname + '/index.html')
})
// renders authorization page
app.get('/auth', (req,res) => {
    res.sendFile(__dirname + '/auth.html')
})
// redirects to user auth on Spotify's website
app.get('/auth_script', (req,res) => {
    // redirect url
    const redirecturl = 'http://127.0.0.1:5500/auth'

    // beginning of auth url
    var url = 'https://accounts.spotify.com/authorize'
   
    // establishes authorization scopes
    var scopes = 'ugc-image-upload user-read-recently-played user-read-playback-state '
    scopes += 'user-top-read app-remote-control playlist-modify-public '
    scopes += 'user-modify-playback-state playlist-modify-private user-follow-modify '
    scopes += 'user-read-currently-playing user-follow-read user-library-modify '
    scopes += 'user-read-private user-library-read playlist-read-collaborative' 
    
    // continuing url
    url += '?response_type=code' 
    url += '&client_id=' + ids.client
    url += '&scope=' + scopes
    url += '&redirect_uri=' + encodeURI(redirecturl)

    res.redirect(url)

})



// listens 
app.listen(5500, () => {
    console.log('listening')
})