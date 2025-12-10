const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should return a successful response when success is true', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done(); // CRUCIAL : Indiquer que le test asynchrone est terminé
      })
      .catch((error) => {
        done(error); // En cas d'erreur, passer l'erreur à done
      });
  });

  it('should do nothing when success is false', function(done) {
    const result = getPaymentTokenFromAPI(false);

    // Vérifier que la fonction ne retourne rien (undefined)
    expect(result).to.be.undefined;

    done(); // Appeler done car c'est un test asynchrone
  });
});
