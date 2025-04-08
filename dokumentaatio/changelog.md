## Viikko 3

- Peli käynnistyy, ja siinä voi pelata kortteja tietokonetta vastaan mutta ei voi vielä voittaa/hävitä
- Lisätty CardDeck-luokka, joka tekee korttipakan ja sekoittaa kortit satunnaisesti
- Lisätty Game-luokka, joka hallitsee pelin logiikkaa, kuten vuoroja ja korttien pelaamista
- Lisätty Player-luokka, joka hallitsee pelaajan kortteja, niiden pelaamista ja nostamista pakasta
- Lisätty GameRenderer-luokka, joka renderöi pelin näkymän Pygame-kirjastolla
- Testattu, että Player-luokka tekee pelaajan käden oikealla määrällä kortteja ja nostaa kortteja oikein

## Viikko 4

- Käyttäjä voi voittaa/hävitä pelin
- Käyttäjä voi aloittaa uuden pelin voitettuaan/hävittyään
- Käyttäjä voi pelata pidempään kuin aikaisemmin, koska poistopakka sekoitetaan nostopakkaan tarvittaessa
- Testattu, että kelvollisen kortin pelaaminen toimii oikein (kortti on samanvärinen kuin pelissä oleva kortti)
- Testattu, että virheellisen kortin pelaaminen ei onnistu (kortti on eri väriä ja arvoa kuin pelissä oleva kortti)
