import React, { useState } from 'react';
import '../styles/Contact.css'; // Ensure you create this CSS file for styling

const Contact = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent the default form submission
    setIsSubmitted(true); // Set submitted state to true

    // Reset form fields
    setName('');
    setEmail('');
    setMessage('');
  };

  return (
    <div className="contact-page">
      <h1>Contact Us</h1>
      <form onSubmit={handleSubmit} className="contact-form">
        <input 
          type="text" 
          placeholder="Your Name" 
          value={name} 
          onChange={(e) => setName(e.target.value)} 
          required 
        />
        <input 
          type="email" 
          placeholder="Your Email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
          required 
        />
        <textarea 
          placeholder="Your Message" 
          value={message} 
          onChange={(e) => setMessage(e.target.value)} 
          required 
        ></textarea>
        <button type="submit" className="submit-button">Submit</button>
      </form>

      {isSubmitted && (
        <div className="popup">
          <div className="popup-content">
            <h2>Submitted!</h2>
            <p>Your message has been sent successfully.</p>
            <button onClick={() => setIsSubmitted(false)} className="close-button">Close</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Contact;
