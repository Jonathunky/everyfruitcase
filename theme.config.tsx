import React from 'react'
import { DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  logo: (
    <>
      <img
        src="/icon.png"
        alt="EveryCase Logo"
        style={{ marginRight: '8px', width: '40px', height: 'auto' }}
      />
      <span
        style={{
          fontFamily: 'Helvetica',
          fontWeight: 'bold',
          fontSize: '24px',
          letterSpacing: '0px',
          color: '#333'
        }}
      >EveryCase</span>
    </>
  ),
  project: {
    //link: 'https://github.com/shuding/nextra-docs-template',
  },
  chat: {
    //link: 'https://discord.com',
  },
  docsRepositoryBase: 'https://github.com/JonathanX64/everyfruitcase',
  footer: {
    text: undefined,
    component: undefined
  },
  sidebar: {
    defaultMenuCollapseLevel: 1
  },
  gitTimestamp: false,
  primaryHue: 320,
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
        <meta property="og:title" content="EveryCase" />
        <meta property="og:description" content="The website about Apple cases" />
        <style>
          {`
            @font-face {
              font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
              font-style: normal;
              font-weight: 400;
            }
          `}
        </style>
      </>
    );
  },
  search: {
    placeholder: "Search..."
  },
}

export default config
