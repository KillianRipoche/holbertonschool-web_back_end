const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  describe('type == "SUM"', function() {
    it('should return 6 when inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 0 when inputs are 0.1 and 0.3', function() {
      expect(calculateNumber('SUM', 0.1, 0.3)).to.equal(0);
    });

    it('should return -2 when inputs are -1.4 and -0.5', function() {
      expect(calculateNumber('SUM', -1.4, -0.5)).to.equal(-1);
    });

    it('should handle negative rounding correctly', function() {
      expect(calculateNumber('SUM', -1.6, -0.4)).to.equal(-2);
    });

    it('should return correct sum for large numbers', function() {
      expect(calculateNumber('SUM', 100.4, 200.5)).to.equal(301);
    });
  });

  describe('type == "SUBTRACT"', function() {
    it('should return -4 when inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 0 when both inputs round to same value', function() {
      expect(calculateNumber('SUBTRACT', 2.4, 2.3)).to.equal(0);
    });

    it('should return positive when a > b', function() {
      expect(calculateNumber('SUBTRACT', 5.5, 2.3)).to.equal(4);
    });

    it('should handle negative numbers', function() {
      expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
    });

    it('should handle mixed positive and negative', function() {
      expect(calculateNumber('SUBTRACT', 1.4, -4.5)).to.equal(5);
    });
  });

  describe('type == "DIVIDE"', function() {
    it('should return 0.2 when inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when b rounds to 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return "Error" when b is 0.4 (rounds to 0)', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');
    });

    it('should return "Error" when b is -0.4 (rounds to 0)', function() {
      expect(calculateNumber('DIVIDE', 1.4, -0.4)).to.equal('Error');
    });

    it('should return 2.5 when inputs are 4.5 and 2.4', function() {
      expect(calculateNumber('DIVIDE', 4.5, 2.4)).to.equal(2.5);
    });

    it('should handle negative division', function() {
      expect(calculateNumber('DIVIDE', -5.5, 2.4)).to.equal(-3);
    });

    it('should return 1 when both values are equal', function() {
      expect(calculateNumber('DIVIDE', 4.5, 4.5)).to.equal(1);
    });

    it('should handle division resulting in fraction', function() {
      expect(calculateNumber('DIVIDE', 1.5, 4.5)).to.equal(0.4);
    });
  });
});
