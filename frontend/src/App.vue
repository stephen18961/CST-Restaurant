<template>
  <div class="container app">

    <div class="row">
      <div class="col-1">
        <nav class="d-flex flex-column">
          <router-link to="/">Home</router-link>
          <router-link to="/menu">Menu</router-link>
          <router-link to="/add">Add</router-link>
        </nav>
      </div>
      <div class="col-7">
        <router-view/>
      </div>
      <div class="col-4 border">
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
            <th scope="col"></th>
          </tr>
          <tr v-for="items in orderStore.orderedItems" class="border">
            <td>{{ items.id }}</td>
            <td><img :src="'http://localhost:5000/static/images/' + items.image" alt="Menu Item Image" class="img-fluid" style="height: 100px;"></td>
            <td>{{ items.name }}</td>
            <td>{{ items.price }}</td>
            <td></td>
          </tr>
        </table>
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

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

router-link {
  display: block;
}
</style>
