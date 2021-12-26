import {post} from '../services/request'
/**
 * @description 获取用户列表
 * @param {*} params 请求接口的参数
 */
// 此处定义的reqUserList方法会调用我们封装的request中的get方法，get方法的第一个参数是请求地址，第二参数是query参数
export const api_send_mail = params => post('/Nebula_BH_No_1/wirte', params)
export const api_read_mail = params => post('/Nebula_BH_No_1/read', params)