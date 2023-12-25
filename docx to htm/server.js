const express = require("express");
const multer = require("multer");
const mammoth = require("mammoth");
const fs = require("fs");
const path = require("path");

const app = express();

// Set up multer for handling file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/"); // Save uploaded files in the 'uploads' directory
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname); // Use original file name
  },
});
const upload = multer({ storage: storage });

// Serve the HTML file
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

// Handle file upload and conversion
app.post("/convert", upload.single("docxFile"), (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }

  const uploadedFilePath = path.join(
    __dirname,
    "uploads",
    req.file.originalname
  );
  const outputDir = path.join(__dirname, "uploads", "docx_files");

  mammoth
    .convertToHtml({ path: uploadedFilePath })
    .then((result) => {
      const html = result.value;

      // Create a subfolder for images
      if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir);
      }

      // Extract images and save them in the 'docx_files' folder
      const images = result.messages.filter(
        (message) => message.type === "image"
      );
      images.forEach((image, index) => {
        const extension = image.contentType.split("/")[1];
        const imageName = `image_${index + 1}.${extension}`;
        const imagePath = path.join(outputDir, imageName);
        fs.writeFileSync(imagePath, image.content);
      });

      // Save the HTML content to a file
      const htmlPath = path.join(outputDir, "converted.html");
      fs.writeFileSync(htmlPath, html);

      res.send("Conversion successful. HTML and images saved.");
    })
    .catch((err) => {
      console.error("Error:", err);
      res.status(500).send("Conversion failed.");
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
