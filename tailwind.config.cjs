/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#0d9488', // Teal - coastal Florida vibe
          dark: '#0f766e',
          light: '#14b8a6',
        },
        secondary: {
          DEFAULT: '#1e293b', // Slate
          dark: '#0f172a',
          light: '#334155',
        },
        accent: {
          DEFAULT: '#f97316', // Orange pop
          warm: '#fb923c',
        },
        trust: '#22c55e', // Green for trust elements
        urgent: '#dc2626', // Red for urgency
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'bounce-slow': 'bounce 2s infinite',
      },
    },
  },
  plugins: [],
}
