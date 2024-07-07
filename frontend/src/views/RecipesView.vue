<script setup>
import RecipeItem from '@/components/RecipeItem.vue'
</script>

<template>
    <main class="w-full">

        <!-- Search Bar -->
        <input type="text" v-model="searchQuery" @input="filterRecipes" placeholder="Search recipes by name..."
            class="md:w-1/2 w-full mb-4 p-2 border rounded" />


        <!-- Categories Buttons -->
        <div class="mb-4">
            <button v-for="category in category_list" @click="toggleCategory(category)" :class="[
                'mr-2 mb-2 py-2 px-4 text-center no-underline inline-block text-sm cursor-pointer rounded',
                selectedCategories.includes(category) ? 'bg-green-600 text-white border-none' : 'bg-gray-100 text-black border border-gray-300 hover:bg-gray-300'
            ]" class="mr-2 mb-2">
                {{ category }}
            </button>
        </div>



        <!-- Recipes List -->
        <div class="recipe-overview">
            <RecipeItem v-for="recipe in filteredRecipes" :recipe="recipe" />
        </div>



    </main>
</template>



<script>
import axios from 'axios'

export default {
    name: 'RecipesView',

    components: {
        RecipeItem
    },

    data() {
        return {
            recipes_list: [],
            filteredRecipes: [],
            searchQuery: "",
            category_list: [],
            selectedCategories: [],
        }
    },

    created() {
        this.getAllRecipesAndCategories()
    },

    methods: {
        getAllRecipesAndCategories() {
            axios
                .get('/api/recipes/')
                .then(response => {
                    this.recipes_list = response.data.recipes;
                    this.category_list = response.data.categories.map(category => category.category_name );
                    this.filteredRecipes = [...this.recipes_list]; // Initialize filtered recipes with all recipes
                })
                .catch(error => {
                    this.recipes_list = []
                });
        },

        filterRecipes() {
            let recipes = [...this.recipes_list];

            if (this.searchQuery.trim() !== "") {
                const lowercaseQuery = this.searchQuery.trim().toLowerCase();
                recipes = recipes.filter(recipe => recipe.recipe_name.toLowerCase().includes(lowercaseQuery));
            }

            if (this.selectedCategories.length > 0) {
                recipes = recipes.filter(recipe =>
                    this.selectedCategories.includes(recipe.category)
                );
            }

            this.filteredRecipes = recipes;
        },


        toggleCategory(category) {
            const index = this.selectedCategories.indexOf(category);
            if (index === -1) {
                this.selectedCategories.push(category);
            } else {
                this.selectedCategories.splice(index, 1);
            }
            this.filterRecipes();
        }





    }

}



</script>


<style scoped>
main {
    text-align: center;
}

li {
    list-style-type: none;
}

.recipe_container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;

    padding: 10px;
    gap: 10px;
    border-width: 2px;
    
}

.recipe-overview {
  @apply grid grid-cols-1 gap-4 p-4 md:grid-cols-2 lg:grid-cols-3;
}




</style>