// stores/invoice.js

import {defineStore} from 'pinia';
import axios from 'axios';

export const useInvoiceStore = defineStore({
    id: 'invoice',
    state: () => ({
        invoices: {},
        invoice_details: {},
        invoice_id: null,
        selected_invoice: {},
        current_status: null,
    }),
    actions: {
        fetchInvoices() {
            axios.get('http://localhost:5000/invoices')
              .then(response => {
                this.invoices = response.data.invoices;
              })
              .catch(error => {
                console.error('Error fetching invoices:', error);
              });
        },
        showInvoiceDetail(invoice_id, invoice_status) {
            axios.get(`http://localhost:5000/invoices/${invoice_id}/details`)
              .then(response => {
                this.invoice_details = response.data.invoice_details;
                this.current_status = invoice_status;
                console.log(this.invoice_details)
              })
              .catch(error => {
                console.error('Error fetching invoices:', error);
              });
        },
        selectInvoice() {
            axios.get(`http://localhost:5000/invoices/${this.invoice_id}`)
              .then(response => {
                this.selected_invoice = response.data.invoice
              })
              .catch(error => {
                console.error('Error fetching invoice:', error)
              });
        }
    }
})