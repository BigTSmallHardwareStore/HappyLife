import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

axios.defaults.baseURL = import.meta.env.VITE_DJANGO_ROUTER // URL for Django

app.use(createPinia())
app.use(router, axios)

app.mount('#app')