## Sovelluslogiikka

```mermaid
classDiagram
    Game "1" --> "1" CardDeck
    Game "1" --> "2" Player
    Player "*" --> "1" CardDeck
```
