# Korttipeli

Korttipeli-sovellus on digitaalinen tekstipohjainen versio korttipelistä, jossa pelaajat pyrkivät pääsemään eroon korteistaan noudattaen pelin sääntöjä. Kortteja voi pelata, jos ne vastaavat värin tai numeron (0-9) perusteella pöydällä olevaa korttia. Pelissä on myös erikoiskortteja, jotka voivat vaikuttaa pelin kulkuun. Sovellus tarjoaa yksinpelin tekoälyvastustajaa vastaan.

Vaatimusmäärittelystä löytyy tarkemmin tietoa sovelluksesta sekä lisää jatkokehitysideoita. 

## Uusin release
[Viikko 7 release](https://github.com/honjen/ot-harjoitustyo/releases/tag/viikko7)

## Dokumentaatio

[Käyttöohje](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Changelog](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Testausdokumentti](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

[Työaikakirjanpito](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)


## Ohjelman käynnistäminen

1. Ennen ohjelman käynnistämistä, asenna riippuvuudet:

```
poetry install
```

2. Käynnistä ohjelma:

```
poetry run invoke build
```

3. Käynnistä ohjelma:

```
poetry run invoke start
```

## Pelaaminen

Valitse pelattava kortti (numero tai väri on sama kuin poistopakan ylin kortti) liikkumalla WASD tai nuolinäppäimillä ja valitse kortti painamalla ENTER. Jos sinulla ei ole pelattavaa korttia niin paina SPACE ja saat kortin lisää. Peliin on lisätty värillisiä erikoiskortteja, kuten ohitus ja suunnanvaihto, nosta 2, villi-kortti, villi nosta 4. Kun pelaaja tai tietokone pääsee eroon korteistaan peli loppuu (voitto/häviö) ja voit valita haluatko pelata uuden pelin. Voit sulkea sovelluksen milloin tahansa painamalla yläkulman ruksia.

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
