import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null, // Add any other state you need
    token: localStorage.getItem('token') || null,
  },
  getters: {
    isAuthenticated: state => !!state.token,
    // Add any other getters you need
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    },
    logout(state) {
      state.user = null;
      state.token = null;
    },
    // Add any other mutations you need
  },
  actions: {
    login({ commit }, { user, token }) {
      commit('setUser', user);
      commit('setToken', token);
      localStorage.setItem('token', token);
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('token');
    },
    // Add any other actions you need
  }
});
