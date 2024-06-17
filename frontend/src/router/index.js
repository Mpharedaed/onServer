import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import AboutPage from '@/views/AboutPage.vue';
import LoginForm from '@/components/LoginForm.vue';
import SignupForm from '@/components/SignupForm.vue';
import UserDashboard from '@/components/UserDashboard.vue'; // Adjusted import path
import store from '@/store'; // Import the Vuex store

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage
  },
  {
    path: '/dashboard',
    name: 'UserDashboard',
    component: UserDashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginForm
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupForm
  }
];

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const loggedIn = store.getters.isAuthenticated;
  const previousRoute = from.path;

  console.log(`Navigating to ${to.path} from ${from.path}. Logged in: ${loggedIn}`);

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    console.log(`Access to ${to.path} requires auth. Redirecting to login.`);
    if (to.path !== '/login') {
      next('/login');
    } else {
      next();
    }
  } else if ((to.path === '/login' || to.path === '/signup') && loggedIn) {
    console.log(`Already logged in. Redirecting to dashboard.`);
    if (previousRoute !== '/dashboard') {
      next('/dashboard');
    } else {
      next('/');
    }
  } else {
    next();
  }
});

export default router;
