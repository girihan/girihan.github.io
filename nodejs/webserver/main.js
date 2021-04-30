let http = require('http');
const fs = require('fs');
let url = require('url');

let app = http.createServer(function(request,response){
  let _url = request.url;
  let queryData = url.parse(_url, true).query;
  let pathname = url.parse(_url, true).pathname;
  let title = queryData.id;

  console.log(queryData);

  if(pathname === '/') {
    if(queryData.id === undefined) {
      title = 'Welcome';
      description = 'Hello, Node.js'
      var template = `
      <!doctype html>
      <html>
      <head>
        <title>WEB1 - ${title}</title>
        <meta charset="utf-8">
      </head>
      <body>
        <h1><a href="/">WEB</a></h1>
        <ul>
          <li><a href="/?id=html">HTML</a></li>
          <li><a href="/?id=css">CSS</a></li>
          <li><a href="/?id=javascript">JavaScript</a></li>
        </ul>
        <h2>${title}</h2>
        <p>${description}</p>
      </body>
      </html>
      `;
      response.writeHead(200);
      response.end(template);
    } else {
      fs.readFile(`data/${queryData.id}`, 'utf8', function(err, description){
        var template = `
        <!doctype html>
        <html>
        <head>
          <title>WEB1 - ${title}</title>
          <meta charset="utf-8">
        </head>
        <body>
          <h1><a href="/">WEB</a></h1>
          <ul>
            <li><a href="/?id=html">HTML</a></li>
            <li><a href="/?id=css">CSS</a></li>
            <li><a href="/?id=javascript">JavaScript</a></li>
          </ul>
          <h2>${title}</h2>
          <p>${description}</p>
        </body>
        </html>
        `;
        response.writeHead(200);
        response.end(template);
      });
    }
   
  } else {
    response.writeHead(404);
    response.end('Not found');
  }
});
app.listen(3000);