// script that actually runs the server

// imports needed modules
const express = require('express')
const {spawn} = require('child_process')
const app = express()
const bodyParser = require('body-parser');
const ids = require('./clients.js')
const fs = require('fs')

const users_data = fs.readFileSync('users.json', (err) => {
    console.log('could not load data')
})
const users = JSON.parse(users_data)

// user endpoint
app.get('/users', (req,res) => {
    res.send(users)
})


// handles the user specific playlist page
app.get('/users_page/:id', (req,res) => {
    res.sendFile(__dirname + '/playlist.html')
})

// for registration page
app.get('/register', (req,res) => {
    res.sendFile(__dirname + '/register.html')
})

// handles the addition of users to json db
app.get('/add_user/:id/:code', (req,res) => {
    const {id} = req.params
    const {code} = req.params
    console.log(id)
    const queried_user = users.find((user) => 
        user.id === id
    )
    if (queried_user === undefined){
        new_user = {
            'id': id,
            'code': code
        }
        const data = JSON.stringify(new_user)

        fs.writeFile('users.json',data,(err) => {
            if (err) {
                console.log('could not write new user data')
            }
            
            console.log('new user data saved')
        })

        res.redirect('/users_page/' + id)
    }
    else {
        res.redirect('/users_page/' + id)
    }
})


// endpoint for specific user by id
app.get('/users_id/:id', (req,res) => {
    const {id} = req.params
    const queried_user = users.find((user) => 
        user.id === id
    )
    res.json(queried_user)
})

// retrieves user based on code
app.get('/users_code/:code', (req,res) => {
    const {code} = req.params
    const queried_user = users.find((user) => 
        user.code === code
    )
    res.json(queried_user)
})

// redirects to user-specific page
app.get('/submit/:id', (req,res) => {
    const {id} = req.params
    const queried_user = users.find((user) => 
        user.id === id
    )
    
    if (queried_user === undefined){
        res.redirect('/auth')
    }
    else {
        res.redirect('/users_page/' + id)
    }
})   

// runs the playlist creation python software
app.get('/create_playlist/:id/:song_id', (req,res) => {
    const {id} = req.params
    const {song_id} = req.params
    const queried_user = users.find((user) => 
        user.id === id
    )
    const code = queried_user.code
 
    const cp = spawn('python3',['child.py',id,code,song_id])

    cp.stdout.on('data', (data) => {
        console.log(data.toString())
    })

    cp.stderr.on('data', (data) => {
        console.log(`stdout: ${data}`)
    })

    cp.on('close', (code) => {
        console.log(`closed with code: ${code}`)
    })

    res.redirect('/users_page/' + id)
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
    const redirecturl = 'http://127.0.0.1:5500/register'

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

