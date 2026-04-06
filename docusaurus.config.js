// @ts-check
const remarkMath = require('remark-math').default;
const rehypeKatex = require('rehype-katex').default;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Computabilidad y Complejidad - Documentacion',
  tagline: 'Trabajos practicos y teoria',
  url: 'http://localhost',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  markdown: {
    format: 'md',
    hooks: {
      onBrokenMarkdownLinks: 'warn'
    }
  },
  i18n: {
    defaultLocale: 'es',
    locales: ['es']
  },
  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex]
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css')
        }
      }
    ]
  ],
  themeConfig: {
    navbar: {
      title: 'Computabilidad y Complejidad',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Documentacion'
        }
      ]
    }
  }
};

module.exports = config;
