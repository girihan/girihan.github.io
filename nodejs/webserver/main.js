let http = require('http');
const fs = require('fs');
let url = require('url');

function templeteHTML(title, list, body) {
  return `
  <!doctype html>
  <html>
  <head>
    <title>WEB1 - ${title}</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1><a href="/">WEB</a></h1>
    ${list}
    <a href="/create">create</a>
    <p>
      <input type="text" name="test">
    </P>
    <p>
      <textarea id="desc" name="description"></textarea>
    </p>
    <p>
      <input type="submit" name="submit"/> 
    </p>
    ${body}
  </body>
  </html>
  `;
}

function templeteList(filelist) {
  let list = '<ul>'
  let i = 0;
  while(i < filelist.length) {
    list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`
    i = i + 1
  }
  list = list + '</ul>'

  return list;
}


let app = http.createServer(function(request,response){
  let _url = request.url;
  let queryData = url.parse(_url, true).query;
  let pathname = url.parse(_url, true).pathname;
  let title = queryData.id;

  console.log('pathname=' , pathname);
  if(pathname === '/') {
    if(queryData.id === undefined) {
      fs.readdir('./data', function(error, filelist){
        title = 'Welcome';
        description = 'Hello, Node.js'
        
        let list = templeteList(filelist);
        let template = templeteHTML(title, list, `<h2>${title}</h2>${description}`);
        
        response.writeHead(200);
        response.end(template);
      });
    } else {
      fs.readdir('./data', function(error, filelist){
        fs.readFile(`data/${queryData.id}`, 'utf8', function(err, description){
          let list = templeteList(filelist);
          let template = templeteHTML(title, list, `<h2>${title}</h2>${description}`);
          response.writeHead(200);
          response.end(template);
        });
      });
    }
  } else if (pathname === '/create') { 
    fs.readdir('./data', function(error, filelist){
      fs.readFile(`data/${queryData.id}`, 'utf8', function(err, description){
        let list = templeteList(filelist);
        let template = templeteHTML(title, list, `<h2>${title}</h2>${description}`);
        response.writeHead(200);
        response.end(template);
      });
    });
  } else {
    response.writeHead(404);
    response.end('Not found');
  }
});
app.listen(3000);