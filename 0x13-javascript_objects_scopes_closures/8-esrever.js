#!/usr/bin/node
exports.esrever = function (list) {
  const myArray = [];
  let x = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    myArray[x] = list[i];
    x++;
  }
  return myArray;
};
