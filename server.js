// script that actually runs the server

// imports needed modules
const express = require('express')
const app = express()

// tells server to use public folder
app.use(express.static('public'))

// renders html
app.get('/', (req,res) => {
    res.sendFile(__dirname + '/index.html')
})
app.get('/auth', (req,res) => {
    res.sendFile(__dirname + '/public/auth.html')
})

// listens 
app.listen(5500, () => {
    console.log('listening')
})