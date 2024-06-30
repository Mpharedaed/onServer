<template>
    <div class="potential-friends-container">
      <h2 class="section-title">Find New Friends</h2>
      <ul class="potential-friends-list">
        <li v-for="user in potentialFriends" :key="user.id" class="potential-friend-item">
          <img :src="user.avatar || 'default-avatar.png'" alt="User Avatar" class="avatar-small">
          <div class="user-info">
            <h3 class="username">{{ user.name }}</h3>
            <button @click="sendFriendRequest(user.id)" class="add-friend-button">Add Friend</button>
          </div>
        </li>
      </ul>
      <div v-if="error" class="error-message">{{ error }}</div>
      <div v-if="loading" class="loading-message">Loading...</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'PotentialFriends',
    data() {
      return {
        potentialFriends: [],
        error: null,
        loading: true,
      };
    },
    created() {
      this.fetchPotentialFriends();
    },
    methods: {
      async fetchPotentialFriends() {
        try {
          const token = localStorage.getItem('token');
          const response = await axios.get('http://127.0.0.1:5000/api/potential_friends', {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          this.potentialFriends = response.data.potential_friends;
        } catch (error) {
          console.error('Error fetching potential friends:', error);
          this.error = 'Failed to fetch potential friends.';
        } finally {
          this.loading = false;
        }
      },
      async sendFriendRequest(userId) {
        try {
          const token = localStorage.getItem('token');
          await axios.post(`http://127.0.0.1:5000/api/add`, { user2_id: userId }, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          alert('Friend request sent successfully!');
          this.potentialFriends = this.potentialFriends.filter(user => user.id !== userId);
        } catch (error) {
          console.error('Error sending friend request:', error);
          alert('Failed to send friend request.');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .potential-friends-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background: #f0f2f5;
    border-radius: 10px;
  }
  
  .section-title {
    font-size: 22px;
    margin-bottom: 10px;
    text-align: center;
  }
  
  .potential-friends-list {
    list-style-type: none;
    padding: 0;
  }
  
  .potential-friend-item {
    background: #fff;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
  }
  
  .avatar-small {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .user-info {
    flex-grow: 1;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .username {
    font-size: 16px;
    color: #333;
  }
  
  .add-friend-button {
    padding: 10px 20px;
    border: none;
    background: #007bff;
    color: #fff;
    cursor: pointer;
    border-radius: 20px;
    font-size: 14px;
  }
  
  .add-friend-button:hover {
    background: #0056b3;
  }
  
  .error-message {
    color: red;
    text-align: center;
  }
  
  .loading-message {
    text-align: center;
  }
  </style>
  