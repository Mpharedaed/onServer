<template>
  <div class="create-post">
    <h2>Create a New Post</h2>
    <form @submit.prevent="createPost">
      <div class="form-group">
        <label for="content">Content</label>
        <textarea id="content" v-model="postData.content" required placeholder="Enter your post content..."></textarea>
      </div>
      <div class="form-group">
        <label for="tags">Tags (comma separated)</label>
        <input type="text" id="tags" v-model="postData.tags" placeholder="e.g., tech, news, design"/>
      </div>
      <div class="form-group">
        <label for="image_url">Image URL</label>
        <input type="url" id="image_url" v-model="postData.image_url" placeholder="https://example.com/image.jpg"/>
      </div>
      <div class="form-group checkbox-group">
        <label for="is_pinned">
          <input type="checkbox" id="is_pinned" v-model="postData.is_pinned"/>
          Pin this post
        </label>
      </div>
      <button type="submit">Create Post</button>
    </form>
    <div v-if="message" class="message">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      postData: {
        content: '',
        tags: '',
        image_url: '',
        is_pinned: false,
      },
      message: '',
    };
  },
  methods: {
    async createPost() {
      this.message = '';
      try {
        const token = localStorage.getItem('token'); // Assume JWT token is stored in localStorage
        const payload = {
          content: this.postData.content,
          tags: this.postData.tags.split(',').map(tag => tag.trim()), // Convert tags to an array
          image_url: this.postData.image_url,
          is_pinned: this.postData.is_pinned
        };
        console.log('Payload:', JSON.stringify(payload, null, 2)); // Log the payload
        const response = await axios.post('http://127.0.0.1:5000/api/posts', payload, {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
        });
        console.log('Response:', response); // Log the response
        this.message = 'Post created successfully!';
        // Clear the form
        this.postData = {
          content: '',
          tags: '',
          image_url: '',
          is_pinned: false,
        };
      } catch (error) {
        console.error('Error:', error); // Log the error
        if (error.response) {
          this.message = error.response.data.error;
        } else {
          this.message = 'An error occurred. Please try again.';
        }
      }
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

.create-post {
  max-width: 600px;
  margin: 0 auto;
  padding: 30px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}

h2 {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: 700;
  color: #333333;
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #555555;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #cccccc;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 16px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #007bff;
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.25);
}

.form-group textarea {
  height: 120px;
  resize: vertical;
}

.checkbox-group {
  display: flex;
  align-items: center;
}

.checkbox-group label {
  margin: 0;
  font-weight: normal;
  color: #555555;
}

.checkbox-group input {
  margin-right: 10px;
}

button {
  display: block;
  width: 100%;
  padding: 14px;
  background: linear-gradient(90deg, #007bff, #0056b3);
  color: #ffffff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: background-color 0.3s, transform 0.2s;
  text-align: center;
}

button:hover {
  background: linear-gradient(90deg, #0056b3, #007bff);
  transform: translateY(-2px);
}

button:active {
  transform: translateY(0);
}

.message {
  margin-top: 20px;
  padding: 10px;
  background: #e6ffe6;
  color: #2d862d;
  border: 1px solid #b3ffb3;
  border-radius: 4px;
  text-align: center;
}

/* Responsive Design */
@media (max-width: 600px) {
  .create-post {
    padding: 20px;
  }

  button {
    padding: 12px;
    font-size: 14px;
  }
}

/* Accessibility Enhancements */
.create-post {
  font-size: 16px;
  line-height: 1.5;
}

.form-group input,
.form-group textarea {
  font-size: 16px;
}

button {
  font-size: 16px;
}

h2 {
  font-size: 1.5rem;
}

.form-group label {
  font-size: 1rem;
}
</style>
