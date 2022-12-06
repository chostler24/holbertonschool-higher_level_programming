#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, reponse, body) => {
  if (err) throw err;
  fs.writeFile(filePath, body, 'UTF-8', (err) => {
    if (err) throw err;
  });
});
