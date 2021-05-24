// script that actually runs the server

// imports needed modules
const express = require('express')
const {spawn} = require('child_process')
const app = express()
const bodyParser = require('body-parser');
const ids = require('./clients.js')


// // tells server to use public folder
// app.use(express.static('public'))

const users = [
   {'code': 'AQDMGNShWIdN7Llx11jwYosgiXqQ1fyXN82GrulG6dsT-AYosX1_q1nh5GCE15E3n_S-5C-KFh53hSdRfsvgNpoLxnPWBwgJsJzTxHcpPkhKpN-1mT7RM15JKVfMGOmelHHh5-t3NKMVu5-nQsJXGxvbJqNvhDcXDi26ybzhYSJjuyByXlXkCiltOnFVhauKU3PMMPXTB0YTkF12yRYXmdMcptKhL_-trxzXxrAVTIOBR6svxVCkqBiYsdi-sLTrq6dT5UyWda2N-J4m6u6XfhN_Ju9mNX9EriEBWSwCfO41wi3kiGBbA72ftmhbUVi4eSOAYdil_Id08wT4OcwI6tovJ3U_NXSCgTRpKfeOvSKvgoKEsuTddLY6NdKDhJifSG8UmlVXN18VSgPfYUZjUG3yIvewh6nS_BpZVRKwnWlBcUPmnbHHW6Dw21fzqoXHnZAvKJLHeUzD-2T1DwPYDm-UjsrQQiSRrC-WQjjDoK4EkfV7IIcZGKf64yJDN2oCz632C3_jj-eoUNUYMSMl3IjKOJkCS5SrEozch0F2f4cxCydKCFpYiHRh9d39VIpXSl8h1-1w3J9bt2T-OoKy8J_kXT7Yux_Alcj7-MSjHmj2ObwX',
   'id': 'mbush-12'},
]

// user endpoint
app.get('/users', (req,res) => {
    res.json(users)
})

// endpoint for specific user
app.get('/users/:id', (req,res) => {
    const {id} = req.params
    const queried_user = users.find((user) => 
        user.id === id
    )
    res.json(queried_user)
})

    

// renders homepage
app.get('/', (req,res) => {
    res.sendFile(__dirname + '/index.html')
})
// renders playlist page
app.get('/playlist', (req,res) => {
    res.sendFile(__dirname + '/playlist.html')
})
// renders authorization page
app.get('/auth', (req,res) => {
    res.sendFile(__dirname + '/auth.html')
})
// redirects to user auth on Spotify's website
app.get('/auth_script', (req,res) => {
    // redirect url
    const redirecturl = 'http://127.0.0.1:5500/playlist'

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