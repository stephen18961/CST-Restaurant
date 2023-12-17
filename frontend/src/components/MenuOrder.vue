<template>
    <div class="row">
    <div class="">
      <h2 class="d-flex justify-content-start text-uppercase">Menu List</h2>
      <Tables></Tables>
    </div>
  </div>

  <div class="container d-flex align-items-start">
  <!-- Button for 'All' category -->
  <button
    @click="menuStore.filterByCategory(null)"
    :class="{ 'btn btn-secondary mx-1': menuStore.selectedCategory !== null, 'btn btn-custom mx-1': menuStore.selectedCategory === null }"
  >
    All
  </button>

  <!-- Buttons for other categories -->
  <button
    v-for="category in menuStore.categories"
    :key="category.id"
    @click="menuStore.filterByCategory(category.category_id)"
    :class="{ 'btn btn-secondary mx-1': menuStore.selectedCategory !== category.category_id, 'btn btn-custom mx-1': menuStore.selectedCategory === category.category_id }"
  >
    {{ category.name }}
  </button>
</div>

    <!-- Menu Display as Table -->
    <table class="table" style="margin-top: 2%;">
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
            <button @click="addItemToOrder(item)" class="btn" style="background-color: #FF8066; color: #FFF6F2">
                Add
            </button>
        </td>
        </tr>
    </tbody>
    </table>
</template>

<script>
import { useMenuStore } from '@/stores/menu';
import { useOrderStore } from '@/stores/orders';
import { onMounted } from 'vue';

export default {
    setup() {
        const menuStore = useMenuStore();

        onMounted(() => {
            menuStore.fetchCategories();
            menuStore.fetchMenuItems();
        });
    
        return {
            menuStore,
        }
    },
    methods: {
        addItemToOrder(item) {
            const menuStore = useOrderStore();

            // console.log(item.id);
            menuStore.addItemToOrder(item);
        }
    }
}
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
