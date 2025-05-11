# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on digitaalinen versio korttipelistä, jossa pelaajat pyrkivät pääsemään eroon korteistaan noudattaen pelin sääntöjä. Kortteja voi pelata, jos ne vastaavat värin tai numeron (0-9) perusteella pöydällä olevaa korttia. Pelissä on myös erikoiskortteja, jotka voivat vaikuttaa pelin kulkuun. Sovellus tarjoaa yksinpelin tekoälyvastustajaa vastaan.


## Perusversion tarjoama toiminnallisuus

### Pelin kulku yleisesti

- Aloittaessa uuden pelin pelaajalle ja tekoälylle jaetaan korttipakasta aloituskäsi (7 korttia)
- Pelaajat pelaavat vuorotellen kortteja pelin sääntöjen mukaisesti
  - Pelaaja voi pelata kortin, jos se täsmää värin tai numeron perusteella pöydällä olevaan korttiin tai on villi-kortti
  - Pelaaja voi halutessaan nostaa kortin pakasta ja vuoro vaihtuu
- Erkoiskortit vaikuttavat pelin kulkuun:
  - Ohituskortti: vuoro siirtyy seuraavalle pelaajalle (kaksinpelissä kortin pelannut pelaaja saa toisen vuoron)
  - Suunnanvaihto: pelin suunta vaihtuu (toimii kuten ohituskortti kaksinpelissä)
  - Nosta kaksi: vastustaja nostaa kaksi korttia ja menettää vuoronsa
  - Nosta neljä: vastustaja nostaa 4 korttia, menettää vuoronsa ja kortin pelannut pelaaja valitsee minkä värinen kortti pitää pelata seuraavaksi
  - Villi kortti: pelaaja valitsee minkä värinen kortti pitää pelata seuraavaksi
- Peli päättyy voittoon tai häviöön, kun jompikumpi pelaaja pääsee eroon kaikista korteistaan
- Peli päättyy tasapeliin, jos nostopakasta loppuvat kortit
- Voittaja saa pisteitä vastustajan korteista
- Pelaaja voi aloittaa uuden pelin

## Tällä hetkellä valmiit toiminnallisuudet
- [x] Pelaajat pelaavat vuorotellen kortteja pelin sääntöjen mukaisesti
  - [x] Pelaaja voi pelata kortin, jos se täsmää värin tai numeron perusteella pöydällä olevaan korttiin tai on villi-kortti
  - [x] Pelaaja voi nostaa kortin pakasta
- [x] Poistopakan kortit sekoitetaan tarvittaessa ja lisätään nostopakkaan
- [x] Peli päättyy, kun jompikumpi pelaaja pääsee eroon kaikista korteistaan (voitto/häviö)
- [x] Pelaaja voi lopettaa tai aloittaa uuden pelin pelin loppumisen jälkeen
- [x] Pelaaja voi pelata värillisiä ohitus- ja suunnanvaihtokortteja saadakseen toisen vuoron
- [x] Pelaaja voi pelata värillisiä nosta 2 kortteja saadakseen vastustajan nostamaan kaksi korttia ja menettämään vuoronsa
- [x] Pelaaja voi pelata villi-kortin ja valita seuraavaksi pelattavan kortin värin
- [x] Pelaaja voi pelata villi nosta 4-kortin ja valita seuraavaksi pelattavan kortin värin sekä saada vastustajansa nostamaan 4 korttia ja menettämään vuoronsa
- [x] Peli päättyy, jos kaikki kortit nostetaan pakasta (tasapeli)
- [x] Peliin on lisätty grafiikoita esim. kortteja tekstin sijaan
- [x] Jos pelaaja nostaa kortteja yli 30 niin niitä voi selata nuolinäppäimillä
- [x] Pelaajalle lasketaan pisteitä voiton jälkeen ja ne tallennetaan top 10 rankingiin
- [x] Pelin aloitusvalikosta pelaaja voi valita haluaako aloittaa pelin, lukea ohjeet, katsoa rankingia tai poistua

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
- Pelaaja voi säätää pelin vaikeustasoa
- Pelaaja voi muuttaa pelin sääntöjä
- Lisää tekoälyvastustajia
- Ääniefektit ja animaatiot
- Turnauspelit, jossa pisteet lasketaan useamman erän perusteella
- Moninpeli verkossa
