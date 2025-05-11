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

## Viikko 5

- Käyttäjä voi pelata ohituskortteja ja saada toisen vuoron
- Käyttä voi pelata suunnanvaihtokortteja ja saada toisen vuoron
- Käyttäjä voi laittaa vastustajan nostamaan 2 korttia ja menettämään vuoronsa
- Yllämainitut erikoiskortit toimivat myös käyttäjään
- Testattu, että korttipakan koko alussa (100 korttia) on oikein ja kortin nostaminen vähentää pakassa olevien korttien määrää
- Testattu, että kun nostopakassa ei ole kortteja, poistopakka sekoitetaan uudelleen ja toimii oikein
- Testattu, että poistopakkaa ei sekoiteta uudelleen, jos siinä on vain yksi kortti
- Testattu, että peli päättyy, kun pelaajalla ei ole enää kortteja (pelaaja voittaa) tai tietokoneella ei ole enää kortteja (pelaaja häviää)
- Testattu, että peli ei pääty, jos kummallakin pelaajalla on vielä kortteja
- Testattu, että is_valid_play palauttaa True, jos pelattavan kortin väri tai arvo vastaa pelissä olevaa korttia ja se palauttaa False, jos väri ja arvo eivät täsmää pelissä olevaan korttiin

## Viikko 6

- Käyttäjä voi pelata villi-kortin ja valita seuraavaksi pelattavan kortin värin
- Käyttäjä voi pelata villi nosta 4-kortin ja valita seuraavaksi pelattavan värin ja laittaa vastustajan nostamaan 4 korttia sekä menettämään vuoronsa
- Käyttäjä voi pelata kortteja alusta asti koska on varmistettu, että uudet värittömät villit kortit eivät tule poistopakan ensimmäiseksi kortiksi
- Yllämainittu villi-kortti toimii myös käyttäjään
- Yllämainittu villi nosta 4 kortti toimii myös käyttäjään mutta tässä versiossa tietokone ei saa uutta vuoroa (korjataan pian)
- Käyttäjä voi nostaa kaikki kortit pakasta ja silloin peli loppuu tasapeliin
- Käyttäjä voi seurata peliä paremmin nyt kun tietokoneen toimintaan on lisätty pieni viive
- Korjattu virhe koodissa liittyen pelin sulkemiseen
- Testattu, että villiä korttia ei voi nostaa aloituskortiksi
- Testattu, että jos ei ole kortteja mitä nostaa palautuu None
- Testattu, että osa erikoiskorteista toimii

## Viikko 7
- Käyttäjä voi päävalikon kautta aloittaa pelin, katsoa ohjeet, katsoa rankingeja tai poistua
- Käyttäjällä on kivempi pelata nyt kun pelissä on kivoja grafiikoita kuten kortteja  
- Käyttäjä voi selata kortteja WASD näppäimillä ja valita kortin ENTER näppäimellä
- Käyttäjän saamat pisteet tallettuvat tietokantaan
- Käyttäjä voi katsoa parhaimmat pisteet high score sivulta
- Testattu, että tasapelitilanteessa näytetään oikea viesti
- Testattu, että erikoiskortti "nosta 2" ja "villi nosta 4" toimivat AI:lla
- Testattu, että pelaaja voi pelata kelvollisen kortin onnistuneesti
- Testattu, että pisteiden laskeminen erikoiskorteille toimii oikein
- Testattu, että AI nostaa kortin, jos sillä ei ole pelattavaa korttia
