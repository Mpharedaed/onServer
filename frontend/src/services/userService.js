// src/services/userService.js
import axios from 'axios';

export const getPotentialFriends = async () => {
  return axios.get('http://localhost:5000/api/potential_friends', {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    },
  });
};

export const sendFriendRequest = async (userId) => {
  return axios.post('http://localhost:5000/api/friendship/add', { user2_id: userId }, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    },
  });
};
