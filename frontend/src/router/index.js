import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MenuItemList from '../components/MenuItemList.vue'
import MenuItemAdd from '../components/MenuItemAdd.vue'
import MenuItemEdit from '../components/MenuItemEdit.vue'
import MenuOrder from '@/components/MenuOrder.vue'
import OrderList from '@/components/OrderList.vue'
import Payment from '@/components/Payment.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { path: '/menu', name: 'menu', component: MenuOrder },
  { path: '/add', name: 'add', component: MenuItemAdd },
  { path: '/menu_items/:id/edit', name: 'editMenuItem', component: MenuItemEdit },
  { path: '/orders', name: 'order', component:OrderList},
  { path: '/payment', name: 'payment', component:Payment},
  { path: '/admin', name: 'admin', component:MenuItemList},
  { path: '/edit/:id', name: 'editMenuItem', component:MenuItemEdit},
  { path: '/add', name: 'addMenuItem', component:MenuItemAdd },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router