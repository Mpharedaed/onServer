<!-- src/components/ResetPassword.vue -->
<template>
  <div class="reset-password">
    <h1>Reset Password</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="new-password">New Password</label>
        <input type="password" id="new-password" v-model="newPassword" required>
      </div>
      <button type="submit">Reset Password</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newPassword: '',
      message: ''
    };
  },
  methods: {
    async submitForm() {
      this.message = '';
      const token = this.$route.params.token;
      try {
        const response = await axios.post(`http://127.0.0.1:5000/api/reset-password/${token}`, { new_password: this.newPassword });
        this.message = response.data.message;
      } catch (error) {
        this.message = error.response ? error.response.data.message : 'An error occurred. Please try again.';
      }
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
