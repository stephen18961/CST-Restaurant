<template>
  <div class="row">
    <div class="col-8">
      <h2>Table List</h2>
      <Tables @send-data="getTableNumber"></Tables>
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
  methods: {
    getTableNumber(data) {
      this.selectedTable = data;
      console.log("Selected table: ", this.selectedTable)
    }
  }
};
</script>
