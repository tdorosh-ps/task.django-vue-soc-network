import {
  AUTH_REQUEST, AUTH_SUCCESS, AUTH_ERROR, AUTH_LOGOUT,
  CREATE_USER, SET_USER,
  SET_POSTS, SET_POST, CREATE_POST, LIKE_POST
} from './mutation-types.js'


export default {
  // Auth mutations
  [AUTH_REQUEST] (state){
    state.authStatus = 'loading';
    state.userEvent = '';
  },
  [AUTH_SUCCESS] (state, token){
    state.authStatus = 'success';
    state.accessToken = token.access;
    if (token.refresh) {
      state.refreshToken = token.refresh;
    }
  },
  [AUTH_ERROR] (state){
    state.authStatus = 'error';
  },
  [AUTH_LOGOUT] (state){
    state.authStatus = 'logout';
    state.accessToken = null;
    state.refreshToken = null;
  },

  // User mutations
  [CREATE_USER] (state) {
    state.userEvent = 'create';
  },
  [SET_USER] (state, user) {
    state.authUser = user;
  },

  //Posts mutations
  [SET_POSTS] (state, posts) {
    state.posts = posts;
  },
  [SET_POST] (state, post) {
    state.post = post;
  },
  [CREATE_POST] (state, post) {
    state.postEvent = 'create';
    state.post = [post, ...state.posts];
  },
  [LIKE_POST] (state, user, action) {
    if (action === 'like') {
      state.post.users_liked = [user, ...state.post.users_liked];
    } else if (action === 'unlike') {
        state.post.users_liked = state.post.users_liked.filter(postUser => {
          return postUser.id != user.id;
    });
    }
  },
};