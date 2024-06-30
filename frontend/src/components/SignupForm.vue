<template>
  <div class="signup-page">
    <div class="signup-container">
      <div class="image-section">
        <div class="overlay">
          <h2>Welcome to Signup Form</h2>
          <p>Join our community and start your journey today.</p>
        </div>
      </div>
      <div class="form-section">
        <h1>Sign Up</h1>
        <form @submit.prevent="submitForm" aria-live="polite">
          <!-- Step 1 -->
          <div v-if="step === 1">
            <div class="form-group">
              <label for="fullname">Full Name</label>
              <input type="text" id="fullname" v-model="fullname" required>
            </div>
            <button type="button" class="next-button" @click="nextStep">Next</button>
          </div>
          <!-- Step 2 -->
          <div v-if="step === 2">
            <div class="form-group">
              <label for="username">Username</label>
              <input type="text" id="username" v-model="username" required>
            </div>
            <button type="button" class="prev-button" @click="prevStep">Back</button>
            <button type="button" class="next-button" @click="nextStep">Next</button>
          </div>
          <!-- Step 3 -->
          <div v-if="step === 3">
            <div class="form-group">
              <label for="email">Email Address</label>
              <input type="email" id="email" v-model="email" required>
            </div>
            <button type="button" class="prev-button" @click="prevStep">Back</button>
            <button type="button" class="next-button" @click="nextStep">Next</button>
          </div>
          <!-- Step 4 -->
          <div v-if="step === 4">
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" id="password" v-model="password" required>
            </div>
            <button type="button" class="prev-button" @click="prevStep">Back</button>
            <button type="submit" class="create-account">Create an Account</button>
          </div>
        </form>
        <p class="signin-text">Already a member? <router-link to="/login">Sign In</router-link></p>
        <div v-if="message" class="message">{{ message }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from '@/plugins/axios';

export default {
  data() {
    return {
      step: 1,
      fullname: '',
      username: '',
      email: '',
      password: '',
      message: ''
    };
  },
  methods: {
    nextStep() {
      if (this.step < 4) {
        this.step++;
      }
    },
    prevStep() {
      if (this.step > 1) {
        this.step--;
      }
    },
    async submitForm() {
      this.message = ''; // Clear previous messages
      try {
        const response = await axiosInstance.post('/signup', {
          fullname: this.fullname,
          username: this.username,
          email: this.email,
          password: this.password
        });
        if (response.data.success) {
          this.message = 'Signup successful! Redirecting to login page...';
          setTimeout(() => {
            if (this.$route.path !== '/login') {
              this.$router.push('/login');
            }
          }, 2000);
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

.form-group input:focus {
  border-color: #6c63ff;
}

.next-button, .prev-button {
  padding: 12px 20px;
  margin-top: 20px;
  background-color: #6c63ff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s, transform 0.3s;
}

.next-button:hover, .prev-button:hover {
  background-color: #594acf;
  transform: scale(1.05);
}

.prev-button {
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

@media (max-width: 480px) {
  .form-group input {
    font-size: 14px;
    padding: 10px;
  }

  .create-account {
    font-size: 14px;
    padding: 10px;
  }

  .overlay h2 {
    font-size: 18px;
  }

  .overlay p {
    font-size: 12px;
  }

  .form-section h1 {
    font-size: 20px;
  }

  .social-buttons button {
    font-size: 20px;
    margin: 0 5px;
  }

  .divider {
    margin: 10px 0;
  }

  .divider::before, .divider::after {
    width: 40%;
  }

  .signup-container {
    padding: 10px;
  }

  .form-section {
    padding: 20px;
    width: 100%;
    box-sizing: border-box;
  }

  .form-group {
    padding: 0 10px;
    box-sizing: border-box;
  }
}
</style>
