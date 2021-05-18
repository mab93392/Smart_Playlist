// routing module

const fs = require('fs')
const url = require('url')
// creates server
function renderHTML(path,res){
    res.writeHead(200, {'Content-Type' : 'text/html'})
    fs.readFile(path, null, function(error,data){
        if (error){
            res.writeHead('404')
            res.write('File not found')
            
        }
        else{
            res.write(data)
            
        }
        res.end()
    })
}
module.exports = {
    handleRequest: function(req,res){
        res.writeHead(200,{'Content-Type': 'text/html'})

        var path = url.parse(req.url).pathname
        switch(path){
            case '/':
                renderHTML('./index.html',res)
                break
            case '/auth':
                renderHTML('./auth.html',res)
                break
            default:
                res.writeHead(404)
                res.write('file not found')
                res.end()
        }
    }
  
}



