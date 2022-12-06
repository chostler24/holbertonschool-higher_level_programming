#!/usr/bin/node
const fs = require('fs');
fs.readFile(
  process.argv[2], 'UTF-8', (err, data) => {
    if (err) throw err;
    console.log(data);
  });
