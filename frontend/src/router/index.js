import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MenuItemList from '../components/MenuItemList.vue'
import MenuItemAdd from '../components/MenuItemAdd.vue'
import MenuItemEdit from '../components/MenuItemEdit.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { path: '/menu', name: 'menu', component: MenuItemList },
  { path: '/add', name: 'add', component: MenuItemAdd },
  { path: '/menu_items/:id/edit', name: 'editMenuItem', component: MenuItemEdit },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router