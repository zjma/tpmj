var assert = require('assert');
import * as Game2Utils from '../src/game2.js';

describe('Array', function() {
  describe('#indexOf()', function() {
    it('should return -1 when the value is not present', function() {
      assert.equal([1, 2, 3].indexOf(4), -1);
    });
  });
});

describe('Game2Utils', function(){
    it('should return 1 when the area is Oppo', function(){
        assert.equal(Game2Utils.getRoleFromArea('Oppo'), 1);
    })
})
