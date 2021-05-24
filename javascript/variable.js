'use strict';

let name = 'javascript';
console.log(name);
name = 'java';
console.log(name);

console.log('-----------------------');

{
    let name1 = 'java';
    console.log(name1);
    name1 = 'hello';
    console.log(name1);
}


const    maxValue = 5;

const size = 17.1;
console.log(`value: ${size}, type: ${typeof size}`);
const bigInt = 1232143134204238203480572803248032482034n;
console.log(`value: ${bigInt}, type: ${typeof bigInt}`);


const symbol_1 = Symbol('id');
const symbol_2 = Symbol('id');
console.log(symbol_1 === symbol_2);
const symbol_3 = Symbol.for('id');
const symbol_4 = Symbol.for('id');
console.log(symbol_3 === symbol_4);


let text = '8' / '2';
console.log(`value: ${text}, type: ${typeof text}`);

const obj = {name:'javascript', usage:'web'};
console.log(obj);
obj.usage = 'backend';
console.log(obj);









