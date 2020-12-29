import {
  AUTH_REQUEST, AUTH_SUCCESS, AUTH_ERROR, AUTH_LOGOUT,
  CREATE_USER, SET_USER,
  SET_POSTS, SET_POST, CREATE_POST, LIKE_POST
} from './mutation-types.js'

import axiosInstance from '../axios.js'

const HTTP = axiosInstance;

const actions = {

  //Auth actions
  authRequest ({ commit }, data) {
    return new Promise((resolve, reject) => {
      commit(AUTH_REQUEST);
      HTTP.post('token/', data)
      .then((response) => {
        const token = response.data;
        localStorage.setItem('user-token', token.access);
        localStorage.setItem('user-refresh-token', token.refresh);
        axiosInstance.defaults.headers.common.Authorization = `Bearer ${token.access}`;
        commit(AUTH_SUCCESS, token);
        resolve(response);
      })
      .catch((err) => {
        commit(AUTH_ERROR);
        localStorage.removeItem('user-token');
        localStorage.removeItem('user-refresh-token');
        reject(err);
      });
    });
  },
  refreshAuthRequest ({ commit }, data) {
    return new Promise((resolve, reject) => {
      commit(AUTH_REQUEST);
      HTTP.post('token/refresh/', data)
      .then((response) => {
        const token = response.data;
        localStorage.setItem('user-token', token.access);
        axiosInstance.defaults.headers.common.Authorization = `Bearer ${token.access}`;
        commit(AUTH_SUCCESS, token);
        resolve(response);
      })
      .catch((err) => {
        commit(AUTH_ERROR);
        localStorage.removeItem('user-token');
        localStorage.removeItem('user-refresh-token');
        reject(err);
      });
    });
  },
  authLogout ({ commit }) {
    return new Promise((resolve) => {
      commit(AUTH_LOGOUT);
      localStorage.removeItem('user-token');
      localStorage.removeItem('user-refresh-token');
      delete axiosInstance.defaults.headers.common.Authorization;
      resolve();
    })
  },

  //User actions
  createUser ({ commit }, data) {
    return new Promise((resolve, reject) => {
      HTTP.post('accounts/create/', data)
        .then((response) => {
          commit(CREATE_USER);
          resolve(response)
        })
        .catch((error) => {
          reject(error);
        })
    })
  },
  async getUser({ commit }) {
    const response = await HTTP.get('accounts/');
    if (response.status === 200) {
      commit(SET_USER, response.data)
    }
  },

  //Posts actions
  async getPosts ({ commit }, params) {
    const response = await HTTP.get('posts/', params);
    if (response.status === 200) {
      commit(SET_POSTS, response.data);
    }
  },
  async getPost ({ commit }, postId) {
    const response = await HTTP.get(`post/${postId}/`)
    if (response.status === 200) {
      commit(SET_POST, response.data)
    }
  },
  async createPost ({ commit }, postData) {
    const response = await HTTP.post('post/create/', postData);
    if (response.status === 201) {
      commit(CREATE_POST, response.data)
    }
  },
  async likePost ({ commit }, postLikeData) {
    const response = await HTTP.post(`post/${postLikeData.post.id}/like/`, postLikeData.data);
    if (response.status === 202) {
      commit(LIKE_POST, postLikeData.post.owner, postLikeData.data.action)
    }
  },
}

export default actions;