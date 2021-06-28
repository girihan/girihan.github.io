let number = [ 1, 400, 12, 34, 500, 10000, 32564];

let total = 0;
let i = 0;
while(i < number.length) {
    // console.log(number[i]);
    total = total + number[i];
    i = i + 1;
}
console.log(total);