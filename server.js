// script that actually runs the server

// imports needed modules
const express = require('express')
const {spawn} = require('child_process')
const app = express()
const bodyParser = require('body-parser');

// tells server to use public folder
app.use(express.static('public'))


// renders html
app.get('/', (req,res) => {
    res.sendFile(__dirname + '/index.html')
})
app.get('/auth', (req,res) => {
    res.sendFile(__dirname + '/auth.html')
})

app.get('/auth_script', (req,res) => {
    // initializes child process
    const cp = spawn('python',['./jsauth.py'])

    // establishes the standard output
    cp.stdout.on('data', (data) => {
        const ids = JSON.parse(data.toString())
        const client = ids.client
        const secret = ids.secret
        

    })

    // closes child process
    cp.on('close', (code) => {
        console.log(`exited with code ${code}`)
    })
    console.log('works')
    res.send()
})



// listens 
app.listen(5500, () => {
    console.log('listening')
})