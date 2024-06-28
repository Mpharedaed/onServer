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
      <div class="form-group toggle-group">
        <label for="is_anonymous">Post Anonymously</label>
        <label class="lock-toggle">
          <input type="checkbox" id="is_anonymous" v-model="postData.is_anonymous"/>
          <span class="slider round">
            <span class="lock">
              <span class="lock-body"></span>
              <span class="lock-shackle"></span>
            </span>
          </span>
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
        is_anonymous: false, // New property for anonymous post
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
          is_pinned: this.postData.is_pinned,
          is_anonymous: this.postData.is_anonymous // Include anonymous option in payload
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
          is_anonymous: false,
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
.create-post {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background: #f0f2f5;
  border-radius: 10px;
}

.form-group {
  margin-bottom: 15px;
}

.checkbox-group {
  display: flex;
  align-items: center;
}

.toggle-group {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.lock-toggle {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.lock-toggle input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: 0.4s;
  border-radius: 34px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: 0.4s;
  border-radius: 50%;
}

.lock {
  position: relative;
  display: inline-block;
  width: 26px;
  height: 26px;
  background-color: white;
  border-radius: 50%;
  transition: 0.4s;
  top: 4px;
}

.lock-body {
  position: absolute;
  width: 14px;
  height: 14px;
  background-color: white;
  border-radius: 3px;
  top: 6px;
  left: 6px;
  transition: 0.4s;
}

.lock-shackle {
  position: absolute;
  width: 10px;
  height: 10px;
  border: 3px solid white;
  border-bottom: none;
  border-radius: 50%;
  top: -8px;
  left: 8px;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:checked + .slider:before {
  transform: translateX(26px);
}

input:checked + .slider .lock {
  background-color: #2196F3;
  transform: translateX(26px);
}

input:checked + .slider .lock .lock-body {
  background-color: #2196F3;
}

input:checked + .slider .lock .lock-shackle {
  border-color: #2196F3;
}


</style>
