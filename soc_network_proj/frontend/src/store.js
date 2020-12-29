import Vue from 'vue'
import Vuex from 'vuex'

import mutations from '@/store/mutations';
import actions from '@/store/actions';


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authUser: null,
    accessToken: localStorage.getItem('user-token') || '',
    refreshToken: localStorage.getItem('user-refresh-token') || '',
    authStatus: 'wait',
    userEvent: '',
    postEvent: '',
    posts: [],
    post: null
  },
  getters: {
    authUser: state => state.authUser,
    isAuthenticated: state => !!state.accessToken,
    authStatus: state => state.authStatus,
    userEvent: state => state.userEvent,
    posts: state => state.posts,
    post: state => state.post,
    postEvent: state => state.postEvent
  },
  mutations: Object.assign(mutations),
  actions: Object.assign(actions),
});