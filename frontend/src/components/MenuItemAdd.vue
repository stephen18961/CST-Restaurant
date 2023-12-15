<template>
  <div class="container mt-4">
    <h1 class="mb-4">Add Menu Item</h1>
    <form @submit.prevent="addMenuItem">
      <div class="mb-3">
        <label for="name" class="form-label">Name:</label>
        <input v-model="newMenuItem.name" id="name" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="price" class="form-label">Price:</label>
        <input v-model="newMenuItem.price" id="price" type="number" step="0.01" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="category" class="form-label">Category ID:</label>
        <input v-model="newMenuItem.category_id" id="category" type="number" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="image" class="form-label">Image:</label>
        <input v-model="newMenuItem.image" id="image" type="text" class="form-control">
      </div>

      <button type="submit" class="btn btn-primary">Add Menu Item</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newMenuItem: {
        name: '',
        price: 0,
        category_id: 0,
        image: '',
      },
    };
  },
  methods: {
    async addMenuItem() {
      try {
        // Make an HTTP request to add a new menu item to the backend
        const response = await axios.post('http://localhost:5000/menu_items', this.newMenuItem);

        // Clear the form after successful addition
        this.newMenuItem = {
          name: '',
          price: 0,
          category_id: 0,
          image: '',
        };

        // Redirect to the menu item list or perform other actions after successful addition
        this.$router.push('/menu-items');

        this.$router.go(-1)

        // Log the response from the backend (optional)
        console.log(response.data);
      } catch (error) {
        console.error('Error adding menu item:', error);
      }
    },
  },
};
</script>
