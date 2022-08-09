/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["catalogue/templates/catalogue/*.html"],
  theme: {
    extend: {
        fontFamily: {
            sans: ['Inter var', 'sans-serif'],
        }
    },
  },
  plugins: [],
}
