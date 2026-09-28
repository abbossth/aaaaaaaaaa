# 16-dars tezkor test

1. URL'dagi `:id` qiymati qayerda? — `req.params.id`
2. `?page=2` qiymati? — `req.query.page`
3. JSON body'ni o'qish uchun qaysi middleware kerak? — `express.json()`
4. Resurs yaratilganda qaysi status? — 201
5. Middleware'da keyingisiga o'tish? — `next()`
6. Error handler middleware nechta parametrga ega? — 4 ta `(err, req, res, next)`
