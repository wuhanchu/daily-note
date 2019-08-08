var path = require("path")

var outPath = path.resolve(__dirname, "./lib")

module.exports = {
    entry: "./src/index.js",
    output: {
        path: outPath
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                loader: "style-loader!css-loader"
            },
            {
                test: /\.less$/,·
                exclude: /node_modules/,
                loader: "style-loader!css-loader!less-loader",
                options: {
                    javascriptEnabled: true
                }
            }
        ]
    },
    // 配置了 jsx 文件在import的时候才不需要写 扩展名
    resolve: {
        extensions: [.js", ".jsx"]
    },
    mode: "production"
}
