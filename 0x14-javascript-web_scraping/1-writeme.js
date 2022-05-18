#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
fs.writeFile(argv[2], argv[3], 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  }
});
