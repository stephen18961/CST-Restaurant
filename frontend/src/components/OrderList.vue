<template>
    <div class="container">
        <div class="">
            <h2 class="d-flex justify-content-start text-uppercase">Orders List</h2>
            <Tables></Tables>
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Table Number</th>
                    <th>Created At</th>
                    <th>Total Amount</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="invoice in invoiceStore.invoices" :key="invoice.id">
                    <td>{{ invoice.id }}</td>
                    <td>{{ invoice.table_number }}</td>
                    <td>{{ invoice.created_at }}</td>
                    <td>{{ invoice.total_amount }}</td>
                    <td v-if="invoice.status.status === 'Open'" class="fw-bolder status-open">{{ invoice.status.status }}</td>
                    <td v-else class="fw-bolder text-danger">{{ invoice.status.status }}</td>
                    <!-- <td>{{ invoice.status.status }}</td> -->
                    <td>
                        <button @click="invoiceStore.showInvoiceDetail(invoice.id, invoice.status.id)" class="btn" style="background-color: #FF8066; color: #FFF6F2">Details</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { useInvoiceStore } from '@/stores/invoice';
import axios from 'axios';
import { onMounted } from 'vue';

export default {
    setup() {
        const invoiceStore = useInvoiceStore();

        onMounted(() => {
            invoiceStore.fetchInvoices();
        });

        return { invoiceStore };
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

.status-open {
    color: #00C26E;
}
</style>