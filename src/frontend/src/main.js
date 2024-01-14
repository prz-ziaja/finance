import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';


// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

//Vuetify Icons
import { fa } from "vuetify/iconsets/fa";
import { aliases, mdi } from 'vuetify/iconsets/mdi';

import "@mdi/font/css/materialdesignicons.css";
import "@fortawesome/fontawesome-free/css/all.css";


const vuetify = createVuetify({
    components: {...components},
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
            fa
        }
    },
    theme: {
        defaultTheme: 'dark'
    }
})

const app = createApp(App)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/'; 

app.use(router).use(vuetify).mount('#app')
