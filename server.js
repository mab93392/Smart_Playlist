const http = require('http')
const route = require('./route.js')

http.createServer(route.handleRequest).listen(5500)

