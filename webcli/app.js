const express = require('express');
const app = express();
const router = express.Router();

const path = __dirname + '/2pmj/';
const port = 8080;

router.use(function (req,res,next) {
  console.log('/' + req.method);
  next();
});

app.use('/2pmj', express.static(path));
app.use('/', router);
app.get('/settings', function(req, res)){
    res.json({hosturl:"http://localhost/tpmj"});
}
app.listen(port, function () {
  console.log('Example app listening on port 8080!')
})
