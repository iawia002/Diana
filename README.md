# Diana
[![](http://img.l.jifangcheng.com/9a1600e2c26fd6180663bc88581f70f3580d2494.png)](https://l.jifangcheng.com)

Edit | Tags | Article
--- | --- | ---
![](http://img.l.jifangcheng.com/ccb802efdf2324a1bc5b1c9c4bb4b6872ba2fd54.png) | ![](http://img.l.jifangcheng.com/bca54377ba24092cf7f8404bca6aff9b7951381b.png) | ![](http://img.l.jifangcheng.com/3138596bb343f210d7aa238165817ece3efd7a83.png)

[![Build Status](https://travis-ci.org/iawia002/Diana.svg?branch=master)](https://travis-ci.org/iawia002/Diana)
[![codecov](https://codecov.io/gh/iawia002/Diana/branch/master/graph/badge.svg)](https://codecov.io/gh/iawia002/Diana)

## Key feature
* Writing with __Markdown__
* Use __label__ to categorize

## Architecture
### frontend
* __npm__
* __webpack__
* __sass__

### backend
* __Flask__ as web framework
* __PostgreSQL__ as database
* __SQLAlchemy__ as ORM

## Quick Start
### frontend
* `npm install` install dependencies
* `npm run dev --Diana:app=blog` start dev environment
* `npm run build --Diana:app=blog` build(for production environment)

### backend

#### play with docker 🐳
* `fab migrate` database migration
* `fab init` Initialize a user(admin/admin) and an article
* `fab runserver`

have fun [http://0.0.0.0:8004](http://0.0.0.0:8004)
