<template>
    <div class="container">
        <div class="row">
            <div v-for="table in tableStore.tables" class="col-3 my-2">
                <button v-on:click="openOrder(table.table_id)" class="btn btn-light">
                    <div>
                        <span class="table-no">
                            {{ table.table_id }}
                        </span>
                        <div>
                            <img v-if="table.occupied === false" src="@/assets/table_0.png" alt="t empty">
                            <img v-if="table.occupied === true" src="@/assets/table_1.png" alt="t used">
                        </div>
                    </div>
                </button>
            </div>
        </div>
    </div>
</template>


<script>
import { useTableStore } from '@/stores/tables';
import { useOrderStore } from '@/stores/orders';
import { onMounted } from 'vue';
import axios from 'axios'

export default {
  name: 'Tables',
  setup() {
    const tableStore = useTableStore();
    const orderStore = useOrderStore();

    onMounted(() => {
        tableStore.fetchTables();
    });

    return {tableStore, orderStore}
  },
  methods: {
    openOrder(table_id) {
        console.log("Opening order from table ", table_id);
        // send data to pinia
        this.orderStore.currentOpenOrder.table_id = table_id;
        this.$router.push('/menu');
    }
  }
}
</script>

<style scoped>
    button {
        display: inline; background: none; border: none; margin: 0; padding: 0; font: inherit; cursor: pointer; outline: inherit;
    }
    span.table-no {
        display: block;
        position: relative;
        top: 92px;
        left: -1px;
    }
</style>