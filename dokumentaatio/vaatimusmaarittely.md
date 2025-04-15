# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on digitaalinen versio korttipelistä, jossa pelaajat pyrkivät pääsemään eroon korteistaan noudattaen pelin sääntöjä. Kortteja voi pelata, jos ne vastaavat värin tai numeron (0-9) perusteella pöydällä olevaa korttia. Pelissä on myös erikoiskortteja, jotka voivat vaikuttaa pelin kulkuun. Sovellus tarjoaa yksinpelin tekoälyvastustajaa vastaan.


## Perusversion tarjoama toiminnallisuus

### Pelin kulku yleisesti

- Aloittaessa uuden pelin pelaajalle ja tekoälylle jaetaan korttipakasta aloituskäsi
- Pelaajat pelaavat vuorotellen kortteja pelin sääntöjen mukaisesti
  - Pelaaja voi pelata kortin, jos se täsmää värin tai numeron perusteella pöydällä olevaan korttiin
  - Jos pelaaja ei voi pelata korttia, hän nostaa kortin pakasta
- Erkoiskortit vaikuttavat pelin kulkuun:
  - Ohituskortti: vuoro siirtyy seuraavalle pelaajalle (kaksinpelissä kortin pelannut pelaaja saa toisen vuoron)
  - Suunnanvaihto: pelin suunta vaihtuu (toimii kuten ohituskortti kaksinpelissä)
  - Nosta kaksi: vastustaja nostaa kaksi korttia ja menettää vuoronsa
  - Nosta neljä: vastustaja nostaa 4 korttia, menettää vuoronsa ja kortin pelannut pelaaja valitsee minkä värinen kortti pitää pelata seuraavaksi
  - Villi kortti: pelaaja valitsee minkä värinen kortti pitää pelata seuraavaksi
- Pelaajan tulee kirjoittaa "yksi" tai painaa tiettyä nappia ennen kuin pelaa toiseksi viimeisen korttinsa tai joutuu nostamaan pakasta neljä korttia
- Peli päättyy, kun jompikumpi pelaaja pääsee eroon kaikista korteistaan
- Voittaja saa pisteitä vastustajan korteista
- Pelaaja voi aloittaa uuden pelin

## Tällä hetkellä valmiit toiminnallisuudet
- [x] Pelaajat pelaavat vuorotellen kortteja pelin sääntöjen mukaisesti
  - [x] Pelaaja voi pelata kortin, jos se täsmää värin tai numeron perusteella pöydällä olevaan korttiin
  - [x] Pelaaja voi nostaa kortin pakasta
- [x] Poistopakan kortit sekoitetaan tarvittaessa ja lisätään nostopakkaan
- [x] Peli päättyy, kun jompikumpi pelaaja pääsee eroon kaikista korteistaan (voitto/häviö)
- [x] Pelaaja voi lopettaa tai aloittaa uuden pelin pelin loppumisen jälkeen
- [x] Pelaaja voi pelata värillisiä ohitus- ja suunnanvaihtokortteja saadakseen toisen vuoron
- [x] Pelaaja voi pelata värillisiä nosta 2 kortteja saadakseen vastustajan nostamaan kaksi korttia ja menettämään vuoronsa 

## Seuraavaksi lisättävät toiminnallisuudet
- [ ] Erikoiskortit: villi kortti, villi nosta 4
- [ ] Grafiikat korteille
- [ ] Pisteiden lasku, high score ranking

## Tunnetut ongelmat, korjaus tulee pian
- Jos pelaaja nostaa kortteja niin paljon kuin pystyy ja nostopakasta loppuvat kortit niin peli kaatuu (normaalisti pelatessa ei pitäisi olla ongelma)

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
- Pelaaja voi säätää pelin vaikeustasoa
- Pelaaja voi muuttaa pelin sääntöjä
- Lisää tekoälyvastustajia
- Ääniefektit ja animaatiot
- Turnauspelit, jossa pisteet lasketaan useamman erän perusteella
- Moninpeli verkossa
