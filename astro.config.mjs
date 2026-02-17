import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  output: 'static',
  site: 'https://concreteportorange.com',
  compressHTML: true,
  build: {
    format: 'directory',
    inlineStylesheets: 'auto'
  }
});
