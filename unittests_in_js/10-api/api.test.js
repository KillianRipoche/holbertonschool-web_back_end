const request = require('request');
const { expect } = require('chai');

describe('API integration test', () => {
  const baseUrl = 'http://localhost:7865';

  describe('Index page', () => {
    it('should return correct status code', (done) => {
      request.get(baseUrl, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });

    it('should return correct message', (done) => {
      request.get(baseUrl, (error, response, body) => {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });

  describe('Cart page', () => {
    it('should return correct status code when :id is a number', (done) => {
      request.get(`${baseUrl}/cart/12`, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });

    it('should return correct message when :id is a number', (done) => {
      request.get(`${baseUrl}/cart/12`, (error, response, body) => {
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });

    it('should return 404 when :id is NOT a number', (done) => {
      request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('Available payments', () => {
    it('should return correct status code', (done) => {
      request.get(`${baseUrl}/available_payments`, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });

    it('should return correct payment methods object', (done) => {
      request.get(`${baseUrl}/available_payments`, (error, response, body) => {
        const expected = {
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        };
        expect(JSON.parse(body)).to.deep.equal(expected);
        done();
      });
    });

    it('should have application/json content-type', (done) => {
      request.get(`${baseUrl}/available_payments`, (error, response, body) => {
        expect(response.headers['content-type']).to.include('application/json');
        done();
      });
    });

    it('should return an object with payment_methods property', (done) => {
      request.get(`${baseUrl}/available_payments`, (error, response, body) => {
        const data = JSON.parse(body);
        expect(data).to.have.property('payment_methods');
        done();
      });
    });

    it('should have credit_cards set to true', (done) => {
      request.get(`${baseUrl}/available_payments`, (error, response, body) => {
        const data = JSON.parse(body);
        expect(data.payment_methods.credit_cards).to.be.true;
        done();
      });
    });

    it('should have paypal set to false', (done) => {
      request.get(`${baseUrl}/available_payments`, (error, response, body) => {
        const data = JSON.parse(body);
        expect(data.payment_methods.paypal).to.be.false;
        done();
      });
    });
  });

  describe('Login', () => {
    it('should return correct status code', (done) => {
      request.post({
        url: `${baseUrl}/login`,
        json: { userName: 'Betty' }
      }, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });

    it('should return welcome message with username', (done) => {
      request.post({
        url: `${baseUrl}/login`,
        json: { userName: 'Betty' }
      }, (error, response, body) => {
        expect(body).to.equal('Welcome Betty');
        done();
      });
    });

    it('should work with different usernames', (done) => {
      request.post({
        url: `${baseUrl}/login`,
        json: { userName: 'John' }
      }, (error, response, body) => {
        expect(body).to.equal('Welcome John');
        done();
      });
    });

    it('should have text/html content-type', (done) => {
      request.post({
        url: `${baseUrl}/login`,
        json: { userName: 'Betty' }
      }, (error, response, body) => {
        expect(response.headers['content-type']).to.include('text/html');
        done();
      });
    });
  });
});
