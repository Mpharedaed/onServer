<template>
  <div class="verify-page">
    <div v-if="message" class="message">{{ message }}</div>
  </div>
</template>

<script>
import axiosInstance from '@/plugins/axios';  // Import the configured Axios instance

export default {
  name: 'EmailVerify',
  data() {
    return {
      message: ''
    };
  },
  async created() {
    const token = this.$route.params.token;
    try {
      const response = await axiosInstance.get(`/verify/${token}`);
      this.message = response.data.message;
    } catch (error) {
      this.message = error.response ? error.response.data.message : 'An error occurred. Please try again.';
    }
  }
};
</script>

<style scoped>
.verify-page {
  /* Styles for your verify page */
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-size: 1.2em;
}
.message {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
