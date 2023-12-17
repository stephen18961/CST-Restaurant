// stores/menu.js

// Import Pinia
import { defineStore } from 'pinia';
import axios from 'axios';

// Create a Pinia store
export const useMenuStore = defineStore({
  id: 'menu',
  state: () => ({
    menuItems: [],
    categories: [],
    selectedCategory: null,
    form: {
        id: null,
        name: '',
        price: 0,
        category_id: 0,
        // Add other fields as needed
      },
  }),
  actions: {
    fetchCategories() {
      axios.get('http://localhost:5000/categories')
        .then(response => {
          this.categories = response.data.categories;
        })
        .catch(error => {
          console.error('Error fetching categories:', error);
        });
    },
    fetchMenuItems() {
      axios.get('http://localhost:5000/menu_items')
        .then(response => {
          this.menuItems = response.data.menu_items;
          console.log('Menu Items:', this.menuItems);
        })
        .catch(error => {
          console.error('Error fetching menu items:', error);
        });
    },
    filterByCategory(categoryId) {
      this.selectedCategory = categoryId;
    },
    selectItem(itemId) {
        const selectedItem = this.menuItems.find(item => item.id === itemId);
      
        if (selectedItem) {
          this.form = { ...selectedItem };
        } else {
          console.error('Item not found');
        }
      },      
    async getMenuItem(itemId) {
        try {
          const response = await axios.get(`http://localhost:5000/menu_items/${itemId}`);
          this.selectedItem = response.data.item;
          return this.selectedItem;
        } catch (error) {
          console.error('Error fetching menu item:', error);
          throw error;
        }
      },
    async editItem(updatedItem) {
        try {
          const response = await axios.put(`http://localhost:5000/menu_items/${updatedItem.id}`, updatedItem);
          console.log('Item updated:', response.data);
          // Optionally, update the local store state if needed
          // this.menuItems = this.menuItems.map(item => (item.id === updatedItem.id ? updatedItem : item));
        } catch (error) {
          console.error('Error updating item:', error);
          throw error;
        }
      },
  },
  getters: {
    filteredMenuItems() {
      console.log('Selected Category:', this.selectedCategory);

      return this.selectedCategory
        ? this.menuItems.filter(item => item.category_id === this.selectedCategory)
        : this.menuItems;
    },
    selectedItemDetails() {
      return this.selectedItem;
    },
  },
});
