// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

import axios from 'axios';
import VueAxios from 'vue-axios';

const app = createApp(App);

// Use Pinia
const pinia = createPinia();
app.use(pinia);

// Use other plugins
app.use(router);
app.use(VueAxios, axios);

app.mount('#app');
