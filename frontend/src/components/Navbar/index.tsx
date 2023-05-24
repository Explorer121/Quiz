import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return(
    <div className="nav" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-around' }}>
      <Link to="/"><h1>Home</h1></Link>
      <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
      <Link to="/login">Login</Link>
      <Link to="/register">Register</Link>
      </div>
    </div>
  )
}

export default Navbar;
