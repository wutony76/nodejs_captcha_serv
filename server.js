var express = require('express'),
    app = express(),
    port = process.env.PORT || 30000,
    bodyParser = require('body-parser');
var cors = require('cors');
var routes = require('./api/routes/todoListRoutes');

app.use(cors())
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
routes(app);

app.get('/parse', cors(), function (req, res, next) {
  res.json({msg: 'This is CORS-enabled for a Single Route'})
})
app.listen(port);

console.log('server is run: ' + port);