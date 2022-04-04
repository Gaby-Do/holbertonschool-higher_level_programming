#!/usr/bin/node
const { argv } = require('process');

if (parseInt(argv[2])) {
  for (let x = 0; x < parseInt(argv[2]); x++) {
    for (let y = 0; y < parseInt(argv[2]); y++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
