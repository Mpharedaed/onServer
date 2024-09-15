// src/services/userService.js
import axios from 'axios';

export const getPotentialFriends = async () => {
  return axios.get('https://blogi-36jo.onrender.com/api/potential_friends', {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    },
  });
};

export const sendFriendRequest = async (userId) => {
  return axios.post('https://blogi-36jo.onrender.com/api/friendship/add', { user2_id: userId }, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    },
  });
};
