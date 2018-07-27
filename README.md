# Diana

[![](docs/images/index.png)](https://ia.jifangcheng.com)

[![Build Status](https://travis-ci.org/iawia002/Diana.svg?branch=master)](https://travis-ci.org/iawia002/Diana)
[![codecov](https://codecov.io/gh/iawia002/Diana/branch/master/graph/badge.svg)](https://codecov.io/gh/iawia002/Diana)


## 关键特性

* 使用 __Markdown__ 写作
* 用 __标签__ 来分类


## 架构
### 前端
* TypeScript
* React
* Sass + CSS Modules

### 后端
* Web 框架：__Flask__
* 数据库：__PostgreSQL__
* ORM：__SQLAlchemy__


## 快速开始
### 前端

前端目录：`moon`

* `yarn install` 安装依赖
* `yarn start` 启动开发环境（[http://localhost:3000](http://localhost:3000)）
* `yarn build` 构建生产环境

### 后端

使用 Docker 🐳：

* `fab migrate` 数据库迁移
* `fab init` 初始化一个用户(admin/admin) 和一篇文章
* `fab dev` 启动服务器开发环境（[http://0.0.0.0:8004](http://0.0.0.0:8004)）
