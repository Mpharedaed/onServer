<template>
<<<<<<< HEAD
  <div class="post-container">
    <h2 class="post-title">My Posts</h2>
    <ul class="post-list">
      <li v-for="post in posts" :key="post.id" class="post-item">
        <div class="post-header" v-if="post.user">
          <img :src="post.user.avatar || 'default-avatar.png'" alt="User Avatar" class="avatar">
          <div class="user-info">
            <h3 class="username">{{ post.user.name || 'Anonymous' }}</h3>
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
=======
  <div class="user-profile">
    <h2 v-if="user">{{ user.username }}'s Profile</h2>
    <div v-if="error">
      <p class="error">{{ error }}</p>
    </div>
    <div v-else-if="posts.length">
      <h3>Your Posts</h3>
      <ul>
        <li v-for="post in posts" :key="post.id">
          <h4>{{ post.content }}</h4>
          <p>{{ post.created_at }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>You have no posts.</p>
    </div>
>>>>>>> 3dc7672530d1e5be219899818d8b5f38eb11f174
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
    };
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/user/posts', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        });
        this.posts = response.data.posts;
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    },
    async likePost(post) {
      try {
        await axios.post(`http://127.0.0.1:5000/api/user/posts/${post.id}/like`, {}, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        });
        post.likes += 1;
      } catch (error) {
        console.error('Error liking post:', error);
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    },
  },
<<<<<<< HEAD
=======
  created() {
    if (this.isAuthenticated) {
      this.user = this.$store.getters.getUser;
      if (this.user) {
        console.log('User data:', this.user);
        this.fetchUserPosts();
      } else {
        this.error = 'User data not found.';
      }
    } else {
      this.error = 'You need to be logged in to view this page.';
    }
  }
>>>>>>> 3dc7672530d1e5be219899818d8b5f38eb11f174
};
</script>

<style scoped>
.post-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background: #f0f2f5;
  border-radius: 10px;
}

.post-title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
  color: #444;
}

.post-list {
  list-style-type: none;
  padding: 0;
}

.post-item {
  background: #fff;
  padding: 15px;
  margin-bottom: 20px;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  border: 1px solid #e1e4e8;
}

.post-header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.user-info {
  flex-grow: 1;
}

.username {
  margin: 0;
  font-size: 14px;
  font-weight: bold;
}

.post-date {
  margin: 0;
  font-size: 12px;
  color: #888;
}

.post-content {
  font-size: 14px;
  margin-bottom: 10px;
  color: #333;
}

.post-actions {
  display: flex;
  align-items: center;
  border-top: 1px solid #e1e4e8;
  padding-top: 10px;
  margin-top: 10px;
}

.like-button,
.comment-button,
.share-button {
  background: none;
  border: none;
  color: #007bff;
  cursor: pointer;
  font-size: 14px;
  margin-right: 10px;
}

.like-button:hover,
.comment-button:hover,
.share-button:hover {
  text-decoration: underline;
}

.like-count {
  font-size: 14px;
  color: #555;
}

.comment-section {
  border-top: 1px solid #e1e4e8;
  padding-top: 10px;
  margin-top: 10px;
}

.comment-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #e1e4e8;
  border-radius: 20px;
  background: #f0f2f5;
}

.no-posts {
  text-align: center;
  font-size: 18px;
  color: #777;
}
</style>
