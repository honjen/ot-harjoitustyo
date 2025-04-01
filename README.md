# Ohjelmistotekniikka, harjoitustyö: korttipeli

Sovellus on digitaalinen tekstipohjainen versio korttipelistä, jossa pelaajat pyrkivät pääsemään eroon korteistaan noudattaen pelin sääntöjä. Kortteja voi pelata, jos ne vastaavat värin tai numeron (0-9) perusteella pöydällä olevaa korttia. Pelissä tulee olemaan myös erikoiskortteja, jotka voivat vaikuttaa pelin kulkuun. Sovellus tarjoaa yksinpelin tekoälyvastustajaa vastaan.

Pelistä puuttuvat vielä lähiaikoina lisättävät ominaisuudet kuten:
- erikoiskortit
- mahdollisuus voittaa/hävitä ja pelata uusi peli
- pakan uudelleen sekoitus
- tekoälyn toimintoihin lisättävä viive
- pelaajan korttien laitto järjestykseen
- grafiikat

Vaatimusmäärittelystä löytyy tarkemmin tietoa sovelluksesta sekä lisää jatkokehitysideoita. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/honjen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

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

Valitse pelattava kortti (numero tai väri on sama kuin poistopakan ylin kortti) painamalla jotain kirjainta (a-z). Jos sinulla ei ole pelattavaa korttia niin paina enter ja saat kortin lisää. Tässä pelin versiossa on vain perustoiminnallisuus ja siitä puuttuu erikoiskortit, joten voit vaan pelataan kortteja vuorotellen tietokonetta vastaan, mutta peliä ei voi vielä voittaa/hävitä ja se loppuu viimeistään kun pakan kortit loppuvat. Voit sulkea sovelluksen milloin tahansa painamalla yläkulman ruksia.

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




