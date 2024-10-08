<template>
  <div class="profile-container">
    <!-- User Info Section -->
    <div class="user-info-container">
      <img :src="avatarUrl" alt="User Avatar" class="avatar-large">
      <div class="user-details">
        <h1 class="username">{{ user.username || 'Anonymous' }}</h1>
        <p class="user-bio">{{ user.bio || 'No bio available' }}</p>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="profile-nav">
      <button @click="activeTab = 'posts'" :class="{ active: activeTab === 'posts' }">Posts</button>
      <button @click="activeTab = 'friends'" :class="{ active: activeTab === 'friends' }">Friends</button>
      <button @click="activeTab = 'potentialFriends'" :class="{ active: activeTab === 'potentialFriends' }">Potential Friends</button>
      <button @click="activeTab = 'settings'" :class="{ active: activeTab === 'settings' }">Settings</button>
    </div>

    <!-- Posts Section -->
    <div v-if="activeTab === 'posts'" class="posts-container">
      <h2 class="section-title">My Posts</h2>
      <ul class="post-list">
        <li v-for="post in posts" :key="post.id" class="post-item">
          <div class="post-header" v-if="post.user">
            <img :src="post.user.avatar || 'default-avatar.png'" alt="User Avatar" class="avatar">
            <div class="user-info">
              <h3 class="username">{{ post.user.username || 'Anonymous' }}</h3>
              <p class="post-date">{{ formatDate(post.date) }}</p>
            </div>
          </div>
          <div class="post-content">{{ post.content }}</div>
          <div class="post-actions">
            <button @click="likePost(post)" class="like-button">👍 Like</button>
            <span class="like-count">{{ post.likes }} Likes</span>
            <button class="comment-button">💬 Comment</button>
            <button class="share-button">🔗 Share</button>
          </div>
          <div class="comment-section">
            <input type="text" class="comment-input" placeholder="Write a comment..." />
          </div>
        </li>
      </ul>
      <p v-if="posts.length === 0" class="no-posts">You have no posts.</p>
    </div>

    <!-- Friends Section -->
    <div v-if="activeTab === 'friends'" class="friends-container">
      <h2 class="section-title">Friends</h2>
      <ul class="friends-list">
        <li v-for="friend in friends" :key="friend.id" class="friend-item">
          <img :src="friend.avatar || 'default-avatar.png'" alt="Friend Avatar" class="avatar-small">
          <div class="friend-info">
            <h3 class="friend-name">{{ friend.username }}</h3>
          </div>
        </li>
      </ul>
      <p v-if="friends.length === 0" class="no-friends">You have no friends.</p>
    </div>

    <!-- Potential Friends Section -->
    <div v-if="activeTab === 'potentialFriends'" class="potential-friends-container">
      <h2 class="section-title">Potential Friends</h2>
      <ul class="potential-friends-list">
        <li v-for="friend in potentialFriends" :key="friend.id" class="friend-item">
          <img :src="friend.avatar || 'default-avatar.png'" alt="Friend Avatar" class="avatar-small">
          <div class="friend-info">
            <h3 class="friend-name">{{ friend.username }}</h3>
            <button @click="sendFriendRequest(friend.id)" class="add-friend-button">Add Friend</button>
          </div>
        </li>
      </ul>
      <p v-if="potentialFriends.length === 0" class="no-friends">No potential friends found.</p>
    </div>

    <!-- Settings Section -->
    <div v-if="activeTab === 'settings'" class="settings-container">
      <h2 class="section-title">Settings</h2>
      <form @submit.prevent="updateSettings">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="user.username">

        <label for="bio">Bio</label>
        <textarea id="bio" v-model="user.bio"></textarea>

        <label for="avatar">Profile Photo</label>
        <input type="file" id="avatar" @change="onFileChange">

        <button type="submit" class="save-button">Save Changes</button>
      </form>
    </div>

    <!-- Error Message -->
    <div v-if="error" class="error-message">{{ error }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserProfile',
  data() {
    return {
      user: { username: '', bio: '', avatar: '' },
      posts: [],
      friends: [],
      potentialFriends: [],
      selectedFile: null,
      error: null,
      loading: true,
      activeTab: 'posts',
    };
  },
  computed: {
    avatarUrl() {
      return this.user.avatar ? `http://127.0.0.1:5000/uploads/${this.user.avatar}` : 'default-avatar.png';
    }
  },
  created() {
    this.fetchUser();
    this.fetchFriends();
    this.fetchPotentialFriends();
  },
  methods: {
    async fetchUser() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://127.0.0.1:5000/api/profile', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.user = response.data;
        this.posts = response.data.posts;
      } catch (error) {
        console.error('Error fetching user:', error);
        this.error = 'Failed to fetch user.';
      }
    },
    async fetchFriends() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://127.0.0.1:5000/api/friends', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.friends = response.data.friends;
      } catch (error) {
        console.error('Error fetching friends:', error);
        this.error = 'Failed to fetch friends.';
      }
    },
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
    },
    onFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    async updateSettings() {
      try {
        const token = localStorage.getItem('token');
        const formData = new FormData();
        formData.append('username', this.user.username);
        formData.append('bio', this.user.bio);
        if (this.selectedFile) {
          formData.append('avatar', this.selectedFile);
        }

        const response = await axios.put('http://127.0.0.1:5000/api/profile', formData, {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'multipart/form-data',
          },
        });
        this.user = response.data.user;
        alert('Settings updated successfully');
      } catch (error) {
        console.error('Error updating settings:', error);
        this.error = 'Failed to update settings.';
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    }
  }
};
</script>


