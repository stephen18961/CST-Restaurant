// stores/orders.js

import {defineStore} from 'pinia';
import axios from 'axios';

export const useOrderStore = defineStore({
    id: 'order',
    state: () => ({
        currentOpenOrder: {
            table_id : null,

        },
        orders: []
    }),

})