<template>
  <div class="container mt-4">
    <h2 class="mb-4">Edit Menu Item</h2>
    <form @submit.prevent="updateMenuItem">
      <div class="mb-3">
        <label for="name" class="form-label">Name:</label>
        <input v-model="formData.name" type="text" id="name" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="price" class="form-label">Price:</label>
        <input v-model="formData.price" type="number" id="price" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="category" class="form-label">Category ID:</label>
        <input v-model="formData.category_id" type="number" id="category" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="image" class="form-label">Image URL:</label>
        <input v-model="formData.image" type="text" id="image" class="form-control">
      </div>

      <button type="submit" class="btn btn-primary">Update</button>
    </form>

    <button @click="deleteMenuItem" class="btn btn-danger mt-3">Delete</button>
  </div>
</template>

<script>
import axios from 'axios';
import { useMenuStore } from '@/stores/menu';
import { onMounted } from 'vue';

export default {
  setup() {
    const menuStore = useMenuStore();

    // Call the actions when the component is mounted
    onMounted(() => {
      menuStore.fetchCategories();
      menuStore.fetchMenuItems();
    });
    return {
      menuStore,
    };
  },
  created() {
    console.log('test',this.menuStore)
  },
  data() {
    return {
      formData: {
        name: '',
        price: 0,
        category_id: 0,
        image: '',
      },
    };
  },
  async mounted() {
    await this.fetchMenuItem();
  },
  methods: {
    async fetchMenuItem() {
      try {
        const itemId = this.$route.params.id;
        const response = await axios.get(`http://localhost:5000/menu_items/${itemId}`);
        this.formData = response.data; // Assuming the API response is the entire menu item object
      } catch (error) {
        console.error('Error fetching menu item:', error);
      }
    },
    async updateMenuItem() {
      try {
        const itemId = this.$route.params.id;
        await axios.put(`http://localhost:5000/menu_items/${itemId}`, this.formData);
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
