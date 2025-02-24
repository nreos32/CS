import express from "express";
import upload from "../middleware/multer.js"

const router = express.Router();

router.post("/single", upload.single("file"), (req, res) => {
  console.log("Uploaded File:", req.file);

  if (!req.file) {
    return res.status(400).json({ error: "No file uploaded" });
  }

  res.json({
    message: "Image uploaded successfully",
    filePath: `/uploads/${req.file.filename}`,
  });
});

router.post("/multiple", upload.array("files", 10), (req, res) => {
  console.log("Uploaded Files:", req.files);

  if (!req.files || req.files.length === 0) {
    return res.status(400).json({ error: "No files uploaded" });
  }

  const uploadedFiles = req.files.map(file => ({
    filename: file.filename,
    path: `/uploads/${file.filename}`
  }));

  res.json({
    message: "Images uploaded successfully",
    files: uploadedFiles
  });
});

export default router;
