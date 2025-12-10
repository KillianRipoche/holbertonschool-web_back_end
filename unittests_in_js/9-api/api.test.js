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

    it('should return 404 when :id contains letters', (done) => {
      request.get(`${baseUrl}/cart/abc123`, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });

    it('should return 404 when :id is a float', (done) => {
      request.get(`${baseUrl}/cart/12.5`, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });

    it('should work with large numbers', (done) => {
      request.get(`${baseUrl}/cart/999999`, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 999999');
        done();
      });
    });

    it('should work with single digit', (done) => {
      request.get(`${baseUrl}/cart/5`, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 5');
        done();
      });
    });

    it('should return 404 for negative numbers', (done) => {
      request.get(`${baseUrl}/cart/-12`, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});
