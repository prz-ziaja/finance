import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';


// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";


const vuetify = createVuetify({
    components: {...components},
    directives
})


const app = createApp(App)


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/'; 




app.use(router).use(vuetify).mount('#app')

