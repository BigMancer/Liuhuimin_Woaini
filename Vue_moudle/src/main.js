import {
    createApp
} from 'vue'
// import './public/static/css/myself.css'; 
import App from './App.vue'
import router from './router'
import store from './store'
// import axios from 'axios'
const app = createApp(App)
app.use(store)
app.use(router)
// app.prototype.$axios = axios
app.mount('#app')