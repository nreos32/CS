import { useState } from "react";
import "./App.css";

const App = () => {
  const [singleFile, setSingleFile] = useState(null);
  const [multipleFiles, setMultipleFiles] = useState([]);
  const [displayImage, setDisplayImage] = useState(null);
  const [displayImages, setDisplayImages] = useState([]);
  const [displayDogImage, setDisplayDogImage] = useState(null);
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSingleFileChange = (e) => {
    if (e.target.files.length > 0) {
      const file = e.target.files[0];
      if (!file.type.startsWith('image/')) {
        setMessage("Please select an image file");
        return;
      }
      setSingleFile(file);
    }
  };

  const handleMultipleFileChange = (e) => {
    const files = Array.from(e.target.files);
    const imageFiles = files.filter(file => file.type.startsWith('image/'));
    if (imageFiles.length !== files.length) {
      setMessage("Some files were skipped because they weren't images");
    }
    setMultipleFiles(imageFiles);
  };

  const fetchSingleFile = async () => {
    try {
      setIsLoading(true);
      setMessage("");
      const response = await fetch(`http://localhost:8000/fetch/single`);
      if (!response.ok) {
        throw new Error("Failed to fetch image");
      }
      const blob = await response.blob();
      const imageUrl = URL.createObjectURL(blob);
      setDisplayImage(imageUrl);
    } catch (error) {
      setMessage(`Error fetching single file: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmitSingleFile = async (e) => {
    e.preventDefault();
    if (!singleFile) {
      setMessage("Please select a file before uploading.");
      return;
    }

    try {
      setIsLoading(true);
      const formData = new FormData();
      formData.append("file", singleFile);
      
      const response = await fetch(`http://localhost:8000/save/single`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Image upload failed");
      }
      setMessage("File uploaded successfully!");
      setSingleFile(null); // Reset file input
    } catch (error) {
      setMessage(`Error uploading file: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchMultiple = async () => {
    try {
      setIsLoading(true);
      setMessage("");
      const response = await fetch('http://localhost:8000/fetch/multiple');
      if (!response.ok) {
        throw new Error("Failed to fetch image list");
      }
      const data = await response.json();
      
      if (data.length === 0) {
        setMessage("No images available");
        return;
      }
      
      const filePromises = data.map(async (filename) => {
        const fetchResponse = await fetch(`http://localhost:8000/fetch/file/${filename}`);
        if (!fetchResponse.ok) {
          throw new Error(`Failed to fetch ${filename}`);
        }
        const fileBlob = await fetchResponse.blob();
        return URL.createObjectURL(fileBlob);
      });

      const imageUrls = await Promise.all(filePromises);
      setDisplayImages(imageUrls);
    } catch (error) {
      setMessage(`Error fetching multiple files: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchDogImage = async () => {
    try {
      setIsLoading(true);
      setMessage("");
      const response = await fetch('https://dog.ceo/api/breeds/image/random');
      if (!response.ok) {
        throw new Error("Failed to fetch dog image");
      }
      const data = await response.json();
      setDisplayDogImage(data.message);
    } catch (error) {
      setMessage(`Error fetching dog image: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      {message && <p className={message.includes("Error") ? "error" : "success"}>{message}</p>}
      
      <section>
        <h2>Fetch Single Random Image</h2>
        <button onClick={fetchSingleFile} disabled={isLoading}>
          {isLoading ? "Loading..." : "Fetch Single File"}
        </button>
        {displayImage && (
          <div className="image-container">
            <h3>Single File</h3>
            <img
              src={displayImage}
              alt="Display Image"
              className="display-image"
            />
          </div>
        )}
      </section>

      <section>
        <h2>Upload Single File</h2>
        <form onSubmit={handleSubmitSingleFile}>
          <input 
            type="file" 
            onChange={handleSingleFileChange}
            accept="image/*"
          />
          <button type="submit" disabled={!singleFile || isLoading}>
            {isLoading ? "Uploading..." : "Upload Single File"}
          </button>
        </form>
      </section>

      <section>
        <h2>Multiple Images</h2>
        <button onClick={fetchMultiple} disabled={isLoading}>
          {isLoading ? "Loading..." : "Fetch Multiple Files"}
        </button>
        <div className="images-grid">
          {displayImages.length > 0 ? (
            displayImages.map((imageUrl, index) => (
              <div key={index} className="image-container">
                <img 
                  src={imageUrl} 
                  alt={`Image ${index + 1}`}
                  className="display-image"
                />
              </div>
            ))
          ) : (
            <p>No images to display</p>
          )}
        </div>
      </section>

      <section>
        <h2>Random Dog Image</h2>
        <button onClick={fetchDogImage} disabled={isLoading}>
          {isLoading ? "Loading..." : "Fetch Dog Image"}
        </button>
        {displayDogImage && (
          <div className="image-container">
            <h3>Dog Image</h3>
            <img
              src={displayDogImage}
              alt="Display Dog Image"
              className="display-image"
            />
          </div>
        )}
      </section>
    </div>
  );
};

export default App;