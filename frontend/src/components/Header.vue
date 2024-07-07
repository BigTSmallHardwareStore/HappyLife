<template>
    <header
        class=">flex flex-wrap sm:justify-start sm:flex-nowrap w-full  text-sm py-4 bg-neutral-800 sticky top-0 z-50 ">

        <nav class="max-w-[85rem] w-full mx-auto px-4 sm:flex sm:items-center sm:justify-between" aria-label="Global">
            <div class="flex items-center justify-between">
                <RouterLink :to="{ 'name': 'home' }" class="flex-none text-xl font-semibold text-white hover:text-green-700">
                    Happy Life
                </RouterLink>



                <div class="sm:hidden">
                    <button type="button"
                        class="hs-collapse-toggle p-2 inline-flex justify-center items-center gap-x-2 rounded-lg border   shadow-sm  disabled:opacity-50 disabled:pointer-events-none bg-transparent border-neutral-700 text-white hover:bg-white/10"
                        data-hs-collapse="#navbar-collapse-with-animation"
                        aria-controls="navbar-collapse-with-animation" aria-label="Toggle navigation">
                        <svg class="hs-collapse-open:hidden flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg"
                            width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="3" x2="21" y1="6" y2="6" />
                            <line x1="3" x2="21" y1="12" y2="12" />
                            <line x1="3" x2="21" y1="18" y2="18" />
                        </svg>
                        <svg class="hs-collapse-open:block hidden flex-shrink-0 size-4"
                            xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 6 6 18" />
                            <path d="m6 6 12 12" />
                        </svg>
                    </button>
                </div>


            </div>




            <div id="navbar-collapse-with-animation"
                class="hs-collapse hidden overflow-hidden transition-all duration-300 basis-full grow sm:block">
                <div class="flex flex-col gap-5 mt-5 sm:flex-row sm:items-center sm:justify-end sm:mt-0 sm:ps-5 ">
                    <RouterLink :to="{ 'name': 'recipes' }"
                        class="font-medium   text-neutral-400 hover:text-neutral-500 menuItem-active-link">
                        Rezepte</RouterLink>


                    <a class="font-medium  text-neutral-400 hover:text-neutral-500 menuItem-active-link"
                        href="#">Account</a>
                    <a class="font-medium  text-neutral-400 hover:text-neutral-500 menuItem-active-link"
                        href="#">Work</a>
                    <a class="font-medium  text-neutral-400 hover:text-neutral-500 menuItem-active-link"
                        href="#">Blog</a>


                </div>
            </div>


        </nav>
    </header>
</template>

<script>
export default {
    name: 'Header',
}

</script>


<style scoped>
.router-link-exact-active.menuItem-active-link {
    /* border-bottom-color: #F19238; 
    color:#F19238*/
    --tw-text-opacity: 1;
    color: rgb(21 128 61 / var(--tw-text-opacity));
}
</style>
