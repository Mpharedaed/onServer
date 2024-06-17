<template>
  <header class="header">
    <div class="container">
      <div class="logo">
        <h1>My App</h1>
      </div>
      <nav class="navigation">
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/dashboard">Dashboard</router-link></li>
          <li v-if="!isAuthenticated"><router-link to="/login">Login</router-link></li>
          <li v-if="isAuthenticated"><a href="#" @click.prevent="logoutUser">Logout</a></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AppHeader',
  computed: {
    ...mapGetters(['isAuthenticated'])
  },
  methods: {
    ...mapActions(['logout']),
    logoutUser() {
      this.logout().then(() => {
        this.$router.push('/login');
      });
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

.header {
  background: linear-gradient(135deg, #6c63ff, #4a4ae1);
  color: white;
  padding: 20px 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: fixed;
  width: 100%;
  z-index: 1000;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}

.logo h1 {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
  margin: 0;
  font-size: 24px;
  animation: fadeInDown 1s ease;
}

.navigation ul {
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.navigation a {
  color: white;
  text-decoration: none;
  position: relative;
  transition: color 0.3s ease;
}

.navigation a::before {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -2px;
  left: 0;
  background-color: white;
  visibility: hidden;
  transition: all 0.3s ease-in-out;
}

.navigation a:hover::before {
  visibility: visible;
  width: 100%;
}

.navigation a:hover {
  color: #e0e0e0;
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
</style>
