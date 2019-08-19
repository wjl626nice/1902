const HtmlWebpackPlugin = require('html-webpack-plugin')
const path = require('path') // 导入 node.js中专一操作路径的模块

const htmlPlugin = new HtmlWebpackPlugin({
    template: './src/index.html',
    filename: 'index.html'
})
const VueLoaderPlugin = require('vue-loader/lib/plugin')
module.exports = {
    entry: path.join(__dirname, './src/index.js'), //打包入口文件的路径
    output: {
        path: path.join(__dirname, './dist'), // 输出文件保存的路径
        filename: 'bundle.js' // 输入文件的名字
    },
    mode: 'development',
    plugins: [htmlPlugin, new VueLoaderPlugin()],
    module: {
        rules: [
            { test: /\.css$/, use: ['style-loader', 'css-loader', 'postcss-loader'] },
            {
                test: /\.jpg|png|gif|bmp|ttf|eot|svg|woff|woff2$/,
                use: 'url-loader?limit=14500'
            },
            { test: /\.js$/, use: 'babel-loader', exclude: /node_modules/ },
            { test: /\.vue$/, use: 'vue-loader' },
        ]
    }
}