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
            
        },
    }
};
</script>
