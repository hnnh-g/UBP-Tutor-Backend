# Petri-Netze

## Petri-Netze: Einsatzgebiete

- Geschäftsvorgänge, betriebliche Organisationsstrukturen, Behördenwege, (Computer-)Kommunikation, Bedienungsanleitungen, Bauanleitungen
- Diese beinhalten Prozesse, bei denen durch Ereignisse und Aktivitäten der Systemzustand verändert wird
- Der Systemzustand wird gekennzeichnet durch:
  - Abstrakte (Zahlen oder Genehmigungen) oder materielle (Bauteile, Werkzeuge oder Münzen) Objekte, die benötigt, verbraucht oder erzeugt werden, sowie
  - Bedingungen (z.B. ein Gegenstand liegt an einem Ort vor) oder Tatsachen (Variable muss Wert x haben), welche benötigt, aufgehoben oder herbeigeführt werden.

## Petri-Netze: Geschichte

- Carl Adam Petri (1926–2010): Kommunikation mit Automaten (Dissertationsschrift 1962)
- Zunächst unbeachtet, erst durch die Softwarekrise praktische Relevanz
- Eingesetzt in vielen Anwendungsgebieten:
  - Betriebssystemmodellierung
  - Workflow-Management
  - Softwareentwicklung
  - Geschäftsprozessmodellierung

## Petri-Netze als Graph

Ein Petri-Netz ist ein gerichteter, bipartiter Graph.

Bipartit: Es gibt zwei Arten von Knoten und jede Kante verbindet einen Knoten der einen Art mit einem der anderen.

Elemente:
- Knoten „Stelle" (Place) — dargestellt als Kreis
- Knoten „Transition" — dargestellt als Rechteck
- Gerichtete Kante — verbindet immer eine Stelle mit einer Transition oder umgekehrt (Transition→Stelle oder Stelle→Transition). Kanten zwischen zwei Stellen oder zwei Transitionen sind nicht erlaubt.

## Beispiel Bibliotheksbenutzung

- Transitionen repräsentieren Ereignisse
- Stellen repräsentieren Objekte und Bedingungen
- Eine Stelle kann markiert werden; die Marke (Token) zeigt, dass eine Bedingung bzw. ein Objekt vorliegt
- Markierung aller Stellen bestimmt den Systemzustand

## Bedingungs/Ereignis-Netze: Definitionen

**Definition 1**

Ein Netz ist ein Tripel N = (S, T, F) mit:
- (i) einer Menge S = {s₁, s₂, …, sₙ} von Stellen,
- (ii) einer Menge T = {t₁, t₂, …, tₘ} von Transitionen,
- (iii) S ∩ T = ∅ und
- (iv) einer zweistelligen Flussrelation F ⊆ (S×T) ∪ (T×S) als Menge der Kanten.

**Definition 2**

Sei N = (S, T, F) ein Netz. Für einen Knoten x ∈ (S ∪ T) ist:
- (i) •x = {y ∈ (S ∪ T) | (y, x) ∈ F} der Vorbereich und
- (ii) x• = {y ∈ (S ∪ T) | (x, y) ∈ F} der Nachbereich von x.

## Netze: Definitionen

**Definition 3**

Sei N = (S, T, F) ein Netz.
- (i) Eine Teilmenge c ⊆ S heißt Fall oder Markierung.
- (ii) Eine Transition t ∈ T ist c-aktiviert, genau dann wenn •t ⊆ c ∧ t•∩c = ∅.
- (iii) Sei t ∈ T c-aktiviert mit c ⊆ S. c' = (c \ •t) ∪ t• heißt Folgefall oder Folgemarkierung von c unter t. Notation: c >ₜ c'

- Alle markierten Stellen bilden die Menge, den Systemzustand
- Ist eine Transition c-aktiviert, „schaltet" oder „feuert" sie:
  - Marken im Vorbereich werden vernichtet
  - Marken im Nachbereich werden erzeugt
- Es entsteht die Folgemarkierung c', der neue Systemzustand

## Schalten eines Petri-Netzes

Schaltbedingungen:
- Eine Transition darf feuern, wenn alle Stellen im Vorbereich markiert und alle Stellen im Nachbereich leer (unmarkiert) sind.
- Feuert die Transition, werden Marken im Vorbereich vernichtet und Stellen im Nachbereich mit Marken gefüllt.
- Nicht erlaubt: Transition feuert obwohl Nachbereichsstelle bereits markiert ist (B/E-Netz), oder Transitionen teilen sich keine Vorbereichsstellen und schalten unabhängig.

## Schaltbeispiel – Bibliotheksbenutzung

