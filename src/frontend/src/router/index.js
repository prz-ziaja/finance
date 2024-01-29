import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import StartScraperView from '../views/StartScraperView.vue'
import StockItems from '../views/StockItems.vue'
import CompanyView from '../views/CompanyView.vue'

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
  {
    path: '/company',
    name: 'CompanyView',
    component: CompanyView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
