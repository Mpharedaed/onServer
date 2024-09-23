const path = require('path');

module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'https://blogi-36jo.onrender.com',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  }
}
