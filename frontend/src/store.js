import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  token: localStorage.getItem('token') || '',
};

const getters = {
  isAuthenticated: state => !!state.token,
};

const mutations = {
  setToken(state, token) {
    state.token = token;
    localStorage.setItem('token', token);
  },
  clearToken(state) {
    state.token = '';
    localStorage.removeItem('token');
  }
};

const actions = {
  login({ commit }, token) {
    commit('setToken', token);
  },
  logout({ commit }) {
    commit('clearToken');
  }
};

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
});
