// stores/admin.js

import {defineStore} from 'pinia';

export const useAdminStore = defineStore({
    id: 'admin',
    state: () => ({
        editForm: {}
    }),
})