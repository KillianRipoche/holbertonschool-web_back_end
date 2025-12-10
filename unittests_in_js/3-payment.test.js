const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with type SUM and correct arguments', function() {
    // Créer un spy sur la méthode calculateNumber de Utils
    const spy = sinon.spy(Utils, 'calculateNumber');

    // Appeler la fonction à tester
    sendPaymentRequestToApi(100, 20);

    // Vérifier que le spy a été appelé une fois
    expect(spy.calledOnce).to.be.true;

    // Vérifier que le spy a été appelé avec les bons arguments
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    // Restaurer le spy pour éviter les effets de bord
    spy.restore();
  });

  it('should call Utils.calculateNumber exactly once', function() {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    // Vérifier que la fonction a été appelée exactement une fois
    expect(spy.callCount).to.equal(1);

    spy.restore();
  });

  it('should call Utils.calculateNumber with correct first argument', function() {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    // Vérifier que le premier argument est 'SUM'
    expect(spy.args[0][0]).to.equal('SUM');
    // Vérifier que le deuxième argument est 100
    expect(spy.args[0][1]).to.equal(100);
    // Vérifier que le troisième argument est 20
    expect(spy.args[0][2]).to.equal(20);

    spy.restore();
  });
});
