import React from "react";
import "../styles/Modal.css";

const Modal = ({ isOpen, onClose, onFileSelect }) => {
  if (!isOpen) return null; // If modal is not open, don't render anything

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    onFileSelect(selectedFile);
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2 style={{ color: "black" }}>Upload Your File</h2>
        <p style={{ color: "black" }} className="para">
          Please select a Video file. It'll Summairaizes a long videos to short
        </p>

        {/* File input */}
        <input type="file" onChange={handleFileChange} />

        {/* Modal buttons */}
        <div className="modal-buttons">
          <button className="cancel-button" onClick={onClose}>
            Cancel
          </button>
          <button className="upload-button" onClick={onClose}>
            Upload
          </button>
        </div>
      </div>
    </div>
  );
};

export default Modal;
