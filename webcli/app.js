const express = require('express');
const app = express();
const router = express.Router();

const path = __dirname + '/2pmj/';
const port = 80;

router.use(function (req,res,next) {
  console.log('/' + req.method);
  next();
});

app.use('/2pmj', express.static(path));
app.use('/', router);
app.get('/settings', function(req, res){
    res.json({hosturl:"http://localhost:8080/tpmj"});
});
app.listen(port, function () {
  console.log('Example app listening on port 80!')
})
