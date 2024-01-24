import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import StartScraperView from '../views/StartScraperView.vue'
import StockItems from '../views/StockItems.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/scraper',
    name: 'scraper',
    component: StartScraperView
  },
  {
    path: '/stock/items',
    name: 'StockItems',
    component: StockItems
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
