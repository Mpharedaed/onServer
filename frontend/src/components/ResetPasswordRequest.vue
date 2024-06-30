<!-- src/components/ResetPasswordRequest.vue -->
<template>
    <div class="reset-password-request">
      <h1>Reset Password</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="email">Email Address</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <button type="submit">Send Reset Link</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        message: ''
      };
    },
    methods: {
      async submitForm() {
        this.message = '';
        try {
          const response = await axios.post('http://127.0.0.1:5000/api/reset-password-request', { email: this.email });
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
  