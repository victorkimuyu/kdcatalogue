/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["catalogue/**/*.html"],
  theme: {
    extend: {
        fontFamily: {
            sans: ['Libre Franklin', 'sans-serif'],
            title: ['Assistant', 'sans-serif'],
        }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}