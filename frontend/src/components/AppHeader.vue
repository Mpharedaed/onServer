<template>
  <header class="header" :class="{ scrolled: isScrolled }">
    <div class="container">
      <div class="logo">
        <h1>Trillow</h1>
      </div>
      <nav class="navigation" :class="{ open: menuOpen }">
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
      <div class="menu-toggle" @click="toggleMenu">
        <span></span>
        <span></span>
        <span></span>
      </div>
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
    ...mapGetters(['isAuthenticated'])
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
    handleScroll() {
      this.isScrolled = window.scrollY > 50;
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

/* General Header Styles */
.header {
  background: linear-gradient(135deg, #6A0572, #A904B5);
  color: #ffffff;
  padding: 15px 30px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  position: fixed;
  width: 100%;
  z-index: 1000;
  top: 0;
  transition: background 0.4s ease, padding 0.4s ease, box-shadow 0.4s ease;
}

.header.scrolled {
  background: linear-gradient(135deg, #4A0357, #8A029D);
  padding: 10px 30px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
}

/* Container and Logo */
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  box-sizing: border-box;
}

.logo h1 {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
  margin: 0;
  font-size: 28px;
  color: #ffffff;
  text-transform: uppercase;
  letter-spacing: 2px;
  animation: fadeInDown 0.8s ease-out;
}

/* Navigation Styles */
.navigation {
  display: flex;
  align-items: center;
}

.navigation ul {
  list-style: none;
  display: flex;
  gap: 25px;
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.navigation ul li {
  display: inline-block;
}

.navigation a {
  color: #ffffff;
  text-decoration: none;
  position: relative;
  padding: 10px 15px;
  transition: color 0.3s ease, background 0.3s ease;
  border-radius: 5px;
  font-size: 1.1em;
}

.navigation a::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  left: 50%;
  bottom: 0;
  background: #FFC107;
  transition: width 0.3s ease;
  transform: translateX(-50%);
}

.navigation a:hover::after {
  width: 100%;
}

.navigation a:hover {
  color: #FFC107;
}

/* Mobile Menu Toggle */
.menu-toggle {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 24px;
  height: 18px;
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

.menu-open .menu-toggle span:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.menu-open .menu-toggle span:nth-child(2) {
  opacity: 0;
}

.menu-open .menu-toggle span:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Mobile Navigation */
.navigation.open {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  background: #ffffff;
  position: absolute;
  top: 60px;
  left: 0;
  width: 100%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  padding: 20px;
  border-radius: 0 0 8px 8px;
  animation: fadeInDown 0.3s ease-out;
}

.navigation.open ul {
  flex-direction: column;
  gap: 15px;
}

.navigation.open ul li {
  width: 100%;
}

.navigation.open ul li a {
  width: 100%;
  text-align: left;
  padding: 10px 0;
  color: #333333;
}

@media (max-width: 768px) {
  .navigation {
    display: none;
  }

  .menu-toggle {
    display: flex;
  }

  .menu-open .navigation {
    display: flex;
  }
}
</style>
