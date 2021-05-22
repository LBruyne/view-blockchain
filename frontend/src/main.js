import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'

Vue.prototype.$http = axios

axios.defaults.baseURL = 'http://localhost:5000'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
axios.defaults.headers.common['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, DELETE'
axios.defaults.headers.common['Access-Control-Max-Age'] = '3600'
axios.defaults.headers.common['Access-Control-Allow-Credentials'] = 'true'
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'x-requested-with,Authorization,token, content-type'

Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
