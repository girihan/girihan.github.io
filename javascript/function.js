function printHello() {
    console.log('hello');
}

printHello();

function printMessage(message){
    console.log(message);
}

printMessage('hello javascript');


const simplePrint = () => console.log('simplePrint');

const add = (a, b) => {
    return a+b; 
}

simplePrint();
console.log(add(3,4));