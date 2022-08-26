/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["catalogue/**/*.html"],
  theme: {
    extend: {
        fontFamily: {
            sans: ['Inter', 'sans-serif'],
        }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}