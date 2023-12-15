// vue.config.js
const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: (config) => {
    config.plugin('html').tap((args) => {
      args[0].title = 'Your Custom Title'; // Set your custom title here
      return args;
    });
  },
});
