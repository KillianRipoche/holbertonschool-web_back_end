const express = require('express');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/html');
  res.send('Hello Holberton School!');
});

// Démarrer le serveur
app.listen(port);

module.exports = app;
