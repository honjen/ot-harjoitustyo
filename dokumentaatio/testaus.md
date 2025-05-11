# Testausdokumentti

## Yksikkö- ja integraatiotestaus

Sovelluksen eri moduuleja ja luokkia on testattu automatisoitujen testien avulla. Testit keskittyvät yksittäisten komponenttien toiminnallisuuteen eristyksissä sekä niiden väliseen yhteistoimintaan.

### Pakan hallinta

Pakan toiminnallisuudesta vastaavaa `CardDeck`-luokkaa (`deck.py`) testataan `test_deck.py`-tiedostossa sijaitsevalla `TestCardDeck`-testiluokalla. Testit tarkistavat pakan oikeanlaisen alustamisen, korttien nostamisen, poistopakan käyttöä pakan tyhjentyessä sekä ensimmäisen kortin noston erityistapauksen.

### Pelilogiikka

Pelilogiikasta vastaavaa `Game`-luokkaa (`game.py`) testataan `test_game.py`-tiedostossa sijaitsevalla `TestGame`-testiluokalla. Testeissä käytetään `unittest.mock`-kirjastoa riippuvuuksien, kuten käyttöliittymärenderöinnin (`FakeRenderer`) ja ulkoisten Pygame-kutsujen, simuloimiseen. Testit kattavat keskeiset pelimekaniikat, kuten pelin päättymistilanteiden tarkistuksen, korttien pelaamisen, erikoiskorttien efektien soveltamisen sekä tekoälyn vuoron toiminnan.

### Pelaajan ja Tekoälyn toiminta

Pelaajan ja tekoälyn perustoiminnallisuudesta vastaavaa `Player`-luokkaa (`player.py`) testataan `test_player.py`-tiedostossa sijaitsevalla `TestPlayer`-testiluokalla. Koska tekoäly on `Player`-luokan ilmentymä, tämä testiluokka kattaa myös tekoälyn perustoimintoja. Testit tarkistavat pelaajan käden alustamisen, korttien nostamisen pakasta ja käteen sekä kortin pelaamisen kädestä annettujen sääntöjen mukaisesti.

### Testauskattavuus
Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 75%. Testikattavuuden ulkopuolelle jäivät build.py, initialize_database.py, main.py, renderer.py, menu.py, sekä osa game.pysta (käytetty # pragma: no cover), koska nämä osat liittyvät käyttöliittymään.

## Järjestelmätestaus

On yritetty tarkistaa, että kaikki määrittelydokumentissa olevat toiminnallisuudet toimivat oikein.
