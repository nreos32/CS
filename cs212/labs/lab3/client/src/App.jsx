import { useState } from "react";

const App = () => {
  // what do we need to track
  // setters for saving
  const [singleFile, setSingleFile] = useState(null);
  const [multipleFiles, setMultipleFiles] = useState([]);

  // getters for displaying
  const [displayImage, setDisplayImage] = useState(null); //DISPLAY 1 IMAGE
  const [displayImages, setDisplayImages] = useState([]); //DISPLAY MULTIPLE IMAGES
  const [displayDogImage, setDisplayDogImage] = useState(null); //DISPLAY DOG IMAGE
  
  const [message, setMessage] = useState("");

  // Handle single file change
  const handleSingleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setSingleFile(e.target.files[0]);
    }
  };

  // Handle multiple file change
  const handleMultipleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setMultipleFiles((prevFiles) => [...prevFiles, ...e.target.files]);
    }
  };

  // fetch functions -> fetch a random single image
  const fetchSingleFile = async () => {
    try {
      const response = await fetch(`http://localhost:8000/fetch/single`);

      const blob = await response.blob(); // we made a blob - Binary Large Object
      // but thats not an image, so we need to make an image element

      // using createObjectURL
      const imageUrl = URL.createObjectURL(blob);
      setDisplayImage(imageUrl);
    } catch (error) {
      console.error("Error fetching single file:", error);
    }
  };

  // fetch functions -> save single
  const handleSubmitSingleFile = async (e) => {
    e.preventDefault();
    if (!singleFile) {
      setMessage("Please select a file before uploading.");
      return;
    }

    try {
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
    } catch (error) {
      console.log("Error:", error);
    }
  };

  // fetch functions -> save multiple
  const handleSubmitMultipleFiles = async (e) => {
    e.preventDefault();
    if (multipleFiles.length === 0) {
      setMessage("Please select files before uploading.");
      return;
    }

    try {
      const formData = new FormData();
      Array.from(multipleFiles).forEach((file) => {
        formData.append("files", file);
      });

      const response = await fetch(`http://localhost:8000/save/multiple`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Image upload failed");
      }
      setMessage("Files uploaded successfully!");
    } catch (error) {
      console.log("Error:", error);
    }
  };

  const fetchMultiple = async () => {
    try {
      const response = await fetch('http://localhost:8000/fetch/multiple');
      const data = await response.json();
      
      const filePromises = data.map(async (filename) => {
        const fetchFilenameData = await fetch(`http://localhost:8000/fetch/file/${filename}`);
        const fileBlob = await fetchFilenameData.blob();
        return URL.createObjectURL(fileBlob);
      });

      const imageUrls = await Promise.all(filePromises);
      setDisplayImages(imageUrls);

    } catch (error) {
      console.log(error)
    }
  };

  const fetchDogImage = async() => {
    try {
      const response = await fetch('https://dog.ceo/api/breeds/image/random');
      const data = await response.json();
      setDisplayDogImage(data.message);
    } catch (error) {
      console.log(error);
    }
  };

  const saveDogImage = async () => {
    if (!displayDogImage) {
      setMessage("Please fetch a dog image first");
      return;
    }

    try {
      const response = await fetch(displayDogImage);
      const blob = await response.blob();
      
      const formData = new FormData();
      formData.append("file", blob, "dog-image.jpg");
      
      const uploadResponse = await fetch(`http://localhost:8000/save/single`, {
        method: "POST",
        body: formData,
      });

      const data = await uploadResponse.json();

      if (!uploadResponse.ok) {
        throw new Error(data.error || "Image upload failed");
      }
      setMessage("Dog image saved successfully!");
    } catch (error) {
      console.error("Error saving dog image:", error);
      setMessage("Failed to save dog image");
    }
  };

  return (
    <div>
      <p>{message}</p>
      <h2>Fetch Single Random Image</h2>
      <button onClick={fetchSingleFile}>Fetch Single File</button>
      {displayImage && (
        <div>
          <h3>Single File</h3>
          <img
            src={displayImage}
            alt="Display Image"
            style={{ width: "100px", marginTop: "5px" }}
          />
        </div>
      )}
      <form onSubmit={handleSubmitSingleFile}>
        <h2>Upload Single File</h2>
        <input type="file" onChange={handleSingleFileChange} />
        <button type="submit">Upload Single File</button>
      </form>

      <h2>Fetch Multiple Files</h2>
      <button onClick={fetchMultiple}>Fetch Multiple Files</button>
      {displayImages.length > 0 ? (
        displayImages.map((image, index) => (
          <div key={index}>
            <img 
              src={image} 
              alt={`Image ${index + 1}`}
              style={{ width: "100px", marginTop: "5px" }}
            />
          </div>
        ))
      ) : (
        <p>No images to display</p>
      )}
      <form onSubmit={handleSubmitMultipleFiles}>
        <h2>Upload Multiple Files</h2>
        <input type="file" multiple onChange={handleMultipleFileChange} />
        <button type="submit">Upload Multiple Files</button>
      </form>

      <h2>Fetch Dog Images</h2>
      <button onClick={fetchDogImage}>Fetch Dog Image</button>
      {displayDogImage && (
        <div>
          <h3>Dog Image</h3>
          <img
            src={displayDogImage}
            alt="Display Dog Image"
            style={{ width: "200px", marginTop: "10px" }}
          />
          <button onClick={saveDogImage}>Save Dog Image</button>
        </div>
      )}
    </div>
  );
};

export default App;