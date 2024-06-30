<template>
  <div class="login-page">
    <div class="login-container">
      <div class="image-section">
        <div class="overlay">
          <h2>Welcome Back</h2>
          <p>Please login to continue.</p>
        </div>
      </div>
      <div class="form-section">
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required>
          </div>
          <button type="submit" class="login-button">Login</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        <p v-if="errorMessage === 'Email not verified. Please check your email to verify your account.'">
          Didn't receive an email? <button @click="resendVerificationEmail">Resend Verification Email</button>
        </p>
        <p class="signup-text">Don't have an account? <router-link to="/signup">Sign Up</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from '@/plugins/axios';  // Import the configured Axios instance

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async submitForm() {
      this.errorMessage = '';  // Clear any previous error messages
      try {
        const response = await axiosInstance.post('/login', {
          email: this.username,  // Assuming the backend expects email, change if needed
          password: this.password
        });

        if (response.data.token) {
          localStorage.setItem('token', response.data.token);
          this.$store.dispatch('login', response.data.token);
          this.$router.push('/dashboard');
        } else {
          this.errorMessage = response.data.message || 'An error occurred. Please try again.';
        }
      } catch (error) {
        if (error.response && error.response.status === 401 && error.response.data.message === "Email not confirmed") {
          this.errorMessage = 'Email not verified. Please check your email to verify your account.';
        } else if (error.response && error.response.status === 404) {
          this.errorMessage = 'User not found. Please register first.';
        } else {
          this.errorMessage = error.response ? error.response.data.message : 'An error occurred. Please try again.';
        }
      }
    },
    async resendVerificationEmail() {
      try {
        const response = await axiosInstance.post('/resend-verification', {
          email: this.username  // Assuming the username field contains the email
        });
        alert(response.data.message);
      } catch (error) {
        if (error.response && error.response.status === 429) {
          alert('You have exceeded the number of allowed requests. Please try again later.');
        } else {
          alert(error.response ? error.response.data.message : 'An error occurred. Please try again.');
        }
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #6c63ff, #4a4ae1);
  font-family: 'Roboto', sans-serif;
  padding: 20px;
  box-sizing: border-box;
}

.login-container {
  display: flex;
  background-color: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
  flex-direction: row;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.login-container:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.image-section {
  position: relative;
  width: 50%;
  background: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?fit=crop&w=500&q=80') center center/cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
}

.overlay {
  background: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 40px;
  text-align: center;
}

.overlay h2 {
  margin-bottom: 20px;
  font-size: 24px;
  animation: fadeInDown 1s;
}

.overlay p {
  font-size: 16px;
  line-height: 1.5;
  animation: fadeInUp 1s;
}

.form-section {
  padding: 40px;
  width: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.form-section h1 {
  text-align: center;
  margin-bottom: 10px;
  font-size: 24px;
  animation: fadeInDown 1s;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #333;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 16px;
}

.login-button {
  width: 100%;
  padding: 12px;
  background-color: #6c63ff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
  transition: background-color 0.3s, transform 0.3s;
}

.login-button:hover {
  background-color: #594acf;
  transform: scale(1.05);
}

.signup-text {
  text-align: center;
  margin-top: 20px;
}

.signup-text a {
  color: #6c63ff;
  text-decoration: none;
}

.signup-text a:hover {
  text-decoration: underline;
}

.message {
  margin-top: 20px;
  font-size: 14px;
  color: red;
  text-align: center;
}

@media (max-width: 768px) {
  .login-container {
    flex-direction: column;
  }
  
  .image-section, .form-section {
    width: 100%;
  }

  .image-section {
    height: 200px;
  }

  .overlay {
    padding: 20px;
  }

  .overlay h2 {
    font-size: 20px;
  }

  .overlay p {
    font-size: 14px;
  }

  .form-section {
    padding: 20px;
  }
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 730px) {
  .form-group input[data-v-943f3ba8] {
    width: 90%;
    margin: 0 auto; /* Center the input field */
  }
  
  .form-group input[data-v-8dac4566] {
    width: 90%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 16px;}
  
    .login-button[data-v-8dac4566] {
    width: 90%;
    padding: 12px;
    background-color: #6c63ff;
    color: white;
    }
  }
    
</style>
