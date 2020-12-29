import Vue from 'vue'
import VueRouter from 'vue-router'

import SignIn from './views/SignIn.vue'
import SignUp from './views/SignUp.vue'
import allPostsList from '@/views/allPostsList.vue'
import ownPostsList from '@/views/ownPostsList.vue'
import postForm from '@/components/post/postForm.vue'
import postRetrieve from '@/components/post/postRetrieve.vue'


import store from './store'


Vue.use(VueRouter)

const ifNotAuthenticated = (to, form, next) => {
  if (!store.getters.isAuthenticated) {
    next();
    return;
  }
  next('/posts/own');
};

const ifAuthenticated = (to, form, next) => {
  if (store.getters.isAuthenticated) {
    next();
    return;
  }
  next('/signin');
};


export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/posts/own'
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignIn,
      beforeEnter: ifNotAuthenticated,
    },
    {
      path: '/posts/own',
      name: 'own-posts',
      component: ownPostsList,
      beforeEnter: ifAuthenticated,
    },
    {
      path: '/posts/all',
      name: 'all-posts',
      component: allPostsList,
      beforeEnter: ifAuthenticated,
    },
    {
      path: '/post/create',
      name: 'create-post',
      component: postForm,
      beforeEnter: ifAuthenticated,
    },
    {
      path: '/post/:id',
      name: 'retrieve-post',
      component: postRetrieve,
      beforeEnter: ifAuthenticated,
    },
  ],
});