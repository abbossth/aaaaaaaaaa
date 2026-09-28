#!/usr/bin/env bash
# 32-dars: image yig'ish, tag, push (mvp-skelet/server papkasida bajaring)

docker build -t mvp-server .                   # yig'ish (oxiridagi nuqta = build context)
docker images mvp-server                       # hajmini ko'ring
docker run -d -p 3000:3000 --name api mvp-server
curl localhost:3000/api/health
docker ps                                      # STATUS: (healthy) ~30 soniyadan keyin

# Kesh tajribasi: src/app.js ga bitta izoh qo'shing va qayta yig'ing
docker build -t mvp-server .                   # "CACHED" qatorlarini sanang!

# Versiyalash (tag)
docker tag mvp-server  <dockerhub_login>/mvp-server:0.1.0
docker tag mvp-server  <dockerhub_login>/mvp-server:latest

# Docker Hub'ga yuklash
docker login
docker push <dockerhub_login>/mvp-server:0.1.0
docker push <dockerhub_login>/mvp-server:latest

# Boshqa kompyuterda (sinfdoshingiznikida!):
# docker run -d -p 3000:3000 <dockerhub_login>/mvp-server:0.1.0

docker rm -f api
