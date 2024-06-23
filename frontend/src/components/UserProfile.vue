<template>
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
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'UserProfile',
  data() {
    return {
      user: null,
      posts: [],
      error: null
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'authToken'])
  },
  methods: {
    async fetchUserPosts() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/user/posts', {
          headers: {
            Authorization: `Bearer ${this.authToken}`
          }
        });
        this.posts = response.data.posts;
        console.log('Fetched posts:', this.posts);
      } catch (error) {
        console.error('Error fetching posts:', error);
        this.error = 'Failed to fetch posts. Please try again later.';
      }
    }
  },
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
};
</script>

<style scoped>
.user-profile {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.error {
  color: red;
}
</style>
