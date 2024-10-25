import React, { useState } from 'react';
import '../styles/HomePage.css';
import Modal from './Modal.js';
import Lottie from 'lottie-react'; // Import Lottie for animations
import animationData from '../animations/animation.json'; // Import your JSON animation file

const HomePage = ({ darkTheme }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleUploadClick = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  const handleFileSelect = (file) => {
    if (file) {
      console.log(`File selected: ${file.name}`);
    }
  };

  return (
    <div className={`home-page ${darkTheme ? 'dark' : ''}`}>
      <div className="home-page-content">
        <h1>Welcome to the page that summarizes long videos to short</h1>
        <button className="primary-button" onClick={handleUploadClick}>
          Upload Video File
        </button>
        <button className="primary-button" style={{ margin: '10px' }} onClick={handleUploadClick}>
          Upload Audio File
        </button>
        
        <Modal 
          isOpen={isModalOpen} 
          onClose={handleCloseModal} 
          onFileSelect={handleFileSelect} 
        />
      </div>

      <div className="home-page-animation">
        <Lottie 
          animationData={animationData} 
          loop={true} 
          className="animated-lottie" 
        />
      </div>
    </div>
  );
};

export default HomePage;
