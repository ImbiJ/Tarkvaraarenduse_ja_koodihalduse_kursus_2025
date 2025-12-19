README_DOCKER
DOCKERFILE'i ja IMAGE loomine

1) tegin uue Dockerfaili teminalis käsuga nano Dockerfile:
FROM python:3.11-slim
COPY app.py /app/app.py
WORKDIR /app
CMD ["python", "app.py"]

2) lõin faili app.py:
print("Tere Dockerist!")

3) ehitasin image käsuga: docker build -t myapp .
Väljund:
+] Building 1.4s (9/9) FINISHED                                      docker:desktop-linux
 => [internal] load build definition from Dockerfile                                  0.0s
 => => transferring dockerfile: 121B                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                   1.2s
 => [auth] library/python:pull token for registry-1.docker.io                         0.0s
 => [internal] load .dockerignore                                                     0.0s
 => => transferring context: 2B                                                       0.0s
 => [internal] load build context                                                     0.0s
 => => transferring context: 27B                                                      0.0s
 => [1/3] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c  0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c  0.0s
 => CACHED [2/3] COPY app.py /app/app.py                                              0.0s
 => CACHED [3/3] WORKDIR /app                                                         0.0s
 => exporting to image                                                                0.1s
 => => exporting layers                                                               0.0s
 => => exporting manifest sha256:f05ae37cb203fc3c212f3ad10911409a87302fd2f09ff5364d6  0.0s
 => => exporting config sha256:a64432ef99eccb48ae34cd9fdb202e279c733eac4360fbfbccf7b  0.0s
 => => exporting attestation manifest sha256:94cec75c071759f5d49766ca297a371c2864ab4  0.0s
 => => exporting manifest list sha256:d2c7ce72d7877f4323949278c3d7e03be168e026d8bbff  0.0s
 => => naming to docker.io/library/myapp:latest                                       0.0s
 => => unpacking to docker.io/library/myapp:latest  

4) käivitasin konteineri käsuga: docker run myapp
Väljund: Tere Dockerist!

5) Tõstsin failid githubi:
* git init
* git status
* git add Dockerfile app.py README_DOCKER.md
* git commit -m "Docker kodutöö kaustas Kodutood"
* git push origin main
* kontroll githubis