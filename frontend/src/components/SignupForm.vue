<template>
  <div class="auth-page">
    <div class="auth-container">
      <div class="form-section">
        <h1>Join Our Community</h1>
        <p class="subtitle">Create your account in just a few easy steps</p>
        <form @submit.prevent="submitForm" aria-live="polite">
          <transition name="slide-fade" mode="out-in">
            <div v-if="step === 1" key="step1">
              <div class="form-group">
                <label for="fullname">Full Name</label>
                <input type="text" id="fullname" v-model="fullname" required />
              </div>
              <button type="button" class="next-button" @click="nextStep">
                Next
              </button>
            </div>
            <div v-if="step === 2" key="step2">
              <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" required />
              </div>
              <div class="button-group">
                <button type="button" class="prev-button" @click="prevStep">
                  Back
                </button>
                <button type="button" class="next-button" @click="nextStep">
                  Next
                </button>
              </div>
            </div>
            <div v-if="step === 3" key="step3">
              <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" v-model="email" required />
              </div>
              <div class="button-group">
                <button type="button" class="prev-button" @click="prevStep">
                  Back
                </button>
                <button type="button" class="next-button" @click="nextStep">
                  Next
                </button>
              </div>
            </div>
            <div v-if="step === 4" key="step4">
              <div class="form-group">
                <label for="password">Password</label>
                <input
                  type="password"
                  id="password"
                  v-model="password"
                  required
                />
              </div>
              <div class="button-group">
                <button type="button" class="prev-button" @click="prevStep">
                  Back
                </button>
                <button type="submit" class="create-account">
                  Create an Account
                </button>
              </div>
            </div>
          </transition>
        </form>
        <p class="signin-text">
          Already a member?
          <router-link to="/login">Sign In</router-link>
        </p>
        <div v-if="message" class="message">{{ message }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from "@/plugins/axios";

export default {
  data() {
    return {
      step: 1,
      fullname: "",
      username: "",
      email: "",
      password: "",
      message: "",
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
      this.message = ""; // Clear previous messages
      try {
        const response = await axiosInstance.post("/signup", {
          fullname: this.fullname,
          username: this.username,
          email: this.email,
          password: this.password,
        });
        if (response.data.success) {
          this.message = "Signup successful! Redirecting to login page...";
          setTimeout(() => {
            if (this.$route.path !== "/login") {
              this.$router.push("/login");
            }
          }, 2000);
        } else {
          this.message =
            response.data.error || "An error occurred. Please try again.";
        }
      } catch (error) {
        this.message = error.response
          ? error.response.data.error
          : "An error occurred. Please try again.";
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap");

.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-family: "Poppins", sans-serif;
  padding: 20px;
  box-sizing: border-box;
  overflow: hidden;
  background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
  position: relative;
}

.auth-page::before {
  content: "";
  position: absolute;
  top: -50px;
  right: -50px;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.5) 0%, rgba(255, 255, 255, 0) 70%);
  transform: rotate(30deg);
}

.auth-page::after {
  content: "";
  position: absolute;
  bottom: -50px;
  left: -50px;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0) 70%);
  transform: rotate(-30deg);
}

.auth-container {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  padding: 40px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  max-width: 450px;
  width: 100%;
  text-align: center;
  position: relative;
  z-index: 1;
}

.form-section h1 {
  margin-bottom: 15px;
  font-size: 28px;
  font-weight: 700;
  color: #333;
}

.subtitle {
  font-size: 16px;
  color: #888;
  margin-bottom: 30px;
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
  border-radius: 30px;
  box-sizing: border-box;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.form-group input:focus {
  border-color: #6c63ff;
  outline: none;
}

.button-group {
  display: flex;
  justify-content: space-between;
}

.next-button,
.prev-button,
.create-account {
  padding: 12px 20px;
  background-color: #6c63ff;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
  font-weight: 500;
  transition: background-color 0.3s, transform 0.3s;
}

.next-button:hover,
.prev-button:hover,
.create-account:hover {
  background-color: #4a4ae1;
  transform: translateY(-2px);
}

.prev-button {
  margin-right: 10px;
}

.signin-text {
  margin-top: 20px;
  font-size: 14px;
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

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.5s ease;
}

.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}

@media (max-width: 768px) {
  .auth-container {
    padding: 20px;
  }

  .form-section h1 {
    font-size: 24px;
  }

  .form-group input {
    padding: 10px;
  }

  .next-button,
  .prev-button,
  .create-account {
    padding: 10px;
    font-size: 14px;
  }

  .signin-text {
    font-size: 12px;
  }
}
</style>
