const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  let consoleSpy;

  // Hook exécuté AVANT chaque test
  beforeEach(function() {
    consoleSpy = sinon.spy(console, 'log');
  });

  // Hook exécuté APRÈS chaque test
  afterEach(function() {
    consoleSpy.restore();
  });

  it('should log "The total is: 120" and be called once for 100 and 20', function() {
    sendPaymentRequestToApi(100, 20);

    // Vérifier le message
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

    // Vérifier qu'il n'a été appelé qu'une seule fois
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it('should log "The total is: 20" and be called once for 10 and 10', function() {
    sendPaymentRequestToApi(10, 10);

    // Vérifier le message
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;

    // Vérifier qu'il n'a été appelé qu'une seule fois
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
