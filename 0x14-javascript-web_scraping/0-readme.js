#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
fs.readFile(argv[2], 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
