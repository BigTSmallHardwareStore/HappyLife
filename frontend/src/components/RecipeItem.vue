<script setup>

</script>

<template>
    <div class="recipe-card">
        <RouterLink :to="{ name: 'single_recipe', params: { recipeId: recipe?.url_name } }" class="recipe_title">
            {{recipe?.recipe_name }}
        </RouterLink>
    </div>
</template>


<script>
export default {
    name: 'RecipeItem',

    props: {
        recipe: Object
    },




}
</script>


<style scoped>
.recipe-card {
    @apply bg-white border border-gray-300 rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow duration-300 ease-in-out;
}

.recipe-title {
    @apply text-lg font-semibold text-gray-800;
}
</style>