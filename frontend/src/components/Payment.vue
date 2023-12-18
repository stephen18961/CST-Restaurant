<template>
    <div class="container mt-4">
      <!-- Invoice Section -->
      <div>
        <h2>Invoice</h2>
        <div v-for="col in invoiceStore.selected_invoice" :key="col">
          {{ col }}
        </div>
      </div>
  
      <!-- Invoice Details Section -->
      <div class="mt-4">
        <h2>Invoice Details</h2>
        <table class="table table-bordered">
          <thead class="thead-dark">
            <tr>
              <th>ID</th>
              <th>Invoice ID</th>
              <th>Menu Item ID</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="detail in invoiceStore.invoice_details" :key="detail.id">
              <td>{{ detail.id }}</td>
              <td>{{ detail.invoice_id }}</td>
              <td>{{ detail.menu_item.name }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <button class="btn btn-danger mt-4" @click="cancel">Cancel</button>
    </div>
  </template>
  
  <script>
  import { useInvoiceStore } from "@/stores/invoice";
  import { onMounted } from "vue";
  
  export default {
    setup() {
      const invoiceStore = useInvoiceStore();
  
      onMounted(() => {

      });

      return { invoiceStore };
    },
    methods: {
        cancel() {
            this.invoiceStore.selected_invoice = {};
            this.invoiceStore.invoice_details = {};
            this.$router.push('/orders')
        }
    }
  };
  </script>
  