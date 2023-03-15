import React from 'react'
import { DocsThemeConfig } from 'nextra-theme-docs'

const footer = {
  text: undefined,
  component: undefined
}

const config: DocsThemeConfig = {
  logo: <span>👀 EveryCase</span>,
  project: {
    //link: 'https://github.com/shuding/nextra-docs-template',
  },
  chat: {
    //link: 'https://discord.com',
  },
  docsRepositoryBase: 'https://github.com/JonathanX64/everyfruitcase',
  footer: footer,
  sidebar: {
    defaultMenuCollapseLevel: 1
  },
  gitTimestamp: false,
  faviconGlyph: '🤙🏻',
  useNextSeoProps() {
    return {
      titleTemplate: '%s – EveryCase'
    }
  },
  toc: {
    float: true
  },
  head: function Head() {
    return (
      <>
        <meta name="robots" content="noindex" />
      </>
    );
  },
  search: {
    placeholder: "Search..."
  },
}

export default config
