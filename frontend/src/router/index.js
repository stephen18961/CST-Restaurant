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
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
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