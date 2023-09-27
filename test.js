
var http = require('http');
// http.createServer(function (request, response) {
//     response.writeHead(200, {'Content-Type': 'text/plain'});
//     response.end('Hello World\n');
// }).listen(8888);

const _data = {
  data: 'test'
}
const serv = http.createServer((req, res) => {
  res.statusCode = 200
  // res.setHeader = ('content-Type', 'application/json')
  res.end(JSON.stringify(_data))
})
serv.listen(8888)
console.log('Server running at http://127.0.0.1:8888/');