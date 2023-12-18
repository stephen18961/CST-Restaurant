<template>
    <h4>#ORDER</h4>

    Orders:
    <table class="table">
        <tr>
        <th scope="col">ItemID</th>
        <th scope="col">Image</th>
        <th scope="col">Name</th>
        <th scope="col">Price</th>
        <th scope="col">Actions</th>
        </tr>
        <tr v-for="items in orderStore.orderedItems" class="border">
        <td>{{ items.id }}</td>
        <td><img :src="'http://localhost:5000/static/images/' + items.image" alt="Menu Item Image" class="img-fluid" style="height: 100px;"></td>
        <td>{{ items.name }}</td>
        <td>{{ items.price }}</td>
        <td><button @click="removeItem(items.id)" class="btn btn-danger btn-sm">Remove</button></td>
        </tr>
    </table>

    <hr>

    <button @click="postOrder" class="btn btn-success">Order</button>
</template>

<script>
import { useOrderStore } from '@/stores/orders';
import axios from 'axios';

export default {
    setup() {
    const orderStore = useOrderStore();

    return {orderStore}
  },
  methods: {
    removeItem(itemId) {
      const orderStore = useOrderStore();
      const index = orderStore.orderedItems.findIndex(items => items.id === itemId);
      if (index !== -1) {
        orderStore.orderedItems.splice(index, 1);
      }
    },
    async postOrder() {
      const orderStore = useOrderStore();

      // Check if no table is selected
      if (orderStore.currentOpenOrder.table_id === null) {
        alert('Please select a table before placing the order.');
        return;
      }

      // Check if orderedItems is empty
      if (orderStore.orderedItems.length === 0) {
        alert('Please add items to your order before placing it.');
        return;
      }

      try {
        let total_price = 0;
        for (const item of orderStore.orderedItems) {
          total_price += item.price;
        }

        const invoiceData = {
          table_number: orderStore.currentOpenOrder.table_id,
          created_at: null,
          total_amount: total_price,
          status_id: 1,
        };

        const invoiceDetailData = [];
        for (const item of orderStore.orderedItems) {
          invoiceDetailData.push({
            invoice_id: null,
            menu_item_id: item.id,
          });
        }

        const orderData = {
          invoiceData,
          invoiceDetailData,
        };

        const response = await axios.post('http://localhost:5000/order', orderData);

        console.log('Order placed', response.data);

        // Optionally, you can clear the orderedItems array after successful orders
        orderStore.clearOrderedItems();

        this.$router.push('/')
      } catch (error) {
        console.error('Error posting order:', error);
        // Handle the error as needed
      }
  }
  }
}  
</script>