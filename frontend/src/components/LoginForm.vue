<template>
  <div class="login-page">
    <div class="login-container">
      <div class="form-section">
        <h1>Welcome Back</h1>
        <p class="subtitle">Please login to continue</p>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <button type="submit" class="login-button">Login</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        <p v-if="resetPasswordLink" class="reset-link">
          Forgot your password? <router-link :to="{ name: 'ResetPasswordRequest' }">Reset it here</router-link>
        </p>
        <p v-if="errorMessage === 'Email not verified. Please check your email to verify your account.'">
          Didn't receive an email? <button @click="resendVerificationEmail">Resend Verification Email</button>
        </p>
        <p class="signup-text">Don't have an account? <router-link to="/signup">Sign Up</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from "@/plugins/axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
      resetPasswordLink: false,
    };
  },
  methods: {
    async submitForm() {
      this.errorMessage = "";
      this.resetPasswordLink = false;
      try {
        const response = await axiosInstance.post("/login", {
          email: this.username,
          password: this.password,
        });

        if (response.data.token) {
          localStorage.setItem("token", response.data.token);
          this.$store.dispatch("login", response.data.token);
          this.$router.push("/dashboard");
        } else {
          this.errorMessage =
            response.data.message || "An error occurred. Please try again.";
        }
      } catch (error) {
        if (
          error.response &&
          error.response.status === 401 &&
          error.response.data.message === "Email not confirmed"
        ) {
          this.errorMessage =
            "Email not verified. Please check your email to verify your account.";
        } else if (error.response && error.response.status === 404) {
          this.errorMessage = "User not found. Please register first.";
        } else if (error.response && error.response.status === 401) {
          this.errorMessage = error.response.data.message;
          this.resetPasswordLink = true;
        } else {
          this.errorMessage = error.response
            ? error.response.data.message
            : "An error occurred. Please try again.";
        }
      }
    },
    async resendVerificationEmail() {
      try {
        const response = await axiosInstance.post("/resend-verification", {
          email: this.username,
        });
        alert(response.data.message);
      } catch (error) {
        if (error.response && error.response.status === 429) {
          alert(
            "You have exceeded the number of allowed requests. Please try again later."
          );
        } else {
          alert(
            error.response
              ? error.response.data.message
              : "An error occurred. Please try again."
          );
        }
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap");

.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f3e7e9 0%, #e3eeff 100%);
  font-family: "Poppins", sans-serif;
  padding: 20px;
  box-sizing: border-box;
}

.login-container {
  background-color: white;
  border-radius: 15px;
  padding: 40px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.login-container::before {
  content: "";
  position: absolute;
  width: 150%;
  height: 150%;
  background: linear-gradient(45deg, #6c63ff, #f59e42);
  top: -75%;
  left: -75%;
  transform: rotate(45deg);
  z-index: 1;
  opacity: 0.15;
}

.login-container:hover {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.form-section h1 {
  margin-bottom: 15px;
  font-size: 28px;
  font-weight: 700;
  color: #333;
  position: relative;
  z-index: 2;
}

.subtitle {
  font-size: 16px;
  color: #888;
  margin-bottom: 30px;
  position: relative;
  z-index: 2;
}

.form-group {
  margin-bottom: 20px;
  position: relative;
  z-index: 2;
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

.login-button {
  width: 100%;
  padding: 12px;
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

.login-button:hover {
  background-color: #4a4ae1;
  transform: translateY(-2px);
}

.signup-text {
  margin-top: 20px;
  font-size: 14px;
  position: relative;
  z-index: 2;
}

.signup-text a {
  color: #6c63ff;
  text-decoration: none;
}

.signup-text a:hover {
  text-decoration: underline;
}

.error {
  margin-top: 20px;
  font-size: 14px;
  color: red;
  text-align: center;
  position: relative;
  z-index: 2;
}

.reset-link {
  margin-top: 10px;
  text-align: center;
  font-size: 14px;
  color: #6c63ff;
  position: relative;
  z-index: 2;
}

.reset-link a {
  color: #6c63ff;
}

@media (max-width: 768px) {
  .login-container {
    padding: 20px;
  }

  .form-section h1 {
    font-size: 24px;
  }

  .form-group input {
    padding: 10px;
  }

  .login-button {
    padding: 10px;
    font-size: 14px;
  }

  .signup-text {
    font-size: 12px;
  }

  .reset-link {
    font-size: 12px;
  }
}
</style>
