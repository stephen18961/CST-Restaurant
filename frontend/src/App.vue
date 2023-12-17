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
          <router-link to="/payment" class="icons mb-2"><img src="@/assets/payment.svg" alt="" id="icons"><p class="text-uppercase">Payment</p></router-link>
          <router-link to="/add" class="icons mb-2">Add</router-link>
        </nav>
      </div>
      <div class="col-7">
        <router-view/>
      </div>
      <div class="col-4" style="border-left:1px solid #ECEDED">
      <h4>#ORDER</h4>
      <div>
        Selected table: {{ orderStore.currentOpenOrder.table_id }}
        <hr>
        Orders:
        <table class="table">
          <tr>
            <th scope="col">ItemID</th>
            <th scope="col">Image</th>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Actions</th>
          </tr>
          <tr v-for="items in orderStore.orderedItems" class="border">
            <td>{{ items.id }}</td>
            <td><img :src="'http://localhost:5000/static/images/' + items.image" alt="Menu Item Image" class="img-fluid" style="height: 100px;"></td>
            <td>{{ items.name }}</td>
            <td>{{ items.price }}</td>
            <td><button @click="removeItem(items.id)" class="btn btn-danger btn-sm">Remove</button></td>
          </tr>
        </table>
        <hr>

        <button @click="postOrder" class="btn btn-success">Order</button>
        
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import { useOrderStore } from '@/stores/orders';
import { onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const orderStore = useOrderStore();

    return {orderStore}
  },
  methods: {
    getTableNumber(data) {
      this.selectedTable = data;
      console.log("Selected table: ", this.selectedTable)
    },
    removeItem(itemId) {
      const orderStore = useOrderStore();
      const index = orderStore.orderedItems.findIndex(items => items.id === itemId);
      if (index !== -1) {
        orderStore.orderedItems.splice(index, 1);
      }
    },
    async postOrder() {
  const orderStore = useOrderStore();

  // Check if orderedItems is empty
  if (orderStore.orderedItems.length === 0) {
    alert('Please add items to your order before placing it.');
    return;
  }

  try {
    let total_price = 0;
    for (const item of orderStore.orderedItems) {
      total_price += item.price;
    }

    const invoiceData = {
      table_number: orderStore.currentOpenOrder.table_id,
      created_at: null,
      total_amount: total_price,
      status_id: 1,
    };

    const invoiceDetailData = [];
    for (const item of orderStore.orderedItems) {
      invoiceDetailData.push({
        invoice_id: null,
        menu_item_id: item.id,
      });
    }

    const orderData = {
      invoiceData,
      invoiceDetailData,
    };

    const response = await axios.post('http://localhost:5000/order', orderData);

    console.log('Order placed', response.data);

    // Optionally, you can clear the orderedItems array after successful orders
    orderStore.clearOrderedItems();
  } catch (error) {
    console.error('Error posting order:', error);
    // Handle the error as needed
  }
}

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
