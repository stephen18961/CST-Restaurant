<template>
    <div>
        <h2>Invoice</h2>
        <div v-for="col in invoiceStore.selected_invoice">
            {{col}}
        </div>
    </div>
    <div>
        <h2>Invoice Details</h2>
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
            invoiceStore.selectInvoice();
        });

        return { invoiceStore };
    },
};
</script>
