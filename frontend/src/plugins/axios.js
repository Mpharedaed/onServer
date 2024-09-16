// src/plugins/axios.js
import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://blogi-36jo.onrender.com/api/',
  headers: {
    'Content-Type': 'application/json'
  }
});
       

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    console.log('Token found and added to headers:', token); // Add this log to debug
    config.headers.Authorization = `Bearer ${token}`;
  } else {
    console.log('No token found in localStorage');
  }
  return config;
});


export default instance;
