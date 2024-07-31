import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import react from "@astrojs/react";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import rehypeMermaid from 'rehype-mermaid'
import mdx from '@astrojs/mdx';
import astroExpressiveCode from "astro-expressive-code";
import { pluginLineNumbers } from '@expressive-code/plugin-line-numbers'
import { remarkImage } from "./plugins/image";
import { remarkToc } from "./plugins/toc";
import remarkCollapse from "remark-collapse";
import sitemap from "@astrojs/sitemap";
import { SITE } from "./src/config";

// https://astro.build/config
export default defineConfig({
  site: SITE.website,
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
    react(),
    sitemap(),
    astroExpressiveCode({
      defaultProps: {
        wrap: true,
      },
      plugins: [pluginLineNumbers()],
      themes: ['dracula'],
    }),
    // expressiveCode({
    //   // Replace the default themes with a custom set of bundled themes:
    //   // "dracula" (a dark theme) and "solarized-light"
    //   themes: ['github-light', 'dracula'],
    // }),
    mdx(),
  ],
  markdown: {
    remarkPlugins: [
      remarkMath,
      remarkImage,
      [remarkToc, { maxDepth: 3 }],
      [
        remarkCollapse,
        {
          test: "Table of contents",
        },
      ],
    ],
    rehypePlugins: [
      rehypeKatex,
      [
        rehypeMermaid,
        { strategy: "img-svg" }
        // { strategy: "img-png" }
      ],
    ],
    shikiConfig: {
      // For more themes, visit https://shiki.style/themes
      themes: { light: "min-light", dark: "night-owl" },
      wrap: true,
    },
  },
  vite: {
    optimizeDeps: {
      exclude: ["@resvg/resvg-js"],
    },
  },
  scopedStyleStrategy: "where",
});
