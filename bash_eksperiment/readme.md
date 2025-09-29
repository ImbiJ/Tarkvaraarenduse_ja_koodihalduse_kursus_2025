tegin bash eksperimendi ja pean siia lisama kõik käsud, mida ma kasutasin. 

Õnneks salvestasin varem oma bash eksperimendi käud eraldi faili ja saan sealt vaadata.

(base) WJ-arvuti:~ imbi$ cd Magistrantuur/Git_repod/Tarkvaraarendus
(base) WJ-arvuti:Tarkvaraarendus imbi$ mkdir bash_eksperiment
(base) WJ-arvuti:bash_eksperiment imbi$ mkdir data
(base) WJ-arvuti:bash_eksperiment imbi$ mkdir scripts
(base) WJ-arvuti:bash_eksperiment imbi$ mkdir results
(base) WJ-arvuti:bash_eksperiment imbi$ touch readme.md
(base) WJ-arvuti:bash_eksperiment imbi$ ls
data		readme.md	results		scripts
/Users/imbi/Magistrantuur/Git_repod/Tarkvaraarendus/bash_eksperiment/scripts
(base) WJ-arvuti:scripts imbi$ nano generate_data.py
(base) WJ-arvuti:bash_eksperiment imbi$ cd scripts
(base) WJ-arvuti:scripts imbi$ nano generate_data.sh
(base) WJ-arvuti:scripts imbi$ nano generate_data.sh
(base) WJ-arvuti:scripts imbi$ chmod +x generate_data.sh
(base) WJ-arvuti:scripts imbi$ ./generate_data.sh
Käivitan faili generate_data.py 1 korda
Käivitan faili generate_data.py 2 korda
Käivitan faili generate_data.py 3 korda
Käivitan faili generate_data.py 4 korda
Käivitan faili generate_data.py 5 korda
Käivitan faili generate_data.py 6 korda
Käivitan faili generate_data.py 7 korda
Käivitan faili generate_data.py 8 korda
Käivitan faili generate_data.py 9 korda
Käivitan faili generate_data.py 10 korda
Kõik failid on slavestatud kataloogi data/
(base) WJ-arvuti:bash_eksperiment imbi$ cat data/* | sort -n | uniq -c > results/summary_total_unique_numbers_counted.txt
(base) WJ-arvuti:bash_eksperiment imbi$ # cat data/* → loeb kõik failid data kataloogist kokku.
(base) WJ-arvuti:bash_eksperiment imbi$ # sort → paneb kõik arvud järjestusse.
(base) WJ-arvuti:bash_eksperiment imbi$ # uniq -c → loeb kokku, mitu korda iga unikaalne arv esineb.
(base) WJ-arvuti:bash_eksperiment imbi$ # > → suunab väljundi faili.
(base) WJ-arvuti:bash_eksperiment imbi$ nano readme.md


Kataloogis data on 10 txt-faili juhuslikult genereeritud numbritega.
Kataloogis reults on fail summary_total_unique_numbers_counted.txt, kus on loetletud, 
mitu korda üht või teist numbrit esines.
Kaustas scripts on 2 faili: generate_data.py ja generate_data.sh
