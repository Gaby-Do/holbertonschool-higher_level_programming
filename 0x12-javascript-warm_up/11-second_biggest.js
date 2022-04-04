#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log('0');
} else {
  const myArray = [];
  for (let i = 2; argv[i]; i++) {
    myArray.push(parseInt(argv[i]));
  }
  const sorted = myArray.sort(function (a, b) { return b - a; });
  console.log(sorted[1]);
}
