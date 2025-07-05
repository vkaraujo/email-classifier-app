import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      '/upload': 'http://localhost:5000'
    }
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './test/setup.js',
    include: ['test/**/*.{test,spec}.{js,jsx,ts,tsx}']
  }
})
