import { BrowserRouter, Routes, Route } from 'react-router-dom'
import React from 'react';
import Navbar from './components/Navbar'
import Home from './components/Home'
import Login from './components/AuthPage/Login'
import Register from './components/AuthPage/Register'
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
