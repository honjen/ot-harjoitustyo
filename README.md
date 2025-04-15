# Ohjelmistotekniikka, harjoitustyö: korttipeli

Sovellus on digitaalinen tekstipohjainen versio korttipelistä, jossa pelaajat pyrkivät pääsemään eroon korteistaan noudattaen pelin sääntöjä. Kortteja voi pelata, jos ne vastaavat värin tai numeron (0-9) perusteella pöydällä olevaa korttia. Pelissä tulee olemaan myös erikoiskortteja, jotka voivat vaikuttaa pelin kulkuun. Sovellus tarjoaa yksinpelin tekoälyvastustajaa vastaan.

Pelistä puuttuvat vielä lähiaikoina lisättävät ominaisuudet kuten:
- erikoiskortit: villi kortti, villi nosta 4 kortti
- pisteet, high score ranking
- grafiikat

Vaatimusmäärittelystä löytyy tarkemmin tietoa sovelluksesta sekä lisää jatkokehitysideoita. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Changelog](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Työaikakirjanpito](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)


## Ohjelman käynnistäminen

1. Ennen ohjelman käynnistämistä, asenna riippuvuudet:

```
poetry install
```

2. Käynnistä ohjelma:

```
poetry run invoke start
```

## Pelaaminen

Valitse pelattava kortti (numero tai väri on sama kuin poistopakan ylin kortti) painamalla jotain kirjaimen (a-z) nappia. Jos sinulla ei ole pelattavaa korttia niin paina enter ja saat kortin lisää. Peliin on lisätty värillisiä erikoiskortteja, kuten ohitus ja suunnanvaihto, joita pelaamalla pelaaja saa toisen vuoron. Pelaamalla värillinen nosta 2 kortti pelaaja laittaa vastustajan nostamaan 2 korttia ja menettämään vuoronsa. Pelistä puuttuvat vielä erikoiskortit, kuten villi kortti ja villi nosta 4 kortti. Kun pelaaja tai tietokone pääsee eroon korteistaan peli loppuu (voitto/häviö) ja voit valita haluatko pelata uuden pelin. Voit sulkea sovelluksen milloin tahansa painamalla yläkulman ruksia.

## Testaus

Suorita testit:

```
poetry run invoke test
```

## Testikattavuus

Generoi testikattavuusraportti htmlcov-hakemistoon:

```
poetry run invoke coverage-report
```

## Pylint

Suorita Pylint-tarkistus:

```
poetry run invoke lint
```
