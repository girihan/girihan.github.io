'use strict';

let globalName = 'global name';
console.log(globalName);

{
    let name = 'sanggil';
    console.log(name);
    name = 'hello';
    console.log(name);
}
// console.name(name);
console.name(globalName);



