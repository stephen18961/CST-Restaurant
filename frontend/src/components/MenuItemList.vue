<!-- MenuItemList.vue -->

<template>
  <div>
    <h1 class="mt-4 mb-3">Menu Items</h1>

    <div class="container flex">
      <!-- Buttons for filtering by category -->
      <button
        @click="menuStore.filterByCategory(null)"
        :class="{ 'btn btn-secondary mx-1': menuStore.selectedCategory !== null, 'btn btn-primary mx-1': menuStore.selectedCategory === null }"
      >
        All
      </button>
      <button
        v-for="category in menuStore.categories"
        :key="category.id"
        @click="menuStore.filterByCategory(category.category_id)"
        :class="{ 'btn btn-secondary mx-1': menuStore.selectedCategory !== category.category_id, 'btn btn-primary mx-1': menuStore.selectedCategory === category.category_id }"
      >
        {{ category.name }}
      </button>
    </div>

<!-- Menu Display as Table -->
<table class="table">
  <thead>
    <tr>
      <th scope="col">Image</th>
      <th scope="col">Name</th>
      <th scope="col">Price</th>
      <th scope="col">Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="item in menuStore.filteredMenuItems" :key="item.id">
      <td>
        <img :src="'http://localhost:5000/static/images/' + item.image" alt="Menu Item Image" class="img-fluid" style="height: 100px;">
      </td>
      <td>{{ item.name }}</td>
      <td>Rp{{ item.price }},00</td>
      <td>
        <button @click="" class="btn btn-success">
              Update
        </button>
      </td>
    </tr>
  </tbody>
</table>

<!-- <div>
      <h1>Menu Items</h1>
      <ul>
        <li v-for="item in menuStore.filteredMenuItems" :key="item.id">
          <img :src="'http://localhost:5000/static/images/' + item.image" alt="Menu Item Image" class="img-fluid" style="height: 100px;">
          {{ item.name }} - {{ item.price }}
          <router-link :to="{ name: 'editMenuItem', params: { id: item.id }}">Edit</router-link>
          <button @click="deleteMenuItem(item.id)">Delete</button>
        </li>
      </ul>
</div> -->


  </div>
</template>

<script>
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
};
</script>

<style scoped>
/* Add your component styles here */
/* You can add additional custom styles here if needed */
</style>
