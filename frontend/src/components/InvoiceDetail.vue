<template>
    <div>
        <h1>Invoice Details</h1>

        <table>
            <thead>
                <tr>
                    <th>Invoice ID</th>
                    <th>Menu Item</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="detail in invoiceStore.invoice_details" :key="detail.id">
                    <td>{{ detail.invoice_id }}</td>
                    <td>{{ detail.menu_item.name }}</td>
                    <td>{{ detail.menu_item.price }}</td>
                </tr>
            </tbody>
        </table>

        <button @click="toPayment" class="btn btn-success" v-if="invoiceStore.invoice_details.length != 0">Payment</button>
        <button @click="cancel" class="btn btn-danger" v-if="invoiceStore.invoice_details.length != 0">Close Details</button>
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
            invoiceStore.fetchInvoices();
            invoiceStore.selectInvoice();
        },
        cancel() {
            this.invoiceStore.invoice_details = [];
        }
    }
};
</script>
