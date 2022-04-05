import { createRouter, createWebHistory } from 'vue-router'
import TracesView from '../views/TracesView.vue'

const routes = [
  {
    path: '/:experiment?',
    name: 'traces',
    component: TracesView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
