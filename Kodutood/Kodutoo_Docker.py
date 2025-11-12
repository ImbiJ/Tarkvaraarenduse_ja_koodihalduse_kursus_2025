## Ül 1
# käivita docker  
docker run hello-world
print("Docker käivitamine õnnestus!")


## Ül 2
# tõmba ubuntu image
docker pull ubuntu

# käiita
docker run -it ubuntu bash
print("Ubuntu konteiner on käivitatud!")

#Konteineris failide ja kaustade vaatamine: 
ls
pwd

# paketihaldus 
apt-get update

# välju konteinerist
exit

## Ül 3
# Containeri life-cycle

# Käivita taustal konteiner
docker run -dit --name test-ctr ubuntu bash

# Kontrolli olekut:
docker ps 

# peata konteiner
docker stop test-ctr

# käivita konteiner uuesti
docker start test-ctr

# ava uuesti terminali sees
docker exec -it test-ctr bash

# Ül 4
# Oma Dockerfile

# Loo fail Dockerfile

# Ava VSC.
# Vali menüüst File → Open Folder → New File → Sisesta failinimeks Dockerfile
# Kopeeri allaolev kood faili ja salvesta see.

FROM python:3.11-slim # kindlasti suurte tähtedega
COPY app.py /app/app.py
WORKDIR /app
CMD ["python", "app.py"]

# kontrolli terminalis sisu:
cat Dockerfile

    # Dockerfile on pigem retsept, mis ütleb Dockerile, kuidas ehitada konteiner: 
        # millist baasipilti kasutada, 
        # millised sõltuvused installida, 
        # milliseid faile konteinerisse kopeerida ja 
        # kuidas konteiner käivitada.


# loo fail app.py
# Vasakul failipaanil tee oma kausta peal paremklõps → vali New File
# Pane nimeks app.py
# Ava fail ja kirjuta sinna:

print("Tere Dockerist!")
# Salvesta fail

# nüüd mine terminali
python3 app.py

# näed väljundit " Tere Dockerist!"

# Ehita image:
docker build -t myapp .

# Käivita image:
docker run myapp


# Ül 5
# Volumes & Mounts

# kuidas andmeid jagada konteineri ja hosti vahel
# Loo kaust data ja sinna fail hello.txt niimoodi:

# Käivita konteiner, kus kaust mountitakse:
docker run -it -v $(pwd)/data:/data ubuntu bash

# Siin: 
    # docker run - käivitab konteineri
    # -it - interaktiivne terminal
        # i - interactive, hoiab STDIN-i avatud, nii et saad konteineriga suhelda
        # t - terminal, loob pseudo-TTY, Loob terminali „akna“ konteinerisse, et saaksid käskusid mugavalt kirjutada.
        # Koos -it tähendab see: saad konteineris shelli avada ja käske interaktiivselt sisestada
    # -v $(pwd)/data:/data - volume mount, ehk failisüsteemi ühendamine
        # $(pwd)/data - sinu arvuti kataloog data, mis asub praeguses kaustas (pwd = print working directory).
        # : - eraldab hosti ja konteineri teed
        # /data - konteineri kaust, kuhu hosti kaust mountitakse
    # ubuntu - image, mida kasutatakse konteineri loomiseks
    # bash - käsk, mis konteineris käivitatakse (siin avab bash shelli, kuhu saad käske sisestada)
        # Kui jätad bash ära, käivitub Ubuntu vaikimisi protsess ja konteiner võib kohe sulguda
# Nüüd konteineris:
cat /data/hello.txt

# cat = ainult loeb, ei muuda faili sisu

    # NB! Faili sisu saab muuta ainult käsudega, mis kirjutavad faili, näiteks:

echo "uus sisu" > /data/hello.txt    # kirjutab kogu faili üle
echo "lisatud rida" >> /data/hello.txt # lisab faili lõppu
nano /data/hello.txt                  # avab redaktoris ja salvestamisel muudetakse faili
        # Üleliigne > asendab kogu faili sisu
        # >> lisab faili lõppu, ei kustuta olemasolevat sisu


# Ül 6
# Halda konteinereid ja korista enda järel
# kuidas eemaldada mittevajalikud konteinerid, volume'id ja vabastada kettaruumi.

# Näita kõiki konteinereid (sh peatatud):
docker ps -a

# Eemalda kõik konteinerid, mida enam ei vaja, kui konteiner veel töötab, tuleb see ennem peatada (docker stop <container_id_or_name>):
docker rm <container_id_or_name>

# Näita kõiki volume'eid:
docker volume ls

    # Kontrolli, kas volüüm on kasutuses:
docker ps -a --filter volume=<VOLUME_NAME>

        # Kui konteinerit leitakse → volüüm on kasutuses, ära eemalda.
        # Kui konteinerit ei leita → volüüm võib olla kasutamata ja turvaline eemaldamiseks.

    # Vaata, kuhu konteinerisse see võib kuuluda:
docker inspect <VOLUME_NAME>

#Eemalda kasutamata volume'id:
docker volume prune

# Loo volüümid selgete nimedega, et neid oleks lihtne tuvastada:
docker volume create kodutoo_volume

    # See volüüm eksisteerib Dockeris, kuid ei ole veel ühegi konteineriga ühendatud.
    # Selle abil saab hiljem andmeid salvestada konteinerite vahel, ilma et need kaoksid, kui konteinerid kustutatakse.
    # Kontrolli, et volüüm on loodud
docker volume ls

    # Kui sul on näiteks ubuntu konteiner, saad selle volüümi külge ühendada nii:
docker run -it -v kodutoo_volume:/data ubuntu bash

#Kontrolli süsteemi kasutust:
docker system df

#Korista kõik kasutamata andmed (images, konteinerid, volume'id, võrgud):

# NB! järgmise käsuga peab olema ettevaatlik. Enne kasutamist loe lisaks: https://docs.docker.com/reference/cli/docker/system/prune/ 
docker system prune

# Pushi oma töö Githubi
    # 1) terminali kaudu:
git init            # Kui repo veel algatatud pole
git add .           # Lisa kõik failid jälgimisele
git commit -m "Esimene commit"
git branch -M main  # Nimetab haru main-iks, kui vaja
git remote add origin https://github.com/KASUTAJA/KODUTOO_DOCKER.git # Asenda URL oma GitHubi repo URL-iga.
git push -u origin main


        # Pärast seda piisab järgmistest pushidest ainult:
git add .
git commit -m "muudatus"
git push

    # 2) VS Code’i GUI kaudu (ilma käsureata)
        # a) Ava Source Control vaade (vasak menüü, ikoon, mis näeb välja nagu haru)
        # b) Vajuta plussmärgile (+), et lisada kõik failid jälgimisele
        # c) Sisesta commit sõnum ülaosas ja vajuta linnukest (✓), et commit teha
        # d) Vajuta kolme punktiga menüül (•••) ja vali Push, et muudatused GitHubi saata

