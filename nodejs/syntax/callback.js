// function a() {
//     console.log('A');
// }

var a = function() {
    console.log('A');
}

function slowfuncc(callback) {
    callback();
}

slowfuncc(a);