/* Load the HTTP library */
  var http = require("http");

  /* Create an HTTP server to handle responses */

  http.createServer(function(request, response) {
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.write("Hello world");
    response.end();
  }).listen(8082);