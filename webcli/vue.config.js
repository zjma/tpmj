module.exports = {
  "publicPath": "/2pmj/",
  "outputDir": "2pmj",
  "transpileDependencies": [
    "vuetify"
  ],
  chainWebpack: config => {
  config.module.rules.delete("svg");
},
configureWebpack: {
  module: {
    rules: [
      {
        test: /\.svg$/,
        loader: 'vue-svg-loader',
      },
    ],
  }
}

}
