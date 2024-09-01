/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}", // adjust these paths to your actual files
    "./public/**/*.{html,js}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'computer': ['Retro Computer', 'sans-serif'],
      },
    },
  },
  plugins: [],
}