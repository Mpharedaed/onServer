<template>
  <div class="signup-page">
    <div class="signup-container">
      <div class="image-section">
        <div class="overlay">
          <h2>Welcome to signup form</h2>
          <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
        </div>
      </div>
      <div class="form-section">
        <h1>Sign Up #06</h1>
        <h3>Signup with these services</h3>
        <div class="social-buttons">
          <button class="google"><i class="fab fa-google"></i></button>
          <button class="facebook"><i class="fab fa-facebook-f"></i></button>
          <button class="twitter"><i class="fab fa-twitter"></i></button>
        </div>
        <div class="divider">or</div>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="fullname">Full Name</label>
            <input type="text" id="fullname" v-model="fullname" required>
          </div>
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required>
          </div>
          <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" v-model="email" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required>
          </div>
          <div class="form-group checkbox">
            <input type="checkbox" id="terms" v-model="terms" required>
            <label for="terms">I Agree All Statements In Terms Of Service</label>
          </div>
          <button type="submit" class="create-account">Create an account</button>
        </form>
        <p class="signin-text">I'm already a member! <router-link to="/login">Sign In</router-link></p>
        <div v-if="message" class="message">{{ message }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      fullname: '',
      username: '',
      email: '',
      password: '',
      terms: false,
      message: ''
    };
  },
  methods: {
    async submitForm() {
      this.message = '';  // Clear previous messages
      if (!this.terms) {
        this.message = 'You must agree to the terms of service';
        return;
      }
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/signup', {
          fullname: this.fullname,
          username: this.username,
          email: this.email,
          password: this.password
        });
        if (response.data.message) {
          this.message = response.data.message;
          this.$router.push('/login'); // Redirect to login page
        } else {
          this.message = response.data.error || 'An error occurred. Please try again.';
        }
      } catch (error) {
        this.message = error.response ? error.response.data.error : 'An error occurred. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

.signup-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #6c63ff, #4a4ae1);
  font-family: 'Roboto', sans-serif;
  padding: 20px;
  box-sizing: border-box;
}

.signup-container {
  display: flex;
  background-color: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
  width: 100%;
  flex-direction: row;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.signup-container:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.image-section {
  position: relative;
  width: 50%;
  background: url('https://images.unsplash.com/photo-1578070181910-f1e514afdd08?q=80&w=1833&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') center center/cover no-repeat;
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

.form-section h3 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 18px;
  animation: fadeInUp 1s;
}

.social-buttons {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.social-buttons button {
  background: none;
  border: none;
  font-size: 24px;
  margin: 0 10px;
  cursor: pointer;
  transition: color 0.3s, transform 0.3s;
}

.social-buttons button:hover {
  color: #555;
  transform: scale(1.1);
}

.social-buttons .google {
  color: #db4437;
}

.social-buttons .facebook {
  color: #4267b2;
}

.social-buttons .twitter {
  color: #1da1f2;
}

.divider {
  text-align: center;
  margin: 20px 0;
  color: #bbb;
  position: relative;
}

.divider::before, .divider::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 45%;
  height: 1px;
  background: #ddd;
}

.divider::before {
  left: 0;
}

.divider::after {
  right: 0;
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

.checkbox {
  display: flex;
  align-items: center;
}

.checkbox input {
  margin-right: 10px;
}

.create-account {
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

.create-account:hover {
  background-color: #594acf;
  transform: scale(1.05);
}

.signin-text {
  text-align: center;
  margin-top: 20px;
}

.signin-text a {
  color: #6c63ff;
  text-decoration: none;
}

.signin-text a:hover {
  text-decoration: underline;
}

.message {
  margin-top: 20px;
  font-size: 14px;
  color: red;
  text-align: center;
}

@media (max-width: 768px) {
  .signup-container {
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
</style>
