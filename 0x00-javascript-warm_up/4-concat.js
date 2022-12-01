#!/usr/bin/node
const myvar = ' is ';
if (process.argv[3]) {
  console.log(process.argv[2] + myvar + process.argv[3]);
} else if (process.argv[2]) {
  console.log(process.argv[2] + myvar + 'undefined');
} else {
  console.log('undefined' + myvar + 'undefined');
}
