# Assumption Mapping Matrix, Wichtigkeit × Beleglage

Framework, um zu entscheiden, welche Annahmen zuerst Testaufwand verdienen und welche man vorerst
unvalidiert stehen lassen kann. Aus Lean-Startup-Praxis (Ash Maurya, David Bland, "Testing Business
Ideas"), hier für PM-Toolkit-Gebrauch angelegt.

**Ohne dieses Werkzeug:** entweder man behandelt jede Annahme als gleich unsicher und validiert alles
umfänglich (Analyse-Paralyse), oder man vertraut allem gleich stark (blindes Bauen auf ungetesteten
Wetten). Beides bricht. Das Werkzeug entscheidet, wo Vertrauen gerechtfertigt ist und wo nicht.

---

## Die zwei Achsen

- **Wichtigkeit:** Wie viel bricht, wenn diese Annahme falsch ist?
- **Beleglage:** Wie gut ist die Annahme bereits abgesichert (Daten, Logik, frühere Erfahrung)?

## Die vier Felder

| | Niedrige Beleglage | Hohe Beleglage |
|---|---|---|
| **Hohe Wichtigkeit** | **Leap of Faith, zuerst testen.** Die riskanteste, teuerste Fehlerquelle. Billigsten/schnellsten Test dafür bauen, bevor man weiterbaut. | **Fundament, darauf weiterbauen.** Ausreichend abgesichert, um mit Vertrauen darauf zu bauen, ohne es ständig neu zu validieren. |
| **Niedrige Wichtigkeit** | **Beobachten, nicht jetzt testen.** Testaufwand lohnt sich aktuell nicht, im Blick behalten, falls sich die Wichtigkeit später ändert. | **Ignorieren.** Weder Risiko noch Testbedarf, keine Aufmerksamkeit wert. |

## Test, ob eine Annahme First-Principles-fähig ist oder Leap-of-Faith-Territory bleibt

Bleibt die Annahme sinnvoll, wenn man die anderen beteiligten Elemente wegdenkt?
- **Ja** → strukturell/ontologisch, oft über Logik ableitbar, First-Principles-Reasoning greift (Beispiel:
  "der Nutzer ist fundamentaler als der einzelne Vorgang oder Kanal", bleibt wahr unabhängig von Prozess/Kanal).
- **Hängt von menschlichem Verhalten ab** (zahlt wer, nutzt wer, bevorzugt wer) → Leap-of-Faith-Territory,
  egal wie klar die Logik scheint. Nur durch Beobachtung echter Menschen zu klären, nicht durch Ableitung.

---

## Beispiel-Anwendung (illustrativ, keine aktive Analyse)

| Annahme | Wichtigkeit | Beleglage | Feld | Typ |
|---|---|---|---|---|
| Der Nutzer ist die fundamentale Einheit, nicht der einzelne Vorgang/Kanal | Hoch | Hoch (logisch abgeleitet, testet sich selbst über "bleibt ohne die anderen sinnvoll") | Fundament | First Principles |
| Nutzer schließen ein Self-Service-Onboarding allein ab, ohne Setup durch den Support | Hoch | Niedrig (nie getestet) | Leap of Faith | Verhaltens-Annahme |
| Ein neuer Content-Kanal zieht die richtige Zielgruppe an | Hoch | Mittel (frühe Signale, noch offen) | Leap of Faith → wandert je nach Ergebnis Richtung Fundament | Verhaltens-Annahme |

---

## Wie benutzen, wenn's konkret wird

1. Alle relevanten Annahmen für die anstehende Entscheidung auflisten.
2. Jede auf Wichtigkeit und Beleglage einschätzen (grob reicht, keine Scheingenauigkeit).
3. Ins Raster einsortieren.
4. Testaufwand nur ins obere linke Feld stecken (Leap of Faith). Alles andere: bauen, beobachten, oder
   ignorieren, je nach Feld.
