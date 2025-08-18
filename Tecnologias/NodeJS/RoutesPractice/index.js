

const  http = require("http");

http.createServer(function (request,response){

    if(request.url in routes){
        return routes[request.url](request,response);
    }

    response.writeHead(404);
    response.end(http.STATUS_CODES[404]);

}).listen(process.env.port || 1337);

var routes = {

    '/': function index (request,response){
         response.writeHead(200);
         response.end("Hello world");
    },
    '/foo': function foo (request,response){
        response.writeHead(200);
        response.end("I am in fooo");
    }
}