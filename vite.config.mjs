import { defineConfig } from "vite";

// Configuration entry point
export default defineConfig({
  base: "/static/",
  build: {
    manifest: "manifest.json",
    emptyOutDir: true,
    outDir: "static_compiled",
    rollupOptions: {
      input: {
        main: "static_src/javascript/main.js",
      }
    },
  },
});
