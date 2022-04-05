#!/usr/bin/node
exports.converter = function (base) {
  return function funcDos (nro) {
    return nro.toString(base);
  };
};
