### Nodejs手动安装

1. 手动新增目录结构

    |- node
        |- nodejs
        |- node-global
        |- npm-cache
        |- test

2. 将[nodejs-version.zip](http://nodejs.org/dist/latest-v9.x/)文件解压至nodejs目录 

3. 将nodejs文件夹路径添加到系统环境变量PATH中
4. 
4. 配置全局模块的安装路径

    npm config set prefix "D:\node\node-global"
    npm config set cache "D:\node\npm-cache"

5. 将node-global文件夹路径添加到系统环境变量PATH中

6. 进入test文件夹新增package.json,内容如下

    "scripts": {
        "test": "mocha"
    }
    或 npm init 生成

7. 运行npm test

- 安装

    npm install --global mocha
    npm install --global nps

- [找不到package.json的问题](https://segmentfault.com/q/1010000004557614)