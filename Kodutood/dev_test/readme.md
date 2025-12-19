# Uus projekt

Plaan teha oma esimene dev (development) konteiner
cmd + shift + P -< käsud>dev -> add dev configuration file
alati lisa workspace'i - kataloogi, mis on parasjagu avatud
Millist konteinerit ma tahan aluseks võtta (Java, phyton, markwown jms)
Valisin Python. 
Kõik see on kihiliselt üles ehiatdtud. Nüüd vali kõige viimasem versioon
Edasi saad lisada featureid nendega saab paigaldada lisaprofaile oma projekti
kas tahame lisada ka üht githubi faili?

Tekitati devcontainer.json fail ja githubi fail, mis kontrollib, kas meie dev-konteiner töötab.

Dev-konteiner pane tööle: VSC all paremas nurgas on kelluke (notifications) - klikka sellel, ütle, et ta paneks konteineri tööle. Kui klikkas sinisel pealkirjal, siis näed, mis toimub.

Kui üles otsingureale tekib nimi "dev_test [dev ...] NB! Just nurksulgused tekst!!, siis oled konteineri sees.

Ava Terminal ja seal + märgi juures noolelt vali fish.

Projekti saad kinni panna close remote connection või siis all vasakul sinine >< tekstiga ruuduke, sealt vali close remote connection

uuesti avada saad ka sealt või notificationsi alt. 

Kui töötad konteineris, siis sinu kasutaja on vscode

Töökataloog on workspaces, kasutaja vscode, sudo õigustega (saad jooksutada kõiki käske ruuduna (root) ehk administraatorina)

sudo apt update - tõmbab avalikust serverist alla mingid pakettide viimased versioonid


# devcontainer. json

siin saab veel lisada erinevaid asju, mis meil võiks vaja olla. 
Kui avan dev konteineri, siis minu arvutis lisatud laiendused default konteineris ei tööta. Seega pean ma need laiendused siin failis välja tooma
olulised on ms-python.python ja ms-python.vscode-pylance

lisaks pean olema kindel, minu materjalid mountitakse minu konteineri sisse: 
"mounts": [
        "source=${localWorkspaceFolder},target=/workspace,type=bind,consistency=cached"
    ],
    "workspaceFolder": "/workspace"


punktiga algavaid katalooge ma ei näe finderis, sest need on peidetud.    

Kui konteiner ei tööta, vali ülevalt reopen conatiner

Kahe akna vahel saab liikuda cmd + <

kui midagi lisad konteinerisse, siis konteineris sees olles vali: cmd + shift + P -> vali ülevalt dev containers: rebuilt

devkonteinerite kohta saad infot ja teavet VSC oma juhendist

Kui jagad kaaslastega .json faili, siis oled kaaslastega samas kaustas

# Image
Parem kasuta dockerfaili, mitte image't siis saab lisada muid asju juurde

või loo ise image, mida saad registreerida.

## Image loomine dockerfile'ga

"image" asemele "build"
"build": {"dockerfile": "Dockerfile", "context": ".."} #see on väga oluline osa! .. viib kataloogi 1 taseme võrra ülespoole, kust otsib requirements faili

siin oli mingeid muudatusi veel

tekita kataloogi Dockerfile (vt Dockeri alt), Kindlasti lisa juurde git.

ja siis taas rebuild. Kui oled konteinerist väljas, siis reopen ja rebuild

# DEv container ja github

githubist saab seda otse avada VSC-s, arvutis töö ära teha. Seejärel pead syncima githubi
