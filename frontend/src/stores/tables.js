// stores/tables.js

import {defineStore} from 'pinia';
import axios from 'axios';

export const useTableStore = defineStore({
    id: 'table',
    state: () => ({
        tables: []
    }),
    actions: {
        fetchTables() {
            axios.get('http://localhost:5000/tables')
            .then(response => {
                this.tables = response.data.tables_list;
                console.log(this.tables)
            })
            .catch(error => {
                console.error('Error fetching tables:', error);
            });
        }
    },
    getters: {
        allTables() {
            return this.tables;
        },
    },
})