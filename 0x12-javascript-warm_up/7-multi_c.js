#!/usr/bin/node
const { argv } = require('process');

if (parseInt(argv[2])) {
  for (let x = 0; x < parseInt(argv[2]); x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
