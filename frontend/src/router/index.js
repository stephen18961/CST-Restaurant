import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Hello from '@/components/Hello.vue'
import MenuItemList from '../components/MenuItemList.vue'
import MenuItemAdd from '../components/MenuItemAdd.vue'
import MenuItemEdit from '../components/MenuItemEdit.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { path: '/hello', name: 'hello', component: Hello },
  { path: '/menu', name: 'menu', component: MenuItemList },
  { path: '/add', name: 'add', component: MenuItemAdd },
  { path: '/menu_items/:id/edit', name: 'editMenuItem', component: MenuItemEdit },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router