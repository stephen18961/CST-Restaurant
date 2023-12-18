<!-- MenuItemList.vue -->

<template>
  <div>
    <h2 class="d-flex justify-content-start text-uppercase">Menu Items</h2>

    <div class="container d-flex mb-3">
      <div class="me-auto p-2">
        <!-- Buttons for filtering by category -->
      <button
        @click="menuStore.filterByCategory(null)"
        :class="{ 'btn btn-secondary mx-1': menuStore.selectedCategory !== null, 'btn btn-custom mx-1': menuStore.selectedCategory === null }"
      >
        All
      </button>
      <button
        v-for="category in menuStore.categories"
        :key="category.id"
        @click="menuStore.filterByCategory(category.category_id)"
        :class="{ 'btn btn-secondary mx-1': menuStore.selectedCategory !== category.category_id, 'btn btn-custom mx-1': menuStore.selectedCategory === category.category_id }"
      >
        {{ category.name }}
      </button>
      </div>
      <div class="p-2">
        <button @click="goToAddMenuItem" class="btn mx-1 btn-primary">Add Menu Item</button>
      </div>
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
      <td>Rp {{ item.price }}</td>
      <td>
        <button @click="updateMenuItem(item.id)" class="btn btn-success">
          Update
        </button>
      </td>
    </tr>
  </tbody>
</table>
</div>
</template>

<script>
import { useMenuStore } from '@/stores/menu';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const menuStore = useMenuStore();
    const router = useRouter();

    // Call the actions when the component is mounted
    onMounted(() => {
      menuStore.fetchCategories();
      menuStore.fetchMenuItems();
    });
    // Function to handle the update button click
    const updateMenuItem = (itemId) => {
      // Navigate to MenuItemEdit.vue with the item ID as a parameter
      router.push({ name: 'editMenuItem', params: { id: itemId } });
    };

    const goToAddMenuItem = () => {
      router.push({ name: 'addMenuItem' });
    };

    return {
      menuStore,
      updateMenuItem,
      goToAddMenuItem,
    };
  },
};
</script>

<style scoped>
* {
  color: black;
}

h2 {
  border-bottom: 1px solid #ECEDED;
  margin: 2%;
  padding-bottom: 3%;
}

.btn-custom {
  background-color: #FF8066;
  color: #FFF6F2;
}
</style>