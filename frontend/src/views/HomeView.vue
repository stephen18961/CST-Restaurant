<template>
  <div class="row">
    <div class="">
      <h2 class="d-flex justify-content-start text-uppercase">Table List</h2>
      <Tables></Tables>
    </div>
  </div>

</template>

<script>
import { useMenuStore } from '@/stores/menu';
import { onMounted } from 'vue';
import Tables from '@/components/Tables.vue'

export default {
  data(){
    return {
      selectedTable : null,
    }
  },
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
  components: {
    Tables,
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
</style>