<template>
  <header class="header" :class="{ scrolled: isScrolled }">
    <div class="container">
      <div class="logo">
        <router-link to="/">
          <!-- Ensure the image path is correct -->
      
        </router-link>
      </div>
      <nav class="navigation">
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li v-if="isAuthenticated">
            <router-link to="/dashboard">Dashboard</router-link>
          </li>
          <li v-if="isAuthenticated">
            <router-link to="/profile">Profile</router-link>
          </li>
          <li v-if="!isAuthenticated">
            <router-link to="/login">Login</router-link>
          </li>
          <li v-if="isAuthenticated">
            <router-link to="/create-post">Create Post</router-link>
          </li>
          <li v-if="isAuthenticated">
            <a href="#" @click.prevent="logoutAndCloseMenu">Logout</a>
          </li>
        </ul>
      </nav>
      <div :class="['menu-toggle', { open: menuOpen }]" @click="toggleMenu">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
    <!-- Mobile Navigation Overlay -->
    <transition name="fade">
      <div
        class="mobile-navigation-overlay"
        v-if="menuOpen"
        @click.self="closeMenu"
      >
        <nav class="mobile-navigation">
          <button class="close-button" @click="closeMenu">&times;</button>
          <ul>
            <li>
              <router-link to="/" @click="closeMenu">Home</router-link>
            </li>
            <li>
              <router-link to="/about" @click="closeMenu">About</router-link>
            </li>
            <li v-if="isAuthenticated">
              <router-link to="/dashboard" @click="closeMenu">Dashboard</router-link>
            </li>
            <li v-if="isAuthenticated">
              <router-link to="/profile" @click="closeMenu">Profile</router-link>
            </li>
            <li v-if="!isAuthenticated">
              <router-link to="/login" @click="closeMenu">Login</router-link>
            </li>
            <li v-if="isAuthenticated">
              <router-link to="/create-post" @click="closeMenu">Create Post</router-link>
            </li>
            <li v-if="isAuthenticated">
              <a href="#" @click.prevent="logoutAndCloseMenu">Logout</a>
            </li>
          </ul>
        </nav>
      </div>
    </transition>
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

    // Logout and close menu function
    logoutAndCloseMenu() {
      this.logout().then(() => {
        this.$router.push('/login');
        this.closeMenu();
      });
    },

    // Toggle mobile menu
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
      if (this.menuOpen) {
        document.body.style.overflow = 'hidden'; // Prevent background scroll
      } else {
        document.body.style.overflow = 'auto'; // Restore background scroll
      }
    },

    // Close mobile menu
    closeMenu() {
      this.menuOpen = false;
      document.body.style.overflow = 'auto'; // Restore background scroll
    },

    // Handle scroll event for header
    handleScroll() {
      this.isScrolled = window.scrollY > 50;
    },

    // Debounce for performance improvement on scroll
    debounce(fn, delay) {
      let timer = null;
      return function (...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
      };
    },
  },
  mounted() {
    this.handleScroll = this.debounce(this.handleScroll, 50); // Debounced scroll handling
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
};
</script>

<style src="./AppHeader.css"></style>
