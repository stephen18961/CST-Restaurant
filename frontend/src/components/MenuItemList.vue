<template>
  <div>
    <h1 class="mt-4 mb-3">Menu Items</h1>
    <div v-for="item in menuItems" :key="item.id" class="card mb-3">
      <router-link :to="{ name: 'editMenuItem', params: { id: item.id } }" class="text-decoration-none">
        <!-- Link to the edit page with the item's ID -->
        <div class="row g-0">
          <div class="col-md-4">
            <img :src="item.image" alt="Menu Item Image" class="img-fluid" style="height: 100px;">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ item.name }}</h5>
              <p class="card-text">Price: Rp{{ item.price }},00</p>
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      menuItems: [],
    };
  },
  mounted() {
    this.fetchMenuItems();
  },
  methods: {
    fetchMenuItems() {
      axios.get('http://localhost:5000/menu_items')
        .then(response => {
          this.menuItems = response.data.menu_items;
        })
        .catch(error => {
          console.error('Error fetching menu items:', error);
        });
    },
  },
};
</script>

<style scoped>
/* Add your component styles here */
/* You can add additional custom styles here if needed */
</style>
