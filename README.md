# Diana
[![](http://img.l.jifangcheng.com/67db89911c345584a41685cb9741ab76f501e878.png)](https://l.jifangcheng.com)

Edit | Tags | Article
--- | --- | ---
![](http://img.l.jifangcheng.com/1ef1b1e039260bcef2a5daf94f9507f393c27046.png) | ![](http://img.l.jifangcheng.com/bca54377ba24092cf7f8404bca6aff9b7951381b.png) | ![](http://img.l.jifangcheng.com/3138596bb343f210d7aa238165817ece3efd7a83.png)

## Architecture
### frontend
* __npm__
* __webpack__
* __coffeescript__
* __sass__

### backend
* __Tornado__ as web framework
* __PostgreSQL__ as database
* __SQLAlchemy__ as ORM

## Quick Start
### frontend
* `npm install` install dependencies
* `npm run d` start dev environment
* `npm run build` build(for production environment)

### backend
#### normal way
* `pip install -r requirements.txt`
* `fab migrate:local` database migration
* `fab init:local` Initialize a user(admin/admin) and an article
* `fab runserver:local` or `python app.py -debug=True`

#### play with docker 🐳
* `fab migrate` database migration
* `fab init` Initialize a user(admin/admin) and an article
* `fab runserver`

have fun [http://0.0.0.0:8004](http://0.0.0.0:8004)
