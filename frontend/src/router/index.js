import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import AboutPage from '@/views/AboutPage.vue';
import LoginForm from '@/components/LoginForm.vue';
import SignupForm from '@/components/SignupForm.vue';
import UserDashboard from '@/components/UserDashboard.vue';
import CreatePost from '@/components/CreatePost.vue';
import UserProfile from '@/components/UserProfile.vue';
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
  },
  {
    path: '/create-post',
    name: 'CreatePost',
    component: CreatePost,
    meta: { requiresAuth: true } // Ensure this route requires authentication
  },
  {
    path: '/profile',
    name: 'UserProfile',
    component: UserProfile,
    meta: { requiresAuth: true } // Ensure this route requires authentication
  }
];

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const loggedIn = store.getters.isAuthenticated;
  console.log(`Navigating to ${to.path} from ${from.path}. Logged in: ${loggedIn}`);

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    console.log(`Access to ${to.path} requires auth. Redirecting to login.`);
    next('/login');
  } else if ((to.path === '/login' || to.path === '/signup') && loggedIn) {
    console.log(`Already logged in. Redirecting to dashboard.`);
    next('/dashboard');
  } else {
    next();
  }
});

export default router;
