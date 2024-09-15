// src/plugins/axios.js
import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://blogi-36jo.onrender.com',
  headers: {
    'Content-Type': 'application/json'
  }
});        

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default instance;
