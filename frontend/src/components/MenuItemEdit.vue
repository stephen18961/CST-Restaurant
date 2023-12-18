<template>
  <div class="container mt-4">
    <h2 class="mb-4">Edit Menu Item</h2>
    <form @submit.prevent="updateMenuItem">
      <div class="mb-3">
        <label for="name" class="form-label">Name:</label>
        <input v-model="adminStore.editForm.name" type="text" id="name" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="price" class="form-label">Price:</label>
        <input v-model="adminStore.editForm.price" type="number" id="price" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="category" class="form-label">Category ID:</label>
        <input v-model="adminStore.editForm.category_id" type="number" id="category" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="image" class="form-label">Image URL:</label>
        <input v-model="adminStore.editForm.image" type="text" id="image" class="form-control">
      </div>

      <button type="submit" class="btn btn-primary" @click="updateMenuItem">Update</button>
    </form>

    <button @click="deleteMenuItem" class="btn btn-danger mt-3">Delete</button>
  </div>
</template>

<script>
import axios from 'axios';
import { useMenuStore } from '@/stores/menu';
import { onMounted } from 'vue';
import { useAdminStore } from '@/stores/admin';

export default {
  setup() {
    const menuStore = useMenuStore();
    const adminStore = useAdminStore();
    // Call the actions when the component is mounted
    onMounted(() => {
      menuStore.fetchCategories();
      menuStore.fetchMenuItems();
    });
    return {
      menuStore, adminStore
    };
  },
  methods: {
    async updateMenuItem() {
      try {
        const adminStore = useAdminStore();
        const itemId = adminStore.editForm.id;
        await axios.put(`http://localhost:5000/menu_items/${itemId}`, adminStore.editForm);
        console.log('Menu item updated successfully');
        // Optionally, you can navigate back to the menu list after a successful update
        this.$router.push({ name: 'menu' });
      } catch (error) {
        console.error('Error updating menu item:', error);
      }
    },
    async deleteMenuItem() {
      try {
        const itemId = this.$route.params.id;
        await axios.delete(`http://localhost:5000/menu_items/${itemId}`);
        console.log('Menu item deleted successfully');
        // Optionally, you can navigate back to the menu list after a successful delete
        this.$router.push({ name: 'menu' });
      } catch (error) {
        console.error('Error deleting menu item:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your component styles here */
</style>
