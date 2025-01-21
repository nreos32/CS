import http from 'http';
import fs from 'fs';

const app = http.createServer((req, res) => {
    if (req.url === '/') {
        try {
            let webpage = fs.readFileSync("homepage.html", 'utf8');
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.end(webpage);
        } catch (error) {
            res.writeHead(500, {'Content-Type': 'text/html'});
            res.end('<h1>Internal Server Error</h1>');
        }
    } else if (req.url === '/about') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end('<h1>About Page</h1><a href="/">Back to Home</a>');
    } else if (req.url === '/user/account/id') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end("<h1>My name is Nicholas</h1><a href='/'>Back to Home</a>");
    } else {
        res.writeHead(404, {'Content-Type': 'text/html'});
        res.end("<h1>404 - Page not found</h1><a href='/'>Back to Home</a>");
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});