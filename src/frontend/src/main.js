import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';

import 'vuetify/styles'
import { createVuetify } from 'vuetify'

const vuetify = createVuetify()
const app = createApp(App)


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/'; 


app.use(router).use(vuetify).mount('#app')

