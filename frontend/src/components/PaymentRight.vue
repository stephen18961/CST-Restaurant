<template>
    <div>
        <h2 class="text-uppercase text-black">Total Price</h2>
        <h3>Total: Rp {{ invoiceStore.selected_invoice.total_amount }}</h3>
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
                // Display alert for 2 seconds
                alert("Payment successful");
                this.$router.push('/');        
            } catch (error) {
                console.error("Error sending invoice_id:", error)
            }
        },
    }
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
</style>