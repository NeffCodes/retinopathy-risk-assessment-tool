/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
    './**/templates/**/**/*.html', //added to hopefully cover new apps
    './**/static/**/**/*.js', //added to hopefully cover new apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

