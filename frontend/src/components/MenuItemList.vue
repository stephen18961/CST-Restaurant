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

    <!-- Menu Display -->
    <div v-for="item in menuStore.filteredMenuItems" :key="item.id" class="card mb-3">
      <router-link :to="{ name: 'editMenuItem', params: { id: item.id } }" class="text-decoration-none">
        <!-- Link to the edit page with the item's ID -->
        <div class="row g-0">
          <div class="col-md-4">
            <img :src="'http://localhost:5000/static/images/' + item.image" alt="Menu Item Image" class="img-fluid" style="height: 100px;">
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
