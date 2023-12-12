import * as Vue from 'vue' // in Vue 3
import App from './App.vue'
import router from './router'
// load bootstrap
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
// axios
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.createApp(App).use(router, VueAxios, axios).mount('#app')