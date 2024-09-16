<template>
  <header class="header" :class="{ scrolled: isScrolled }">
    <div class="container">
      <div class="logo">
        <router-link to="/">
          <!-- Update the path to your logo image -->
          
        </router-link>
      </div>
      <nav class="navigation">
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/dashboard">Dashboard</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/profile">Profile</router-link></li>
          <li v-if="!isAuthenticated"><router-link to="/login">Login</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/create-post">Create Post</router-link></li>
          <li v-if="isAuthenticated"><a href="#" @click.prevent="logoutUser">Logout</a></li>
        </ul>
      </nav>
      <div class="menu-toggle" :class="{ open: menuOpen }" @click="toggleMenu">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
    <!-- Mobile Navigation Overlay -->
    <div class="mobile-nav-overlay" :class="{ open: menuOpen }">
      <nav class="mobile-navigation">
        <ul>
          <li><router-link to="/" @click="closeMenu">Home</router-link></li>
          <li><router-link to="/about" @click="closeMenu">About</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/dashboard" @click="closeMenu">Dashboard</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/profile" @click="closeMenu">Profile</router-link></li>
          <li v-if="!isAuthenticated"><router-link to="/login" @click="closeMenu">Login</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/create-post" @click="closeMenu">Create Post</router-link></li>
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
  data() {
    return {
      menuOpen: false,
      isScrolled: false,
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  methods: {
    ...mapActions(['logout']),
    logoutUser() {
      this.logout().then(() => {
        this.$router.push('/login');
      });
    },
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    closeMenu() {
      this.menuOpen = false;
    },
    handleScroll() {
      this.isScrolled = window.scrollY > 50;
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
};
</script>

<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

/* General Header Styles */
.header {
  background-color: transparent;
  color: #ffffff;
  padding: 20px 30px;
  position: fixed;
  width: 100%;
  z-index: 1000;
  top: 0;
  transition: background-color 0.4s ease, padding 0.4s ease;
}

.header.scrolled {
  background-color: rgba(0, 0, 0, 0.85);
  padding: 15px 30px;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.logo img {
  height: 40px;
  transition: transform 0.3s ease;
}

.logo img:hover {
  transform: rotate(360deg);
}

.navigation {
  display: flex;
  align-items: center;
}

.navigation ul {
  list-style: none;
  display: flex;
  gap: 30px;
  margin: 0;
  padding: 0;
  font-family: 'Montserrat', sans-serif;
}

.navigation ul li {
  display: inline-block;
}

.navigation a {
  color: #ffffff;
  text-decoration: none;
  font-size: 1rem;
  position: relative;
  transition: color 0.3s ease;
}

.navigation a::after {
  content: '';
  position: absolute;
  width: 0%;
  height: 2px;
  background-color: #ffcc00;
  left: 50%;
  bottom: -5px;
  transform: translateX(-50%);
  transition: width 0.3s ease;
}

.navigation a:hover::after {
  width: 100%;
}

.navigation a:hover {
  color: #ffcc00;
}

/* Mobile Menu Toggle */
.menu-toggle {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 25px;
  height: 20px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.menu-toggle span {
  background: #ffffff;
  height: 2px;
  width: 100%;
  border-radius: 2px;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.menu-toggle.open span:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.menu-toggle.open span:nth-child(2) {
  opacity: 0;
}

.menu-toggle.open span:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

/* Mobile Navigation Overlay */
.mobile-nav-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #6A0572, #A904B5);
  opacity: 0;
  visibility: hidden;
  transform: scale(1.1);
  transition: opacity 0.5s ease, transform 0.5s ease, visibility 0.5s;
  z-index: 999;
}

.mobile-nav-overlay.open {
  opacity: 1;
  visibility: visible;
  transform: scale(1);
}

.mobile-navigation {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
}

.mobile-navigation ul {
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.mobile-navigation ul li {
  margin: 20px 0;
  opacity: 0;
  animation: slideIn 0.5s forwards;
}

.mobile-navigation ul li:nth-child(1) {
  animation-delay: 0.2s;
}

.mobile-navigation ul li:nth-child(2) {
  animation-delay: 0.3s;
}

.mobile-navigation ul li:nth-child(3) {
  animation-delay: 0.4s;
}

.mobile-navigation ul li:nth-child(4) {
  animation-delay: 0.5s;
}

.mobile-navigation ul li:nth-child(5) {
  animation-delay: 0.6s;
}

.mobile-navigation ul li:nth-child(6) {
  animation-delay: 0.7s;
}

.mobile-navigation ul li:nth-child(7) {
  animation-delay: 0.8s;
}

.mobile-navigation a {
  color: #ffffff;
  font-size: 1.8rem;
  text-decoration: none;
  transition: color 0.3s ease;
  font-family: 'Montserrat', sans-serif;
}

.mobile-navigation a:hover {
  color: #ffcc00;
}

/* Animations */
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Media Queries */
@media (max-width: 768px) {
  .navigation {
    display: none;
  }

  .menu-toggle {
    display: flex;
  }
}
</style>
