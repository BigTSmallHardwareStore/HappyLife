/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
        'node_modules/preline/dist/*.js',
    ],
    theme: {
        extend: {
            fontFamily: {
              sans: ['PlayfairDisplay', 'sans-serif'],
            },
          },
    },
    plugins: [
      require('preline/plugin'),
    ],
}

