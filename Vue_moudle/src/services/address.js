// 该文件无用

import axios from 'axios'
if (process.env.NODE_ENV == 'development') {
    // 开发环境
    axios.defaults.baseURL = 'http://127.0.0.1:5000';
} else if (process.env.NODE_ENV == 'debug') {
    // 测试环境
    axios.defaults.baseURL = 'http://127.0.0.1:5000';
} else if (process.env.NODE_ENV == 'production') {
    // 生产环境  
    axios.defaults.baseURL = 'http://刘慧敏.我爱你/';
}