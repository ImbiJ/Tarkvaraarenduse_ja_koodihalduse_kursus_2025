FROM python:3.11-slim # Määrab aluspildi, millest konteiner ehitatakse
COPY app.py /app/app.py
WORKDIR /app # Seadistab töökataloogi konteineris, kus kõik järgmised käsud toimuvad.
CMD ["python", "app.py"] # Määrab, milline käsk konteineri käivitamisel automaatselt käivitub.
        # Oluline: konteiner võib CMD-iga ainult ühe käsu automaatselt käivitada.
# COPY requirements.txt . # Vasakul on sinu arvutis fail, paremal konteineris asukoht
# RUN pip install --no-cache-dir -r requirements.txt # Käivitab käske konteineri ehitamise ajal (nt tarkvara installimine).
# ENV DEBUG=True # Määrab keskkonnamuutuja konteineris
# EXPOSE 5000 # Näitab, millist porti konteiner kasutab (see ei ava porti automaatselt, ainult dokumenteerib).
# ENTRYPOINT ["python", "Kodutoo_Docker.py"] # Sarnane CMD-ile, aga veidi tugevam: käivitab alati määratud käsu, CMD saab lisaks argumente anda.
# ARG VERSION=1.0 # Ehitusaja muutuja, mida saab kasutada RUN käskudes.
# VOLUME /app/data # Määrab konteineris katalooge, mida saab hostiga jagada.





