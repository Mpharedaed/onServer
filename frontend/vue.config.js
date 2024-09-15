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
  }
}
