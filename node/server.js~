const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');


http.createServer((req, res) => {
	if (req.url === "/") {
		fs.readFile("./Public/Index.html", "UTF-8", (err, body) => {
			res.writeHead(200, {"Content-Type": "text/html"});
			res.end(body);
		});
	} else if(req.url.match("/sysinfo")) {
		myHostName = os.hostname();
		html = `
		<!DOCTYPE html>
		<html>
			<head>
				<title>Node JS Response</title>
			</head>
			<body>
				<p>Hostname: ${myHostName}</p>
				<p>IP: ${ip.address()}</p>
				<p>Server Uptime: ${((os.uptime())/86400)} Days</p>
				<p>Total Memory: ${((os.totalmem())/1000000)}mb</p>
				<p>Free Memory: ${((os.freemem())/1000000)}mb</p>
				<p>Number of CPUs: ${(os.cpus().length)}</p>
			</body>
		</html>`
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(html);
	} else {
		res.writeHead(404, {"Contetn-Type": "text/plain"});
		res.end(`404 File Not Found at ${req.url}`);
	}
}).listen(3000);

console.log("Server listening on port 3000")
