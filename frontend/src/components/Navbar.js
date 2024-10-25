import React from 'react';
import { NavLink } from 'react-router-dom'; // Use NavLink for active link styling
import '../styles/Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">Summ-Array</div>
      <ul className="navbar-menu">
        <li><NavLink to="/" activeClassName="active" className="nav-link">Home</NavLink></li>
        <li><NavLink to="/about" activeClassName="active" className="nav-link">About</NavLink></li>
        <li><NavLink to="/contact" activeClassName="active" className="nav-link">Contact</NavLink></li>
        <li><button className="login-btn">Login</button></li>
      </ul>
    </nav>
  );
};

export default Navbar;
