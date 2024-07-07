<template>

    <div class="w-full ">

        <!-- Recipe Name -->
        <div class="w-full  p-4 text-center">
            <div v-if="recipeData?.recipe_picture != null" class="flex item-center justify-center">
                <img :src="ImageUrl" alt="Pictures tbd" />
            </div>

            <div class="text-4xl p-4 font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl">
                {{ recipeData?.recipe_name }}
            </div>
        </div>



        <div class="flex flex-col md:flex-row md:flex-wrap text-center h-full">
            <!-- Description Column -->
            <div class="order-2 md:order-1 w-full md:w-4/5 p-4 ">
                <div v-html="recipeData?.description"></div>
            </div>



            <!-- Ingredients List Column -->
            <div class="order-1 md:order-2 w-full md:w-1/5 p-4 ">

                <!-- Buttons for portions -->
                <div class="flex items-center space-x-4 md:mb-4 mb-2 justify-center">

                    <button @click="decrease" class="btn">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                        </svg>
                    </button>


                    <input type="number" v-model.number="portions" @input="updatePortion"
                        class="w-16 text-center border rounded no-spinners" min="1" />

                    <button @click="increase" class="btn">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                        </svg>
                    </button>
                </div>




                <ul>
                    <li v-for="ingredient in recipeData?.ingredients" class="list-none">
                        <span v-if="ingredient?.quantity !== null"> 
                        {{ ingredient?.quantity * portions }} 
                    </span>
                    <span v-else>

                    </span>
                    {{ ingredient?.unit }} {{ ingredient?.ingredient }}
                    </li>
                </ul>
            </div>
        </div>
    </div>





</template>


<script>
import axios from 'axios';

export default {
    name: 'SingleRecipe',

    props: {
        recipeId: String,
    },

    data() {
        return {
            recipeData: [],
            ImageUrl: '',
            portions: 1
        }
    },

    mounted() {
        this.getRecipeData();
    },

    methods: {
        getRecipeData() {
            axios
                .get(`/api/recipes/${this.recipeId}`)
                .then(response => {
                    this.recipeData = response.data;
                    if (this.recipeData?.recipe_picture != null) {
                        this.buildImageUrl();
                    }
                })
                .catch(error => {
                    this.recipeData = 'No recipe found';
                    // console.log(error)
                });
        },

        buildImageUrl() {
            const serverIP = import.meta.env.VITE_DJANGO_ROUTER;
            this.ImageUrl = `${serverIP}${this.recipeData?.recipe_picture}`;
            // console.log(this.ImageUrl)
        },


        // for the counter
        increase() {
            this.portions++;
        },
        decrease() {
            if (this.portions > 1) {
                this.portions--;
            }
        },

        updatePortion() {
            if (this.portions < 0) {
                this.portions = 1;
            }
        },
    }
}


</script>

<style scoped>
.no-spinners::-webkit-outer-spin-button,
.no-spinners::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}
</style>