Die folgenden PNML-Dokumente zeigen das Bibliotheksnetz in verschiedenen Markierungszuständen.

**Nach dem Feuern von „Nutzer trifft ein" → C₁:** Nutzer an Theke = 1 Token, Buch ausleihbar = 1 Token. Transition „Ausleihe" ist jetzt aktiviert (•Ausleihe ⊆ C₁ und Ausleihe• ∩ C₁ = ∅).

**Nach dem Feuern von „Ausleihe" → C₂:** Nutzer an Theke = 0, Buch ausleihbar = 0. Keine Transition mehr aktiviert.

**Nach dem Feuern von „Rückgabe" statt „Ausleihe" → C₃ (wenn Nutzer an Theke markiert, Buch auch):** Nutzer an Theke = 1, Buch ausleihbar = 1. „Rückgabe" aktiviert, wenn •Rückgabe ⊆ c und Rückgabe•∩c = ∅.

## Beispiel – Jahreszeiten

Zyklisches Petri-Netz mit vier Jahreszeiten als Stellen und vier Transitions für Saisonwechsel. Anfangsmarkierung: Winter = 1, Nicht Herbst = 1, Winter oder Frühling = 1.

## Zusammenfassung Stellen, Marken, Transitionen

- Stellen können markiert oder unmarkiert sein (repräsentierte Bedingung wahr oder falsch, Objekt vorhanden oder nicht vorhanden)
- Markierung gibt Systemzustand an
- Transitionen verändern den Systemzustand, also die Markierung:
  - Können nur feuern, wenn Marken im Vorbereich vorhanden und Stellen im Nachbereich frei sind
  - Marken vor der Transition werden vernichtet, Stellen im Nachbereich gefüllt

## Grundsituationen – Kausalität

Kausalität wird durch die Verbindung von Stellen und Transitionen erreicht:
- Schalten von t führt **genau** zum Schalten von t' (1 Vorbereichsstelle, 1 Nachbereichsstelle)
- Schalten von t **notwendig** für Schalten von t' (mehrere Eingangskanten in t')
- Schalten von t₁ oder t₂ **hinreichend** für Schalten von t' (mehrere Kanten in eine gemeinsame Stelle)

## Grundsituationen – Nebenläufigkeit

Nebenläufige oder konkurrierende Prozesse können abgebildet werden.

**Definition 4**

