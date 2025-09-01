const express = require('express');
const router = require('./routes/index.js');

const app = express;

app.use('/', router);

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
