import { createRouter, createWebHistory } from 'vue-router'
import TracesView from '../views/TracesView.vue'

const routes = [
  {
    path: '/',
    redirect: '/traces'
  },
  {
    path: '/traces/:experiment?',
    name: 'traces',
    component: TracesView
  },
  {
    path: '/traces',
    name: 'home',
    component: TracesView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
