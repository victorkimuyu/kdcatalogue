/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["catalogue/**/*.html"],
  theme: {
    extend: {
        fontFamily: {
            sans: ['Inter var', 'sans-serif'],
            title: ['Assistant', 'sans-serif'],
        }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}