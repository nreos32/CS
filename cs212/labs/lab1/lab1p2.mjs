import http from 'http';
import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';

dotenv.config();
const app = http.createServer((req, res) => {
        if (req.url === '/') {
            let webpage = fs.readFileSync("homepage.html");
            res.end(webpage)
        }
        else if (req.url === '/about') {
            let webpage = fs.readFileSync("aboutme.html");
            res.end(webpage)}
        
        else if (req.url === '/login') {
            let webpage = fs.readFileSync("login.html");
            res.end(webpage)}
        
        else if (req.url === '/register') {
            let webpage = fs.readFileSync("register.html");
            res.end(webpage)}

        else {
            res.end("Page Not Found")
        }
    });
const PORT = process.env.PORT || 8000;

app.listen(PORT, () => {
    console.log(`http://localhost:${PORT}`);
});