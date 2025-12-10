const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  it('should stub Utils.calculateNumber to return 10 and verify console.log', function() {
    // Créer un stub qui retourne toujours 10
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Créer un spy sur console.log
    const consoleSpy = sinon.spy(console, 'log');

    // Appeler la fonction à tester
    sendPaymentRequestToApi(100, 20);

    // Vérifier que le stub a été appelé avec les bons arguments
    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;

    // Vérifier que console.log a été appelé avec le bon message
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;

    // Restaurer le stub et le spy
    stub.restore();
    consoleSpy.restore();
  });

  it('should always return 10 regardless of input', function() {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    // Test avec des valeurs différentes
    sendPaymentRequestToApi(200, 50);

    // Le stub retourne toujours 10, peu importe les arguments
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    consoleSpy.restore();
  });
});
