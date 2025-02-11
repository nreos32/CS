import express from "express";
import fs from "fs";
import path from "path";
import _ from "lodash";
import { fileURLToPath } from "url"; // for file path

const router = express.Router();

// grab the current directory to this file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const upload_directory = path.join(__dirname, "../uploads");

router.get("/multiple", (req, res) => {
  let files_array = fs.readdirSync(upload_directory);
  if (files_array.length == 0) {
    return res.status(503).send({
      message: "No images",
    });
  }
  
  return res.json(files_array); 
});

router.get("/single", (req, res) => {
  let files_array = fs.readdirSync(upload_directory);
  if (files_array.length == 0) {
    return res.status(503).send({
      message: "No images",
    });
  }

  let filename = _.sample(files_array);  // Get one random file using _.sample instead of _.sampleSize
  return res.sendFile(path.join(upload_directory, filename));
});

// helper function for multiple 
router.get("/file/:filename", (req, res) => {
  return res.sendFile(path.join(__dirname, "../uploads", req.params.filename));
});


export default router;