Sei N = (S, T, F) ein Netz, M und M' Markierungen von N und G ⊆ T eine Menge von Transitionen. Dann heißt G Schritt von M nach M' (M >_G M'), falls gilt:
- (i) ∀t ∈ G ist t M-aktiviert,
- (ii) t₁, t₂ ∈ G ∧ t₁ ≠ t₂ ⇒ •t₁∩•t₂ = ∅ = t₁•∩t₂• und
- (iii) M' = (M \ •G) ∪ G• mit •G = ⋃_{t∈G} •t und G• analog.

- Schaltreihenfolge der Transitionen aus G unerheblich, können also „gleichzeitig" feuern => Parallelität
- G ist nebenläufig aktiviert

**Fork** – Aufspaltung von Prozessen: eine Transition mit mehreren Nachbereichsstellen.

**Join** – Zusammenführung von Prozessen: mehrere Stellen als Vorbereich einer Transition.

Sobald „Aufteilen" feuert, sind „Haare schneiden" und „Maniküre" nebenläufig aktiviert (G = {t_haare_schneiden, t_maniküre} ist ein Schritt).

## Grundsituationen – Konflikt

**Definition 5**

Gilt für einen Fall c und zwei c-aktivierte Ereignisse e₁, e₂: •e₁ ∩ •e₂ ≠ ∅, dann liegt eine Konfliktsituation vor.

- Ereignisse benötigen dieselben Ressourcen/Bedingungen
- Können nur alternativ eintreten ⇒ Schaltung nicht deterministisch

## Grundsituationen – Kontakt

**Definition 6**

Gilt für einen Fall c: •e ⊆ c ∧ e•∩c ≠ ∅, dann liegt eine Kontaktsituation vor.

- Nachbereich eines Ereignisses ist nicht frei
- Schaltreihenfolge der aktivierten Transitionen nicht beliebig

## Konflikt und Kontakt

Konflikt/Kontakt: Ereignisse, die nur alternativ zueinander eintreten können, weil sie gemeinsame Vor- oder Nachbedingungen besitzen, stehen in einem Konflikt/Kontakt zueinander. Kein Konflikt/Kontakt besteht, wenn zu einem bestimmten Zeitpunkt mehrere Transitionen schalten können, aber keine gemeinsamen Vor- und Nachbedingungen bestehen.

## Grundsituationen – Konfusion

Entscheidet die Reihenfolge eintretender Ereignisse, ob ein Konflikt bzw. ein Kontakt entsteht oder nicht, liegt eine Konfusion vor.

## Bedingungs-Ereignis-Netze

Stellen sind Bedingungen, Transitionen sind Ereignisse.

**Definition 7**

Ein Quadrupel Σ = (B, E, F, C) heißt Bedingungs-Ereignis-Netz, falls gilt:
- (i) (B, E, F) ist ein schlichtes Netz ohne isolierte Elemente.
- (ii) C ⊆ P(B) ist eine Äquivalenzklasse der Erreichbarkeitsrelation R_Σ = (r_Σ ∪ r_Σ⁻¹)*. Dabei ist r_Σ ⊆ P(B) × P(B) und c₁ r_Σ c₂ ⟺ ∃G ⊆ E mit c₁ >_G c₂. C heißt Fallklasse von Σ.
- (iii) ∀e ∈ E ∃c ∈ C, so dass e c-aktiviert ist.

- C enthält also alle erreichbaren Markierungen
- Jedes Ereignis ist unter min. einer Markierung aktiviert

## Lebendige B/E-Netze

**Definition 8**

Sei Σ = (B, E, F, C) ein B/E-Netz.
- (i) Ein Fall c ∈ C heißt tot in Σ, wenn kein Ereignis aus E c-aktiviert ist.
- (ii) Ein Ereignis e ∈ E heißt tot im Fall c, wenn es kein c' mit c r_Σ c' gibt, bei dem e c'-aktiviert ist.
- (iii) Ein Ereignis e ∈ E ist lebendig im Fall c, wenn es in keinem Fall c' mit c r_Σ c' tot ist.
- (iv) Ein Fall c ∈ C wird lebendig genannt, wenn alle Transitionen aus E in c lebendig sind.
- (v) Das B/E-Netz Σ heißt lebendig, wenn alle Fälle in C lebendig sind.

Dies lässt sich auf andere Arten von Petri-Netzen verallgemeinern.

## Stellen/Transitionen-Netze

**Definition 9**

Ein Sextupel N = (S, T, F, K, W, m₀) heißt Stellen/Transitionen-Netz (S/T-Netz) bzw. Petri-Netz, wenn gilt:
- (i) (S, T, F) ist ein Netz,
- (ii) K : S → ℕ₊ ∪ {∞} ist die Kapazitätsfunktion,
- (iii) W : F → ℕ₊ ist die Gewichtsfunktion und
- (iv) m₀ : S → ℕ₀ ∪ {∞} ist die Anfangsmarkierung, wobei ∀s ∈ S : m₀(s) ≤ K(s).

**Folgerung:** Ein B/E-Netz (B, E, F, C) kann in ein Petri-Netz N = (B, E, F, K, W, m₀) überführt werden mit K : B → 1, W : F → 1 und m₀(s) = 1 falls s ∈ c, sonst 0, für ein c ∈ C.

## Dimensionen und Kapazitäten

**Dimensionen (Kantengewichte):** Beschriftung von Verbindungen. Legen die Anzahl von erzeugten bzw. verbrauchten Marken beim Schalten einer Transition fest. Wenn keine Angabe, dann 1.

**Kapazitäten (Stellenkapazitäten):** Beschriftung von Stellen. Legen die Höchstgrenze für die Anzahl von Token in einer Stelle fest. Wenn keine Beschriftung, dann k = 1.

## Stellen/Transitionen-Netze: Schaltregel

**Definition 10**

Sei N = (S, T, F, K, W, m₀) ein Petri Netz, m eine Markierung von N und t eine Transition aus T. Dann gilt:
- (i) t ist m-aktiviert, wenn für alle s ∈ •t gilt: m(s) ≥ W(s, t) und für alle s ∈ t• gilt: m(s) + W(t, s) ≤ K(s).
- (ii) Ist t m-aktiviert, kann t schalten, wodurch die Markierung m' entsteht, die durch:

  m'(s) = m(s) − W(s,t) + W(t,s), falls s ∈ •t ∧ s ∈ t•  
  m'(s) = m(s) − W(s,t),          falls s ∈ •t ∧ s ∉ t•  
  m'(s) = m(s) + W(t,s),          falls s ∉ •t ∧ s ∈ t•  
  m'(s) = m(s),                    falls s ∉ •t ∧ s ∉ t•  

  definiert ist.

## Stellen/Transitionen-Netze: Beispiel – Erzeuger-Verbraucher-System

Zwei zyklische Prozesse (Erzeuger links, Verbraucher rechts), verbunden über einen gemeinsamen Speicher mit Kapazität k = 6. Erzeuger legt jeweils 2 Marken in den Speicher, Verbraucher entnimmt jeweils 3. Verbraucher hat einen Pufferspeicher mit k = 2.

Anfangsmarkierung: Erzeuger-bereit = 1, Verbraucher-bereit = 1, Speicher = 0, Verbraucher-Puffer = 0.

## Beispiel – Formel 1

S/T-Netz: Formel-1-Rennen mit Runden, Boxenstopps und Tankfüllung.

Stellen: Auto (1 Token), Tank (4 Token, k=10), Rundenanzahl (1 Token, k=4), Runden zu fahren (4 Token, k=4), Auto unterwegs, Auto in der Box, Ziel erreicht.  
Transitionen: Runde beginnen (W(Tank→t)=3), Runde komplettieren, Rennen beenden (W(Rundenanzahl→t)=4), Tanken (W(t→Tank)=9), Zurück zur Strecke.

## Lebendigkeit in Petri-Netzen

**Deadlock** – Eine Markierung, unter der keine Transition lebendig ist (tote Markierung).

Formal: Ein Deadlock ist eine Stellenmenge S, die – wenn sie einmal unmarkiert ist – genau dann nie wieder markiert werden kann, wenn keine Transition mehr schalten kann, die in ihrem Nachbereich eine Stelle aus S hat.

Praktisch: Ein Deadlock liegt vor, wenn ein Teilnetz durch eine (ungünstige) Schaltfolge lahmgelegt werden kann.

**Trap** – Eine Stelle, die einmal markiert, unter keiner Folgemarkierung unmarkiert ist.

## Lebendigkeit in Petri-Netzen

Eine Transition heißt:
- **tot**, wenn sie bei keinem der möglichen Folgezustände (Folgemarkierung) aktiviert ist, d. h. nie wieder schalten kann
- **aktivierbar**, wenn sie unter mindestens einer Folgemarkierung aktiviert ist
- **lebendig**, wenn sie unter allen Folgemarkierungen aktivierbar ist

Ein Petri-Netz heißt:
- **tot**, wenn alle Transitionen tot sind
- **deadlockfrei** oder **schwach lebendig**, falls es unter keiner Folgemarkierung tot ist, d. h. bei jeder Folgemarkierung mindestens eine Transition aktivierbar ist
- **(stark) lebendig**, wenn alle Transitionen lebendig sind

## Weitere Eigenschaften

- **Terminierung** – Ein Petri-Netz terminiert unter einer bestimmten Anfangsmarkierung, wenn jede Schaltsequenz zu einem Deadlock führt.
- **Reversibilität** – Ein Petri-Netz, das aus jedem seiner Zustände in seinen Anfangszustand zurückkehren kann, wird rücksetzbar genannt.
- **k-Beschränktheit** – Jede Stelle enthält unter jeder Folgemarkierung maximal k Marken.
- In einem Petri-Netz können diese Eigenschaften nachgewiesen werden, jedoch sind die nötigen Algorithmen oft zu komplex für die Praxis.

## Erreichbarkeitsgraph

Der Erreichbarkeitsgraph enthält alle von der Anfangsmarkierung erreichbaren Markierungen. Er wird als gerichteter Graph dargestellt, in dem Knoten Markierungen und Kanten Transitionen repräsentieren.

**Beispiel Erzeuger-Verbraucher-System** (Stellen s1…s5):

Anfangsmarkierung: (s1=1, s2=0, s3=1, s4=0, s5=2) — kurz: (1,0,1,0,2)

```
(1,0,1,0,2) --t1,t3--> (0,1,4,1,0)
                              |
                             t2
                              ↓
                        (1,0,2,1,0) <--t1-- (0,1,2,1,0)
                                                 ↑
                                                t2,t4
                                                 |
(1,0,0,0,2) <--t1,t3-- (0,1,3,1,0) <--t2,t4-- (1,0,1,0,2)
```

Markierungstupel: (s1, s2, s3, s4, s5)
- t2 und t4 sind nebenläufig aktiviert (Schritt)
- t1 und t3 sind nebenläufig aktiviert (Schritt)
- Das Netz ist lebendig, reversibel, deadlockfrei, trapfrei und beschränkt (k=4 für s3).

## Strukturelle Analyse von Petri-Netzen

- Verhalten eines Petri-Netzes (z.B. Beschränktheit, Lebendigkeit) kann u.U. durch Analyse der Struktur bestimmt werden.
- Entspricht die Struktur eines Petri-Netzes bestimmten Anforderungen, können Verhaltenseigenschaften abgeleitet werden.
- Beispiele: (extended) Free Choice Nets, Marked Graphs, State Machines.

## Unterarten von Petri-Netzen: Marked Graph

„Markierter Graph"

Ein Petri-Netz heißt Markierter Graph, wenn jede Stelle genau eine ausgehende und eine eingehende Kante hat:
- Konflikte sind nicht möglich
- Nebenläufigkeit kann abgebildet werden
- Bei einer Marke lebendig und reversibel
- Kann ohne Informationsverlust als Aktivitätsdiagramm abgebildet werden (Stellen als Pfeile)
- Zur Abbildung nicht-deterministischer Prozesse aufgrund von Nebenläufigkeit

**Beispiel:** Der Friseursalon als Markierter Graph (jede Stelle hat genau je eine ein- und ausgehende Kante).

## Unterarten von Petri-Netzen: State Machine

(Finiter) „Zustandsautomat"

Ein Petri-Netz heißt State Machine, wenn jede Transition genau eine eingehende und eine ausgehende Kante besitzt:
- Keine Nebenläufigkeit
- Konflikte sind möglich
- Kein Erzeugen/Verbrauchen von Marken ⇒ 1-beschränkt
- Bei einer Marke lebendig und reversibel
- Kann ohne Informationsverlust als Zustandsdiagramm abgebildet werden (Transitionen als Pfeile)
- Zur Abbildung nicht-deterministischer Prozesse aufgrund von geteilten Ressourcen

| | Erlaubt | Nicht Erlaubt |
|---|---|---|
| **Marked Graph** | Stelle mit je 1 ein- und ausgehender Kante | Stelle mit 2 eingehenden Kanten von unterschiedlichen Transitionen |
| **State Machine** | Transition mit je 1 ein- und ausgehender Kante | Transition mit 3 ausgehenden Kanten |

## Unterarten von Petri-Netzen: Free Choice Net

„Freie-Wahl-Netz"

Jede Kante von einer Stelle zu einer Transition ist entweder:
- Die einzige Kante, die in dieser Stelle beginnt, oder
- Die einzige Kante, die an dieser Transition endet
- Nebenläufigkeit und Konflikte sind möglich, aber nicht gleichzeitig

Die Wahl zwischen dem Feuern zweier Transitionen ist niemals abhängig vom Rest des Netzes: Wenn eine Transition im Nachbereich einer Stelle aktiviert ist, sind alle Transitionen im Nachbereich dieser Stelle aktiviert.

**Extended Free Choice Net (EFCN):** Kann in ein FCN überführt werden. Existiert eine Kante von einer Stelle s zu einer Transition, dann existiert eine Kante von allen Stellen vor dieser Transition zu jeder Transition im Nachbereich von s.

Ist ein (e)FCN frei von Deadlocks und Traps, ist es lebendig.

## Unterarten von Petri-Netzen: Zusammenfassung

Hierarchie der Unterarten (von speziell nach allgemein):
- **Marked Graph** und **State Machine** sind Teilmengen des **Free Choice Net**
- Free Choice Net ⊆ Extended Free Choice Net ⊆ **Petri Net (allgemein)**

## Hörsaalübung: Münzautomat

Das Verhalten eines Münzautomaten soll modelliert werden:
- Der Automat steht bereit, wenn keine Münzen im Automaten sind
- Eine Münze kann in den bereitstehenden Automaten eingeworfen werden
- Ist eine Münze im Automaten, kann entweder zum Zustand der Bereitschaft abgebrochen werden oder ein Artikel ausgewählt werden
- Ist ein Artikel ausgewählt, wird dieser ausgegeben und der Automat steht erneut bereit

Erweiterungen:
- Es befinden sich fünf Artikel im Automaten. Ist der Automat leer, werden alle Artikel wieder aufgefüllt.
- Ein Artikel kostet 50 ct, es werden 10 ct und 20 ct Münzen angenommen. Werden zuviele Münzen eingeworfen, verbleiben diese im Automaten.

## Zusammenfassung

- Petri-Netze geeignet zur Modellierung logischer und nebenläufiger Prozesse
- Bestehen aus Stellen (Zustände, Bedingungen) und Transitionen (Ereignisse, Veränderungen)
- Markierte Stellen geben an, welche Zustände/Bedingungen gelten
- Stellen/Transitionen-Netze erweitern Bedingungs/Ereignis-Netze um Kantengewichte und Kapazitäten
- Verhaltenseigenschaften wie Lebendigkeit oder Beschränktheit können durch den Erreichbarkeitsgraph oder durch strukturelle Analyse bestimmt werden
