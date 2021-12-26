import {
  createRouter,
  createWebHashHistory
} from 'vue-router'

const routes = [{
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/read',
    name: 'Read',
    component: () => import('../views/Read.vue')
  },
  {
    path: '/write',
    name: 'Write',
    component: () => import('../views/Write.vue'),
    meta: {
      title: "写一封信给你爱的人吧！",
      keepAlive: true // 需要被缓存
    }
  },
  {
    path: '/read_my_story',
    name: 'Read_my_story',
    component: () => import('../views/Read_my_story.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})
export default router