<template>
    <div>
        <h2 class="text-uppercase">Invoice Details</h2>

        <table class="table">
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
                    <td>Rp {{ detail.menu_item.price }}</td>
                </tr>
            </tbody>
        </table>

        <div class="container"> 
            <button @click="toPayment" class="btn btn-success m-2" v-if="invoiceStore.current_status == 1">Payment </button>
            <button @click="cancel" class="btn btn-danger" v-if="invoiceStore.invoice_details.length != 0">Close Details</button>
        </div>
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
            console.log(invoiceStore.selected_invoice)
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
</style>