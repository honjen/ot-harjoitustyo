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
  - Ohituskortti: vuoro siirtyy seuraavalle pelaajalle
  - Suunnanvaihto: pelin suunta vaihtuu (toimii kuten ohituskortti kaksinpelissä)
  - Nosta kaksi: vastustaja nostaa kaksi korttia
  - Nosta neljä: vastustaja nostaa 4 korttia, ja pelaaja valitsee uuden värin
  - Villi kortti: pelaaja valitsee uuden värin
- Pelaajan tulee kirjoittaa "yksi" ennen kuin pelaa toiseksi viimeisen korttinsa tai joutuu nostamaan pakasta neljä korttia
- Peli päättyy, kun jompikumpi pelaaja pääsee eroon kaikista korteistaan
- Voittaja saa pisteitä vastustajan korteista
- Pelaaja voi aloittaa uuden pelin

## Tällä hetkellä valmiit toiminnallisuudet
- [x] Pelaajat pelaavat vuorotellen kortteja pelin sääntöjen mukaisesti
  - [x] Pelaaja voi pelata kortin, jos se täsmää värin tai numeron perusteella pöydällä olevaan korttiin
  - [x] Jos pelaaja ei voi pelata korttia, hän nostaa kortin pakasta
- [x] Poistopakan kortit sekoitetaan tarvittaessa
- [x] Peli päättyy, kun jompikumpi pelaaja pääsee eroon kaikista korteistaan (voitto/häviö)
- [x] Pelaaja voi lopettaa tai aloittaa uuden pelin pelin loppumisen jälkeen

## Seuraavaksi lisättävät toiminnallisuudet
- [ ] Erikoiskortit
- [ ] Pisteiden lasku, high score ranking

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
- Graafinen käyttöliittymä
- Pelaaja voi tarkastella ranking listaa, jossa on listattuna pelaajat jotka ovat saaneet korkeimmat pistemäärät
- Pelaaja voi säätää pelin vaikeustasoa
- Pelaaja voi muuttaa pelin sääntöjä
- Lisää tekoälyvastustajia
- Ääniefektit ja animaatiot
- Turnauspelit, jossa pisteet lasketaan useamman erän perusteella
- Moninpeli verkossa