<style scoped>
.profile-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background: #f0f2f5;
  border-radius: 10px;
}

.user-info-container {
  display: flex;
  align-items: center;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  margin-bottom: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.avatar-large {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-right: 20px;
}

.user-details {
  flex-grow: 1;
}

.username {
  font-size: 24px;
  font-weight: bold;
  margin: 0;
}

.user-bio {
  font-size: 16px;
  color: #666;
}

.profile-nav {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.profile-nav button {
  padding: 10px 20px;
  border: none;
  background: #007bff;
  color: #fff;
  cursor: pointer;
  border-radius: 20px;
  font-size: 16px;
}

.profile-nav button.active {
  background: #0056b3;
}

.section-title {
  font-size: 22px;
  margin-bottom: 10px;
  text-align: center;
}

.posts-container, .friends-container, .potential-friends-container, .settings-container {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.post-list, .friends-list, .potential-friends-list {
  list-style-type: none;
  padding: 0;
}

.post-item, .friend-item {
  background: #f9f9f9;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.post-header, .friend-info {
  display: flex;
  align-items: center;
}

.avatar, .avatar-small {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.post-content, .friend-name {
  font-size: 16px;
  color: #333;
}

.post-actions, .comment-section, .error-message {
  border-top: 1px solid #e1e4e8;
  padding-top: 10px;
  margin-top: 10px;
}

.like-button, .comment-button, .share-button {
  background: none;
  border: none;
  color: #007bff;
  cursor: pointer;
  font-size: 14px;
  margin-right: 10px;
}

.like-button:hover, .comment-button:hover, .share-button:hover {
  text-decoration: underline;
}

.like-count, .no-posts, .no-friends {
  font-size: 14px;
  color: #555;
}

.comment-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #e1e4e8;
  border-radius: 20px;
  background: #f0f2f5;
}

.settings-container label {
  display: block;
  font-size: 14px;
  margin-bottom: 5px;
}

.settings-container input, .settings-container textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #e1e4e8;
  border-radius: 5px;
}

.save-button {
  padding: 10px 20px;
  border: none;
  background: #28a745;
  color: #fff;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
}

.error-message {
  color: #ff4d4d;
  text-align: center;
  font-size: 16px;
}
</style>
