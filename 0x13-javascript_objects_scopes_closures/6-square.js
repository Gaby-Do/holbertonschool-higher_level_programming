#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.width; x++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    } else {
      for (let x = 0; x < this.width; x++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write('X');
        }
        console.log('');
      }
    }
  }
}
module.exports = Square;
