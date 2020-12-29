import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axiosInstance from '@/axios.js'

Vue.config.productionTip = false

Vue.use(Vuex)
Vue.use(BootstrapVue)

const token = localStorage.getItem('user-token')
if (token) {
  axiosInstance.defaults.headers.common.Authorization = `Bearer ${token}`;
}

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
