const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

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

  it('should have correct content-type', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });

  it('should respond without errors', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(error).to.be.null;
      done();
    });
  });

  it('should return a string', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.be.a('string');
      done();
    });
  });

  it('should not be empty', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body.length).to.be.greaterThan(0);
      done();
    });
  });
});
