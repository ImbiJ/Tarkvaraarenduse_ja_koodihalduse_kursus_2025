# Käivitan generate data faili 10 korda
N=10
for i in $(seq 1 $N) # For-tsükkel, mis kordab käske
                              # iga i väärtuse jaoks
do #tsükli käsuread pannakse do ... done vahele
    echo "Käivitan faili generate_data.py $i korda"
                          #echo kuvab sõnumi terminalis
                          # $i - mitmendat korda
    python3 generate_data.py > ../data/data$i.txt 
                          # > suunab skripti väljundi faili,
                          # mis asub teises kataloogis samal tasandil
done

echo "Kõik failid on slavestatud kataloogi data/"
