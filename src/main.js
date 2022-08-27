import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus';
import 'element-plus/theme-chalk/index.css';



 
import locale from 'element-plus/lib/locale/lang/zh-cn'
createApp(App).use(ElementPlus, { locale }).mount('#app')

// import { createApp } from 'vue'

// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'

// import App from './App.vue'
// import './registerServiceWorker'


// createApp(App).use(ElementPlus)

// createApp(App).mount('#app')