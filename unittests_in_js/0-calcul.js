/**
 * Arrondit deux nombres et retourne leur somme
 * @param {number} a - Premier nombre
 * @param {number} b - Deuxième nombre
 * @returns {number} La somme des nombres arrondis
 */

function calculteNumber(a, b) {
  return Math.round(a) + Math.round(b);
}

module.exports = calculteNumber;
