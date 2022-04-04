#!/usr/bin/node
const { argv } = require('process');

if (!argv[3]) {
  argv[3] = 'undefined';
}
if (!argv[2]) {
  argv[2] = 'undefined';
}
console.log(argv[2] + ' is ' + argv[3]);
