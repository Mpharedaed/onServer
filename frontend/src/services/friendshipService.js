// src/services/friendshipService.js
import axios from '@/plugins/axios';

export const sendFriendRequest = (user2_id) => {
  return axios.post('/friendship/add', { user2_id });
};

export const acceptFriendRequest = (user2_id) => {
  return axios.post('/friendship/accept', { user2_id });
};

export const blockFriendship = (user2_id) => {
  return axios.post('/friendship/block', { user2_id });
};

export const deleteFriendship = (user2_id) => {
  return axios.post('/friendship/delete', { user2_id });
};

export const addInteraction = (user2_id) => {
  return axios.post('/friendship/interaction', { user2_id });
};

export const completeQuest = (user2_id) => {
  return axios.post('/friendship/complete_quest', { user2_id });
};

export const revealIdentity = (user2_id) => {
  return axios.post('/friendship/reveal', { user2_id });
};

export const getPotentialFriends = () => {
  return axios.get('/friendship/potential-friends');
};