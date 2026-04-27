# Created by Jan Ivicic © 2025 - 2026

class Lang:
    def __init__(self):
        self.en = {
                    "Piškvorky" : "Tic-Tac-Toe",

                    "Hráč vs. Hráč": "Player vs Player",
                    "Hráč vs. Počítač": "Player vs Computer",
                    "Hráč vs. Počítač EASY": "Player vs Computer EASY",
                    "Hráč vs. Počítač MEDIUM": "Player vs Computer MEDIUM",
                    "Hráč vs. Počítač HARD": "Player vs Computer HARD",
                    "Hráč vs. Počítač EXPERT": "Player vs Computer EXPERT",
                    "Hráč vs. Hráč CHAOS": "Player vs Player CHAOS",
                    "Hráč vs. Počítač CHAOS": "Player vs Computer CHAOS",
                    "Tréning s AI": "Training with AI",

                    "Hráč 1": "Player 1",
                    "Hráč 2": "Player 2",
                    "AI hráč": "AI Player",

                    "Vitaj v hre!": "Welcome to the game!",
                    "Vyber si herný mód:": "Choose game mode:",
                    "Vyber si veľkosť hracej plochy:": "Choose board size:",
                    "Zadaj meno:": "Enter name:",
                    "Vyber si farbu:": "Choose color:",
                    "POTVRDIŤ A ZAČAŤ HRU": "CONFIRM AND START GAME",

                    "Aký ťah by si urobil?": "What move would you make?",
                    "Výborný ťah!": "Excellent move!",
                    "Toto je ideálny ťah, pretože:": "This is the ideal move because:",

                    "na ťahu:": "on turn:",
                    "Víťaz:": "Winner:",
                    "Kliknutím začnete novú hru.": "Click to start a new game.",
                    "Je to remíza!": "It's a draw!",

                    "Tento ťah vedie k okamžitej výhre.": "This move leads to an immediate win.",
                    "Tento ťah blokuje výhru súpera.": "This move blocks the opponent's win.",
                    "Stred je strategicky najsilnejšia pozícia.": "The center is the strongest strategic position.",
                    "Rohy sú výhodné pre budovanie výhry.": "Corners are advantageous for building a win.",
                    "Toto je najlepší strategický ťah.": "This is the best strategic move."
                  }
        
        self.de = {
                    "Piškvorky" : "Drei gewinnt",

                    "Hráč vs. Hráč": "Spieler gegen Spieler",
                    "Hráč vs. Počítač": "Spieler gegen Computer",
                    "Hráč vs. Počítač EASY": "Spieler gegen Computer EASY",
                    "Hráč vs. Počítač MEDIUM": "Spieler gegen Computer MEDIUM",
                    "Hráč vs. Počítač HARD": "Spieler gegen Computer HARD",
                    "Hráč vs. Počítač EXPERT": "Spieler gegen Computer EXPERT",
                    "Hráč vs. Hráč CHAOS": "Spieler gegen Spieler CHAOS",
                    "Hráč vs. Počítač CHAOS": "Spieler gegen Computer CHAOS",
                    "Tréning s AI": "Training mit KI",

                    "Hráč 1": "Spieler 1",
                    "Hráč 2": "Spieler 2",
                    "AI hráč": "KI-Spieler",

                    "Vitaj v hre!": "Willkommen im Spiel!",
                    "Vyber si herný mód:": "Wähle den Spielmodus:",
                    "Vyber si veľkosť hracej plochy:": "Wähle die Spielfeldgröße:",
                    "Zadaj meno:": "Gib einen Namen ein:",
                    "Vyber si farbu:": "Wähle eine Farbe:",
                    "POTVRDIŤ A ZAČAŤ HRU": "BESTÄTIGEN UND SPIEL STARTEN",

                    "Aký ťah by si urobil?": "Welchen Zug würdest du machen?",
                    "Výborný ťah!": "Ausgezeichneter Zug!",
                    "Toto je ideálny ťah, pretože:": "Dies ist der ideale Zug, weil:",

                    "na ťahu:": "am Zug:",
                    "Víťaz:": "Gewinner:",
                    "Kliknutím začnete novú hru.": "Klicken Sie, um ein neues Spiel zu starten.",
                    "Je to remíza!": "Unentschieden!",

                    "Tento ťah vedie k okamžitej výhre.": "Dieser Zug führt zu einem sofortigen Sieg.",
                    "Tento ťah blokuje výhru súpera.": "Dieser Zug blockiert den Sieg des Gegners.",
                    "Stred je strategicky najsilnejšia pozícia.": "Die Mitte ist die strategisch stärkste Position.",
                    "Rohy sú výhodné pre budovanie výhry.": "Ecken sind vorteilhaft für den Siegaufbau.",
                    "Toto je najlepší strategický ťah.": "Dies ist der beste strategische Zug."
                  }

    def translate(self, lang, text):
        if lang == "en":
            return self.en.get(text, text)
        elif lang == "de":
            return self.de.get(text, text)
        else:
            return text