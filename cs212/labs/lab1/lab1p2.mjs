import http from 'http';
import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';

dotenv.config();
const app = http.createServer((req, res) => {
    try {
        if (req.url === '/') {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            let webpage = fs.readFileSync(path.join(process.cwd(), "pages", "homepage.html"));
            res.end(webpage);
        }
        else if (req.url === '/about') {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            let webpage = fs.readFileSync(path.join(process.cwd(), "pages", "aboutme.html"));
            res.end(webpage);
        }
        else if (req.url === '/contact') {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            let webpage = fs.readFileSync(path.join(process.cwd(), "pages", "contact.html"));
            res.end(webpage);
        }
        else {
            res.writeHead(404, { 'Content-Type': 'text/html' });
            let webpage = fs.readFileSync(path.join(process.cwd(), "pages", "404.html"));
            res.end(webpage);
        }
    } catch (error) {
        console.error("Error reading file:", error);
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error');
    }
});

const PORT = process.env.PORT || 8000;

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});