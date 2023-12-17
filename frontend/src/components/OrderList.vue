<template>
    <div>
        <h1>Orders List</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Table Number</th>
                    <th>Created At</th>
                    <th>Total Amount</th>
                    <th>Status ID</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="invoice in invoiceStore.invoices" :key="invoice.id">
                    <td>{{ invoice.id }}</td>
                    <td>{{ invoice.table_number }}</td>
                    <td>{{ invoice.created_at }}</td>
                    <td>{{ invoice.total_amount }}</td>
                    <td>{{ invoice.status_id }}</td>
                    <td><button @click="invoiceStore.showInvoiceDetail(invoice.id)" class="btn btn-success">Details</button></td>
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
