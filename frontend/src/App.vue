<script setup>
import Header from '@/components/Header.vue'
</script>

<template>
<div class="flex flex-col h-screen">

    <Header></Header>


    <main class="relative">
        <div class="max-w-[85rem] min-h-[40rem] mx-auto py-10 px-4 sm:px-6 lg:px-8 ">
            <RouterView />
        </div>

    </main>


    <footer class="mt-auto py-3  bg-neutral-800  inset-x-0 bottom-0">
        <div class="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8">
            Footer
        </div>
    </footer>

</div>

</template>



<script>
export default {
    name: 'App',

    components: {
        Header
    }
}
</script>
