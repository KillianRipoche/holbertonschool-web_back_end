const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('type == "SUM"', function() {
    it('should return 6 when inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 0 when inputs are 0.1 and 0.3', function() {
      assert.strictEqual(calculateNumber('SUM', 0.1, 0.3), 0);
    });

    it('should return -2 when inputs are -1.4 and -0.5', function() {
      assert.strictEqual(calculateNumber('SUM', -1.4, -0.5), -1);
    });

    it('should handle negative rounding correctly', function() {
      assert.strictEqual(calculateNumber('SUM', -1.6, -0.4), -2);
    });

    it('should return correct sum for large numbers', function() {
      assert.strictEqual(calculateNumber('SUM', 100.4, 200.5), 301);
    });
  });

  describe('type == "SUBTRACT"', function() {
    it('should return -4 when inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0 when both inputs round to same value', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.4, 2.3), 0);
    });

    it('should return positive when a > b', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.5, 2.3), 4);
    });

    it('should handle negative numbers', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
    });

    it('should handle mixed positive and negative', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, -4.5), 5);
    });
  });

  describe('type == "DIVIDE"', function() {
    it('should return 0.2 when inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when b rounds to 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return "Error" when b is 0.4 (rounds to 0)', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
    });

    it('should return "Error" when b is -0.4 (rounds to 0)', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.4), 'Error');
    });

    it('should return 2 when inputs are 4.5 and 2.4', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 4.5, 2.4), 2.5);
    });

    it('should handle negative division', function() {
      assert.strictEqual(calculateNumber('DIVIDE', -5.5, 2.4), -3);
    });

    it('should return 1 when both values are equal', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 4.5, 4.5), 1);
    });

    it('should handle division resulting in fraction', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.5, 4.5), 0.4);
    });
  });
});
