import express from 'express';
import * as TpmjUtils from 'common';

var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.json(TpmjUtils.Obj);
});

export default router;
