let testFolder = './data';
let fs = require('fs');

fs.readdir(testFolder, function(error, filelist) {
    console.log(filelist);
});
