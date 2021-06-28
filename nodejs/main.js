// 1. Use strict
// added in ES 5
// use this for Valin Javascript

'use strict'

// 2. Variable
// let (added in ES6)
let globalName = 'global javascript'
{
    let name = 'java script';
    console.log(name);
    name = 'omg';
    console.log(name);
    console.log(globalName);
}
// console.log(name);
console.log(globalName);

// Constants
const max = 1024
console.log(max)

// 4. Variable type
const count = 17;
const size = 17.1;
console.log(`value:${count}, type: ${typeof count}`);
