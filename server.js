// server that will run 
const http = require('http')
const fs = require('fs')
const port = 5501

// creates server
const server = http.createServer(function(req,resp){
    resp.writeHead(200, {'Content-Type' : 'text/html'})
    fs.readFile('index.html', function(error,data){
        if (error){
            resp.writeHead('404')
            resp.write('File not found')
        }
        else{
            resp.write(data)
        }
    })
})

server.listen(port)

