<!-- menuComponent.vue -->
<template>
    <div>
      <h1>Menu Items</h1>
      <div v-for="item in menuItems" :key="item.id">
        <img :src="item.image" alt="Menu Item Image" style="width: 100px; height: 100px;">
        <p>{{ item.name }}</p>
        <p>Price: Rp{{ item.price }},00</p>
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
        axios.get('http://localhost:5000/menu_items') // Replace with your Flask API endpoint
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
  </style>
  