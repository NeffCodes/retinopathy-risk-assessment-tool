module.exports = {
  // Enabling JIT mode for faster builds and more flexibility in using dynamic class names
  mode: 'jit',
  // Defining the paths where Tailwind should look for class names
  content: [
    "./patients/templates/**/*.{html,js}",   // Templates in the 'patients' app
    "./patients/templates/partials/**/*.{html,js}",  // Partials in the 'patients' app
    "./templates/**/*.html",    // Generic templates
    "./static/**/*.js",         // Static JavaScript files
    "./static/**/*.svg",        // SVG files
    "./**/forms.py"             // If we use Django forms with Tailwind classes
  ],
  theme: {
    // Extend allows you to add custom values while retaining the default ones
    extend: {
      // Custom color palette to suit your project's branding
      colors: {
        'primary': '#1E3A8A', // Dark Blue
        'secondary': '#34D399', // Light Green
        'accent': '#3B82F6', // Another shade of blue for accents
        'neutral': '#F3F4F6', // Light gray for backgrounds
        'text': '#374151', // Dark gray for text
      },
      // Custom font families to maintain brand consistency
      fontFamily: {
        sans: ['Open Sans', 'ui-sans-serif', 'system-ui'], // Tailwind's 'sans' key with custom fonts
        serif: ['Merriweather', 'ui-serif', 'Georgia'], // Optional serif font
      },
      // Custom spacing to provide more flexibility in layouts
      spacing: {
        '18': '4.5rem', // Example custom spacing value
      },
    },
  },
  plugins: [],
};
