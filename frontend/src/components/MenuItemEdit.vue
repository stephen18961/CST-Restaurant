<template>
  <form @submit.prevent="editItem">
    <label>Name:</label>
    <input v-model="form.name" />

    <label>Price:</label>
    <input v-model="form.price" />

    <!-- Add other form fields as needed -->

    <button type="submit">Edit Item</button>
  </form>
</template>

<script>
import { useMenuStore } from '@/stores/menu';

export default {
  setup() {
    const menuStore = useMenuStore();
    this.menuStore = menuStore;
  },
  data() {
    return {
      // Assuming useMenuStore is the store instance
      form: this.menuStore.form,
    };
  },
  methods: {
    editItem() {
      // Call the store action to edit the item using this.form
      this.useMenuStore.editItem(this.form);

      // Optionally, reset the form after editing
      this.resetForm();
    },
    resetForm() {
      // Reset form fields as needed
      this.form = {
        id: null,
        name: '',
        price: 0,
        // Reset other fields as needed
      };
    },
  },
};
</script>
