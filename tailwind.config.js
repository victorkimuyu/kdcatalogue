/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["catalogue/**/*.html"],
  theme: {
    extend: {
        fontFamily: {
            sans: ['Fira Sans', 'sans-serif'],
        }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}