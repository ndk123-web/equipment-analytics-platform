import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react() , tailwindcss()],
  server: {
    // example: from react -> get('/api/data') it means get('http://localhost:8000/api/data')
    proxy: {
      '/api': 'http://localhost:8000'
    }
  }
})
