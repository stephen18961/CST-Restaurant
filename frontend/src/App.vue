<template>
  <header>
    <div class="d-flex mb-3">
      <div class="me-auto p-2"><a class="fw-bolder fs-4" href="#" style="color: #3A001E; margin-left: 25px;">CST Restaurant</a></div>
    </div>
  </header>
  <div class="container app">

    <div class="row">
      <div class="col-1 left-side">
        <nav class="d-flex flex-column fw-medium align-items-center justify-content-center ">
          <router-link to="/" class="icons mb-2"><img src="@/assets/home.svg" alt=""><p class="text-uppercase">Home</p></router-link>
          <router-link to="/menu" class="icons mb-2"><img src="@/assets/menu.svg" alt="" id="icons"><p class="text-uppercase">Menu</p></router-link>
          <router-link to="/orders" class="icons mb-2"><img src="@/assets/orders.svg" alt="" id="icons"><p class="text-uppercase">orders</p></router-link>
          <!-- <router-link to="/payment" class="icons mb-2"><img src="@/assets/payment.svg" alt="" id="icons"><p class="text-uppercase">Payment</p></router-link> -->
          <div v-if="currentRoute === '/payment'" class="icons mb-2 router-link-exact-active"><img src="@/assets/payment.svg" alt="" id="icons"><p class="text-uppercase">Payment</p></div>
          <div v-else class="icons mb-2"><img src="@/assets/payment.svg" alt="" id="icons"><p class="text-uppercase">Payment</p></div>
          <router-link to="/admin" class="icons mb-2">Admin</router-link>
        </nav>
      </div>
      <div class="col-7">
        <!-- Router view here --> 
        <router-view/>
      </div>
      <div class="col-4" style="border-left:1px solid #ECEDED">
      
      <div>
        <div class="me-auto p-3" style="border-bottom: 1px solid #ECEDED;">
          <span v-if="currentRoute === '/'" class="fs-2 text-black text-uppercase">Selected Table: {{ orderStore.currentOpenOrder.table_id }}</span>
          <span v-if="currentRoute === '/menu'" class="fs-2 text-black text-uppercase">Selected Table: {{ orderStore.currentOpenOrder.table_id }}</span>
        </div>

        <CurrentOrder v-if="currentRoute === '/menu'"></CurrentOrder>
        <!-- <OrderDetails v-if="currentRoute ==='/orders' "></OrderDetails> -->
        <InvoiceDetail v-if="currentRoute === '/orders'"></InvoiceDetail>
        <PaymentRight v-if="currentRoute === '/payment'"></PaymentRight>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import { useOrderStore } from '@/stores/orders';
import { onMounted } from 'vue';
import CurrentOrder from '@/components/CurrentOrder.vue'
import axios from 'axios';
import InvoiceDetail from './components/InvoiceDetail.vue';
import PaymentRight from './components/PaymentRight.vue';

export default {
  data() {
    return {
      currentRoute: this.$route.path
    }
  },
  components: {
    // Payment
    CurrentOrder,
    InvoiceDetail,
    PaymentRight
  },
  setup() {
    const orderStore = useOrderStore();

    return {orderStore}
  },
  methods: {
    getTableNumber(data) {
      this.selectedTable = data;
      console.log("Selected table: ", this.selectedTable)
    },
  },
  watch: {
    '$route'(to, from) {
      // Update the currentRoute whenever the route changes
      this.currentRoute = to.path;
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
}

.app {
  max-width: 100% !important;
}

header {
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

header a {
  color: #3A001E;
  text-decoration: none;
}

nav {
  padding: 30px;
}

nav a {
  color: #3A001E;
  text-decoration: none;
}

router-link {
  display: block;
}

.icons {
  filter: grayscale(100%); 
  opacity: 0.45;
}

.icons:hover {
  filter: grayscale(0%);
  opacity: 1;
}

.router-link-exact-active {
  filter: grayscale(0%);
  opacity: 1;
}

.left-side {
  border-right: 1px solid #ECEDED;
}

</style>
