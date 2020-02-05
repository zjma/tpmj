const express = require('express');
const app = express();
const router = express.Router();

const path = __dirname + '/assets/';
const port = 8081;

router.use(function (req,res,next) {
  console.log('/' + req.method);
  next();
});

app.use('/assets', express.static(path));
app.use('/', router);

app.listen(port, function () {
  console.log('Example app listening on port 8081!')
})
