<template>
    <div>
        <h3>Total Price</h3>
        {{ invoiceStore.selected_invoice.total_amount }}
    </div>
    <div>
        <button @click="confirmPayment" class="btn btn-success">Pay</button>
    </div>
</template>


<script>
import { useInvoiceStore } from '@/stores/invoice';
import { onMounted } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const invoiceStore = useInvoiceStore();

        onMounted(() => {
            invoiceStore.fetchInvoices();
            invoiceStore.selectInvoice();
        });

        return { invoiceStore };
    },
    methods: {
        confirmPayment() {
            const invoiceStore = useInvoiceStore();

            const payload = {'invoice_id' : invoiceStore.invoice_id};
            console.log("Altering Invoice: ", payload);

            try {
                const response = axios.post('http://localhost:5000/finish_payment', payload);
                console.log(response.data);
            } catch (error) {
                console.error("Error sending invoice_id:", error)
            }
        },
    }
};
</script>
