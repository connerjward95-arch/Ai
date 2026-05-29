/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#667eea',
        'primary-dark': '#5568d3',
        secondary: '#764ba2',
        success: '#48bb78',
        warning: '#f6ad55',
        danger: '#f56565',
      },
    },
  },
  plugins: [],
};
