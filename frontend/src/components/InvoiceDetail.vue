<template>
    <div>
        <h1>Invoice Details</h1>

        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Invoice ID</th>
                    <th>Menu Item ID</th>
                    <!-- Add other fields as needed -->
                </tr>
            </thead>
            <tbody>
                <tr v-for="detail in invoiceStore.invoice_details" :key="detail.id">
                    <td>{{ detail.id }}</td>
                    <td>{{ detail.invoice_id }}</td>
                    <td>{{ detail.menu_item_id }}</td>
                    <!-- Add other fields as needed -->
                </tr>
            </tbody>
        </table>

        <button @click="toPayment" class="btn btn-success" v-if="invoiceStore.invoice_details != {}">Payment</button>
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
    methods: {
        toPayment() {
            const invoiceStore = useInvoiceStore();
            const invoice_id = invoiceStore.invoice_details[0].invoice_id;
            invoiceStore.invoice_id = invoice_id;
            this.$router.push('/payment')
        }
    }
};
</script>
