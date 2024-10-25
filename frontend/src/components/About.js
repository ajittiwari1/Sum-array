import React from 'react';
import '../styles/AboutUs.css'; // Ensure you create this CSS file for styling

const AboutUs = () => {
  const teamMembers = [
    { name: 'Ajit Tiwari', college: 'TCET', role: 'FrontEnd Lead' },
    { name: 'Aryan Singh', college: 'DJ Sanghvi', role: 'Backend Lead' },
    { name: 'Ajinkya Thoke', college: 'VCET', role: 'Database & Frontend' },
  ];

  return (
    <div className="about-us">
      <h1>About Us</h1>
      <p>
        We are a team of passionate individuals dedicated to harnessing the power of artificial intelligence
        to create innovative solutions. Our project focuses on summarizing lengthy video and audio content,
        making it easier for users to digest information quickly and efficiently. With a user-friendly interface,
        our tool aims to enhance productivity and understanding, whether for educational purposes, content creation, 
        or personal use.
      </p>

      <div className="team-cards">
        {teamMembers.map((member, index) => (
          <div className="team-card" key={index}>
            <h3>{member.name}</h3>
            <p>{member.college}</p>
            <p>{member.role}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AboutUs;
