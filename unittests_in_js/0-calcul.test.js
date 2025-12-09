const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {

  describe('cas basiques', function() {
    it('devrait retourner 4 quand on passe (1, 3)', function() {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('devrait retourner 5 quand on passe (1, 3.7)', function() {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });

    it('devrait retourner 5 quand on passe (1.2, 3.7)', function() {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('devrait retourner 6 quand on passe (1.5, 3.7)', function() {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });

  describe('arrondissement de a', function() {
    it('devrait arrondir a vers le bas quand .1 <= décimale < .5', function() {
      assert.strictEqual(calculateNumber(1.1, 0), 1);
      assert.strictEqual(calculateNumber(1.2, 0), 1);
      assert.strictEqual(calculateNumber(1.3, 0), 1);
      assert.strictEqual(calculateNumber(1.4, 0), 1);
    });

    it('devrait arrondir a vers le haut quand décimale >= .5', function() {
      assert.strictEqual(calculateNumber(1.5, 0), 2);
      assert.strictEqual(calculateNumber(1.6, 0), 2);
      assert.strictEqual(calculateNumber(1.9, 0), 2);
    });
  });

  describe('arrondissement de b', function() {
    it('devrait arrondir b vers le bas quand .1 <= décimale < .5', function() {
      assert.strictEqual(calculateNumber(0, 2.1), 2);
      assert.strictEqual(calculateNumber(0, 2.2), 2);
      assert.strictEqual(calculateNumber(0, 2.4), 2);
    });

    it('devrait arrondir b vers le haut quand décimale >= .5', function() {
      assert.strictEqual(calculateNumber(0, 2.5), 3);
      assert.strictEqual(calculateNumber(0, 2.7), 3);
      assert.strictEqual(calculateNumber(0, 2.9), 3);
    });
  });

  describe('arrondissement des deux nombres', function() {
    it('devrait arrondir a et b avant de les additionner', function() {
      assert.strictEqual(calculateNumber(1.4, 2.4), 3);
      assert.strictEqual(calculateNumber(1.5, 2.5), 5);
      assert.strictEqual(calculateNumber(2.6, 2.6), 6);
    });
  });

  describe('nombres négatifs', function() {
    it('devrait gérer les nombres négatifs', function() {
      assert.strictEqual(calculateNumber(-1.4, -2.4), -3);
      assert.strictEqual(calculateNumber(-1.5, 2.5), 2);
      assert.strictEqual(calculateNumber(1.5, -2.5), 0);
    });

    it('devrait arrondir -1.5 vers -1', function() {
      assert.strictEqual(calculateNumber(-1.5, 0), -1);
    });
  });

  describe('cas extrêmes', function() {
    it('devrait gérer les zéros', function() {
      assert.strictEqual(calculateNumber(0, 0), 0);
      assert.strictEqual(calculateNumber(0.4, 0.4), 0);
    });

    it('devrait gérer les très grands nombres', function() {
      assert.strictEqual(calculateNumber(1000000.4, 2000000.6), 3000001);
    });

    it('devrait gérer les très petits décimaux', function() {
      assert.strictEqual(calculateNumber(0.1, 0.2), 0);
      assert.strictEqual(calculateNumber(0.4, 0.4), 0);
      assert.strictEqual(calculateNumber(0.5, 0.5), 2);
    });
  });
});
