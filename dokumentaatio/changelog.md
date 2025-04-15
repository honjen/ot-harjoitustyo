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
