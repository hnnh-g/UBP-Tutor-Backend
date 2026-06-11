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

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="bibliothek" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Bibliotheksbenutzung</text></name>
    <page id="p0">

      <!-- Stellen -->
      <place id="s_nutzer_an_theke">
        <name><text>Nutzer an Theke</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <place id="s_buch_ausleihbar">
        <name><text>Buch ausleihbar</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>

      <!-- Transitionen -->
      <transition id="t_nutzer_trifft_ein">
        <name><text>Nutzer trifft ein</text></name>
      </transition>

      <transition id="t_ausleihe">
        <name><text>Ausleihe</text></name>
      </transition>

      <transition id="t_rueckgabe">
        <name><text>Rückgabe</text></name>
      </transition>

      <!-- Kanten -->
      <arc id="a1" source="t_nutzer_trifft_ein" target="s_nutzer_an_theke">
        <inscription><text>1</text></inscription>
      </arc>
      <arc id="a2" source="s_nutzer_an_theke" target="t_ausleihe">
        <inscription><text>1</text></inscription>
      </arc>
      <arc id="a3" source="s_nutzer_an_theke" target="t_rueckgabe">
        <inscription><text>1</text></inscription>
      </arc>
      <arc id="a4" source="s_buch_ausleihbar" target="t_ausleihe">
        <inscription><text>1</text></inscription>
      </arc>
      <arc id="a5" source="t_rueckgabe" target="s_buch_ausleihbar">
        <inscription><text>1</text></inscription>
      </arc>

    </page>
  </net>
</pnml>
```

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

**Anfangsfall C₀:** Buch ausleihbar = 1 Token, alle anderen Stellen = 0 Token.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="bibliothek_c0" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Bibliotheksbenutzung – Anfangsfall C₀</text></name>
    <page id="p0">

      <place id="s_nutzer_theke">
        <name><text>Nutzer an Theke</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_buch">
        <name><text>Buch ausleihbar</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>

      <transition id="t_eintritt">
        <name><text>Nutzer trifft ein</text></name>
      </transition>
      <transition id="t_ausleihe">
        <name><text>Ausleihe</text></name>
      </transition>
      <transition id="t_rueckgabe">
        <name><text>Rückgabe</text></name>
      </transition>

      <arc id="a1" source="t_eintritt"   target="s_nutzer_theke"/>
      <arc id="a2" source="s_nutzer_theke" target="t_ausleihe"/>
      <arc id="a3" source="s_nutzer_theke" target="t_rueckgabe"/>
      <arc id="a4" source="s_buch"        target="t_ausleihe"/>
      <arc id="a5" source="t_rueckgabe"   target="s_buch"/>

    </page>
  </net>
</pnml>
```

**Nach dem Feuern von „Nutzer trifft ein" → C₁:** Nutzer an Theke = 1 Token, Buch ausleihbar = 1 Token. Transition „Ausleihe" ist jetzt aktiviert (•Ausleihe ⊆ C₁ und Ausleihe• ∩ C₁ = ∅).

**Nach dem Feuern von „Ausleihe" → C₂:** Nutzer an Theke = 0, Buch ausleihbar = 0. Keine Transition mehr aktiviert.

**Nach dem Feuern von „Rückgabe" statt „Ausleihe" → C₃ (wenn Nutzer an Theke markiert, Buch auch):** Nutzer an Theke = 1, Buch ausleihbar = 1. „Rückgabe" aktiviert, wenn •Rückgabe ⊆ c und Rückgabe•∩c = ∅.

## Beispiel – Jahreszeiten

Zyklisches Petri-Netz mit vier Jahreszeiten als Stellen und vier Transitions für Saisonwechsel. Anfangsmarkierung: Winter = 1, Nicht Herbst = 1, Winter oder Frühling = 1.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="jahreszeiten" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Jahreszeiten</text></name>
    <page id="p0">

      <!-- Stellen -->
      <place id="s_fruehling">
        <name><text>Frühling</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_sommer">
        <name><text>Sommer</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_herbst">
        <name><text>Herbst</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_winter">
        <name><text>Winter</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_nicht_herbst">
        <name><text>Nicht Herbst</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_winter_fruehling">
        <name><text>Winter oder Frühling</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>

      <!-- Transitionen -->
      <transition id="t_fruehlingsanfang">
        <name><text>Frühlingsanfang</text></name>
      </transition>
      <transition id="t_sommeranfang">
        <name><text>Sommeranfang</text></name>
      </transition>
      <transition id="t_herbstanfang">
        <name><text>Herbstanfang</text></name>
      </transition>
      <transition id="t_winteranfang">
        <name><text>Winteranfang</text></name>
      </transition>

      <!-- Kanten -->
      <!-- Frühlingsanfang: Winter → Frühling, konsumiert Winter oder Frühling, erzeugt Nicht Herbst -->
      <arc id="a1" source="s_winter"          target="t_fruehlingsanfang"/>
      <arc id="a2" source="t_fruehlingsanfang" target="s_fruehling"/>
      <arc id="a3" source="s_nicht_herbst"    target="t_sommeranfang"/>
      <arc id="a4" source="t_fruehlingsanfang" target="s_nicht_herbst"/>

      <!-- Sommeranfang: Frühling → Sommer -->
      <arc id="a5" source="s_fruehling"  target="t_sommeranfang"/>
      <arc id="a6" source="t_sommeranfang" target="s_sommer"/>
      <arc id="a7" source="s_winter_fruehling" target="t_herbstanfang"/>

      <!-- Herbstanfang: Sommer → Herbst, konsumiert Winter oder Frühling -->
      <arc id="a8" source="s_sommer"      target="t_herbstanfang"/>
      <arc id="a9" source="t_herbstanfang" target="s_herbst"/>

      <!-- Winteranfang: Herbst → Winter, erzeugt Winter oder Frühling, Nicht Herbst -->
      <arc id="a10" source="s_herbst"       target="t_winteranfang"/>
      <arc id="a11" source="t_winteranfang"  target="s_winter"/>
      <arc id="a12" source="t_winteranfang"  target="s_nicht_herbst"/>
      <arc id="a13" source="t_winteranfang"  target="s_winter_fruehling"/>

    </page>
  </net>
</pnml>
```

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

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="kausalitaet" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Grundsituation: Kausalität (genau)</text></name>
    <page id="p0">

      <transition id="t">  <name><text>t</text></name>  </transition>
      <place id="s_mitte"> <name><text>s</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <transition id="t_prime"> <name><text>t'</text></name> </transition>
      <place id="s_out">
        <name><text>s'</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <arc id="a1" source="t"       target="s_mitte"/>
      <arc id="a2" source="s_mitte" target="t_prime"/>
      <arc id="a3" source="t_prime" target="s_out"/>

    </page>
  </net>
</pnml>
```

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

## Nebenläufigkeit Beispiel – Der Friseursalon

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="friseursalon" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Friseursalon</text></name>
    <page id="p0">

      <!-- Stellen -->
      <place id="s_kunde_wartet">
        <name><text>Kunde wartet</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_haare_bereit">
        <name><text>Haare bereit</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_maniküre_bereit">
        <name><text>Maniküre bereit</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_haare_fertig">
        <name><text>Haare fertig</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_maniküre_fertig">
        <name><text>Maniküre fertig</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <!-- Transitionen -->
      <transition id="t_kunde_trifft_ein">
        <name><text>Kunde trifft ein</text></name>
      </transition>
      <transition id="t_fork">
        <name><text>Aufteilen</text></name>
      </transition>
      <transition id="t_haare_schneiden">
        <name><text>Haare schneiden</text></name>
      </transition>
      <transition id="t_maniküre">
        <name><text>Maniküre</text></name>
      </transition>
      <transition id="t_fertig">
        <name><text>Kunde fertig</text></name>
      </transition>

      <!-- Kanten -->
      <arc id="a1" source="t_kunde_trifft_ein" target="s_kunde_wartet"/>
      <arc id="a2" source="s_kunde_wartet"     target="t_fork"/>
      <arc id="a3" source="t_fork"             target="s_haare_bereit"/>
      <arc id="a4" source="t_fork"             target="s_maniküre_bereit"/>
      <arc id="a5" source="s_haare_bereit"     target="t_haare_schneiden"/>
      <arc id="a6" source="s_maniküre_bereit"  target="t_maniküre"/>
      <arc id="a7" source="t_haare_schneiden"  target="s_haare_fertig"/>
      <arc id="a8" source="t_maniküre"         target="s_maniküre_fertig"/>
      <arc id="a9" source="s_haare_fertig"     target="t_fertig"/>
      <arc id="a10" source="s_maniküre_fertig" target="t_fertig"/>

    </page>
  </net>
</pnml>
```

Sobald „Aufteilen" feuert, sind „Haare schneiden" und „Maniküre" nebenläufig aktiviert (G = {t_haare_schneiden, t_maniküre} ist ein Schritt).

## Grundsituationen – Konflikt

**Definition 5**

Gilt für einen Fall c und zwei c-aktivierte Ereignisse e₁, e₂: •e₁ ∩ •e₂ ≠ ∅, dann liegt eine Konfliktsituation vor.

- Ereignisse benötigen dieselben Ressourcen/Bedingungen
- Können nur alternativ eintreten ⇒ Schaltung nicht deterministisch

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="konflikt_ressource" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Konflikt – Betriebsmittel</text></name>
    <page id="p0">

      <place id="s_betriebsmittel">
        <name><text>Betriebsmittel</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <transition id="t_prozess1">
        <name><text>Prozess 1</text></name>
      </transition>
      <transition id="t_prozess2">
        <name><text>Prozess 2</text></name>
      </transition>

      <arc id="a1" source="s_betriebsmittel" target="t_prozess1"/>
      <arc id="a2" source="s_betriebsmittel" target="t_prozess2"/>

    </page>
  </net>
</pnml>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="konflikt_geld" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Konflikt – Geld (Kino oder Party)</text></name>
    <page id="p0">

      <place id="s_geld">
        <name><text>Geld</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <transition id="t_kino">
        <name><text>Kino</text></name>
      </transition>
      <transition id="t_party">
        <name><text>Party</text></name>
      </transition>

      <arc id="a1" source="s_geld" target="t_kino"/>
      <arc id="a2" source="s_geld" target="t_party"/>

    </page>
  </net>
</pnml>
```

## Grundsituationen – Kontakt

**Definition 6**

Gilt für einen Fall c: •e ⊆ c ∧ e•∩c ≠ ∅, dann liegt eine Kontaktsituation vor.

- Nachbereich eines Ereignisses ist nicht frei
- Schaltreihenfolge der aktivierten Transitionen nicht beliebig

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="kontakt" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Kontakt</text></name>
    <page id="p0">

      <place id="s1">
        <name><text>s1</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s2">
        <name><text>s2</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_out">
        <name><text>s_out</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <transition id="t1">
        <name><text>t1</text></name>
      </transition>
      <transition id="t2">
        <name><text>t2</text></name>
      </transition>

      <arc id="a1" source="s1" target="t1"/>
      <arc id="a2" source="s2" target="t2"/>
      <arc id="a3" source="t1" target="s_out"/>
      <arc id="a4" source="t2" target="s_out"/>

    </page>
  </net>
</pnml>
```

## Konflikt und Kontakt

Konflikt/Kontakt: Ereignisse, die nur alternativ zueinander eintreten können, weil sie gemeinsame Vor- oder Nachbedingungen besitzen, stehen in einem Konflikt/Kontakt zueinander. Kein Konflikt/Kontakt besteht, wenn zu einem bestimmten Zeitpunkt mehrere Transitionen schalten können, aber keine gemeinsamen Vor- und Nachbedingungen bestehen.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="kein_konflikt" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Kein Konflikt/Kontakt – unabhängige Prozesse</text></name>
    <page id="p0">

      <place id="s_links">
        <name><text>s_links</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_mitte">
        <name><text>s_mitte</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_rechts">
        <name><text>s_rechts</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <transition id="t_links">
        <name><text>t_links</text></name>
      </transition>
      <transition id="t_rechts">
        <name><text>t_rechts</text></name>
      </transition>

      <arc id="a1" source="s_links"  target="t_links"/>
      <arc id="a2" source="t_links"  target="s_mitte"/>
      <arc id="a3" source="s_rechts" target="t_rechts"/>
      <arc id="a4" source="t_rechts" target="s_mitte"/>

    </page>
  </net>
</pnml>
```

## Grundsituationen – Konfusion

Entscheidet die Reihenfolge eintretender Ereignisse, ob ein Konflikt bzw. ein Kontakt entsteht oder nicht, liegt eine Konfusion vor.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="konfusion" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Konfusion</text></name>
    <page id="p0">

      <place id="s_start">
        <name><text>s_start</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_mitte_oben">
        <name><text>s_mitte_oben</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_mitte_unten">
        <name><text>s_mitte_unten</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_end_oben">
        <name><text>s_end_oben</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_end_unten">
        <name><text>s_end_unten</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <transition id="e1"> <name><text>e1</text></name> </transition>
      <transition id="e2"> <name><text>e2</text></name> </transition>
      <transition id="e3"> <name><text>e3</text></name> </transition>
      <transition id="e4"> <name><text>e4</text></name> </transition>

      <arc id="a1" source="s_start"       target="e1"/>
      <arc id="a2" source="s_start"       target="e2"/>
      <arc id="a3" source="e1"            target="s_mitte_oben"/>
      <arc id="a4" source="e2"            target="s_mitte_unten"/>
      <arc id="a5" source="s_mitte_oben"  target="e3"/>
      <arc id="a6" source="s_mitte_unten" target="e4"/>
      <arc id="a7" source="e3"            target="s_end_oben"/>
      <arc id="a8" source="e4"            target="s_end_unten"/>

    </page>
  </net>
</pnml>
```

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

**Beispiel: Nicht-lebendiges Netz** — Transition feuert einmalig, dann Deadlock:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="nicht_lebendig" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Nicht-lebendiges B/E-Netz</text></name>
    <page id="p0">

      <place id="s_in">
        <name><text>s_in</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_out">
        <name><text>s_out</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <transition id="t">
        <name><text>t</text></name>
      </transition>

      <arc id="a1" source="s_in"  target="t"/>
      <arc id="a2" source="t"     target="s_out"/>

    </page>
  </net>
</pnml>
```

**Beispiel: Lebendiges Netz** — Zyklus, beide Transitionen immer erreichbar:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="lebendig" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Lebendiges B/E-Netz</text></name>
    <page id="p0">

      <place id="s_a">
        <name><text>s_a</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_b">
        <name><text>s_b</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <transition id="t1">
        <name><text>t1</text></name>
      </transition>
      <transition id="t2">
        <name><text>t2</text></name>
      </transition>

      <arc id="a1" source="s_a" target="t1"/>
      <arc id="a2" source="t1"  target="s_b"/>
      <arc id="a3" source="s_b" target="t2"/>
      <arc id="a4" source="t2"  target="s_a"/>

    </page>
  </net>
</pnml>
```

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

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="erzeuger_verbraucher" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Erzeuger-Verbraucher-System</text></name>
    <page id="p0">

      <!-- Stellen Erzeuger-Seite -->
      <place id="s_e_bereit">
        <name><text>Erzeuger bereit</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_e_produziert">
        <name><text>Erzeuger produziert</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <!-- Speicher (gemeinsam, k=6) -->
      <place id="s_speicher">
        <name><text>Speicher</text></name>
        <capacity><text>6</text></capacity>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <!-- Stellen Verbraucher-Seite -->
      <place id="s_v_bereit">
        <name><text>Verbraucher bereit</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_v_puffer">
        <name><text>Verbraucher Puffer</text></name>
        <capacity><text>2</text></capacity>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <!-- Transitionen -->
      <transition id="t_produzieren">
        <name><text>Produzieren</text></name>
      </transition>
      <transition id="t_einlagern">
        <name><text>Einlagern</text></name>
      </transition>
      <transition id="t_entnehmen">
        <name><text>Entnehmen</text></name>
      </transition>
      <transition id="t_verbrauchen">
        <name><text>Verbrauchen</text></name>
      </transition>

      <!-- Kanten Erzeuger-Zyklus -->
      <arc id="a1" source="s_e_bereit"    target="t_produzieren"/>
      <arc id="a2" source="t_produzieren" target="s_e_produziert"/>
      <arc id="a3" source="s_e_produziert" target="t_einlagern"/>
      <arc id="a4" source="t_einlagern"   target="s_e_bereit"/>
      <!-- Einlagern schreibt 2 Marken in Speicher -->
      <arc id="a5" source="t_einlagern"   target="s_speicher">
        <inscription><text>2</text></inscription>
      </arc>

      <!-- Kanten Verbraucher-Zyklus -->
      <!-- Entnehmen liest 3 Marken aus Speicher -->
      <arc id="a6" source="s_speicher"    target="t_entnehmen">
        <inscription><text>3</text></inscription>
      </arc>
      <arc id="a7" source="s_v_bereit"    target="t_entnehmen"/>
      <arc id="a8" source="t_entnehmen"   target="s_v_puffer">
        <inscription><text>2</text></inscription>
      </arc>
      <arc id="a9" source="s_v_puffer"    target="t_verbrauchen">
        <inscription><text>2</text></inscription>
      </arc>
      <arc id="a10" source="t_verbrauchen" target="s_v_bereit">
        <inscription><text>2</text></inscription>
      </arc>

    </page>
  </net>
</pnml>
```

## Beispiel – Formel 1

S/T-Netz: Formel-1-Rennen mit Runden, Boxenstopps und Tankfüllung.

Stellen: Auto (1 Token), Tank (4 Token, k=10), Rundenanzahl (1 Token, k=4), Runden zu fahren (4 Token, k=4), Auto unterwegs, Auto in der Box, Ziel erreicht.  
Transitionen: Runde beginnen (W(Tank→t)=3), Runde komplettieren, Rennen beenden (W(Rundenanzahl→t)=4), Tanken (W(t→Tank)=9), Zurück zur Strecke.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="formel1" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Formel 1 Rennen</text></name>
    <page id="p0">

      <!-- Stellen -->
      <place id="s_auto">
        <name><text>Auto</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_tank">
        <name><text>Tank</text></name>
        <capacity><text>10</text></capacity>
        <initialMarking><text>4</text></initialMarking>
      </place>
      <place id="s_rundenanzahl">
        <name><text>Rundenanzahl</text></name>
        <capacity><text>4</text></capacity>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_runden_zu_fahren">
        <name><text>Runden zu fahren</text></name>
        <capacity><text>4</text></capacity>
        <initialMarking><text>4</text></initialMarking>
      </place>
      <place id="s_auto_unterwegs">
        <name><text>Auto unterwegs</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_auto_box">
        <name><text>Auto in der Box</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_ziel">
        <name><text>Ziel erreicht</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <!-- Transitionen -->
      <transition id="t_runde_beginnen">
        <name><text>Runde beginnen</text></name>
      </transition>
      <transition id="t_runde_komplettieren">
        <name><text>Runde komplettieren</text></name>
      </transition>
      <transition id="t_rennen_beenden">
        <name><text>Rennen beenden</text></name>
      </transition>
      <transition id="t_tanken">
        <name><text>Tanken</text></name>
      </transition>
      <transition id="t_zurueck">
        <name><text>Zurück zur Strecke</text></name>
      </transition>

      <!-- Kanten -->
      <arc id="a1" source="s_auto"            target="t_runde_beginnen"/>
      <arc id="a2" source="s_tank"            target="t_runde_beginnen">
        <inscription><text>3</text></inscription>
      </arc>
      <arc id="a3" source="t_runde_beginnen"  target="s_auto_unterwegs"/>

      <arc id="a4" source="s_auto_unterwegs"      target="t_runde_komplettieren"/>
      <arc id="a5" source="t_runde_komplettieren"  target="s_rundenanzahl"/>
      <arc id="a6" source="s_runden_zu_fahren"     target="t_rennen_beenden">
        <inscription><text>4</text></inscription>
      </arc>

      <arc id="a7" source="s_rundenanzahl"    target="t_rennen_beenden">
        <inscription><text>4</text></inscription>
      </arc>
      <arc id="a8" source="t_rennen_beenden"  target="s_ziel"/>

      <arc id="a9"  source="s_auto_unterwegs" target="t_tanken"/>
      <arc id="a10" source="t_tanken"         target="s_auto_box"/>
      <arc id="a11" source="t_tanken"         target="s_tank">
        <inscription><text>9</text></inscription>
      </arc>
      <arc id="a12" source="s_auto_box"        target="t_zurueck"/>
      <arc id="a13" source="t_zurueck"         target="s_auto"/>

    </page>
  </net>
</pnml>
```

## Lebendigkeit in Petri-Netzen

**Deadlock** – Eine Markierung, unter der keine Transition lebendig ist (tote Markierung).

Formal: Ein Deadlock ist eine Stellenmenge S, die – wenn sie einmal unmarkiert ist – genau dann nie wieder markiert werden kann, wenn keine Transition mehr schalten kann, die in ihrem Nachbereich eine Stelle aus S hat.

Praktisch: Ein Deadlock liegt vor, wenn ein Teilnetz durch eine (ungünstige) Schaltfolge lahmgelegt werden kann.

**Trap** – Eine Stelle, die einmal markiert, unter keiner Folgemarkierung unmarkiert ist.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="deadlock_trap" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Deadlock und Trap – Ressourcen-Beispiel</text></name>
    <page id="p0">

      <place id="s_ressource">
        <name><text>Ressource</text></name>
        <capacity><text>2</text></capacity>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_reserviert_a">
        <name><text>Reserviert A</text></name>
        <capacity><text>2</text></capacity>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_reserviert_b">
        <name><text>Reserviert B</text></name>
        <capacity><text>2</text></capacity>
        <initialMarking><text>1</text></initialMarking>
      </place>

      <transition id="t_nehmen_a"> <name><text>Nehmen A</text></name> </transition>
      <transition id="t_nehmen_b"> <name><text>Nehmen B</text></name> </transition>
      <transition id="t_zurueck_a"><name><text>Zurück A</text></name> </transition>
      <transition id="t_zurueck_b"><name><text>Zurück B</text></name> </transition>

      <arc id="a1" source="s_ressource"   target="t_nehmen_a">
        <inscription><text>2</text></inscription>
      </arc>
      <arc id="a2" source="t_nehmen_a"    target="s_reserviert_a"/>
      <arc id="a3" source="s_ressource"   target="t_nehmen_b">
        <inscription><text>2</text></inscription>
      </arc>
      <arc id="a4" source="t_nehmen_b"    target="s_reserviert_b"/>
      <arc id="a5" source="s_reserviert_a" target="t_zurueck_a">
        <inscription><text>2</text></inscription>
      </arc>
      <arc id="a6" source="t_zurueck_a"   target="s_ressource">
        <inscription><text>2</text></inscription>
      </arc>
      <arc id="a7" source="s_reserviert_b" target="t_zurueck_b">
        <inscription><text>2</text></inscription>
      </arc>
      <arc id="a8" source="t_zurueck_b"   target="s_ressource">
        <inscription><text>2</text></inscription>
      </arc>

    </page>
  </net>
</pnml>
```

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

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="marked_graph_friseur" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Marked Graph – Friseursalon</text></name>
    <page id="p0">

      <place id="s_kunde_ein">
        <name><text>Kunde trifft ein</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_haare_bereit">
        <name><text>Haare bereit</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_maniküre_bereit">
        <name><text>Maniküre bereit</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_haare_fertig">
        <name><text>Haare fertig</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_maniküre_fertig">
        <name><text>Maniküre fertig</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_kunde_fertig">
        <name><text>Kunde fertig</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>

      <transition id="t_fork">   <name><text>Fork</text></name>  </transition>
      <transition id="t_haare">  <name><text>Haare schneiden</text></name> </transition>
      <transition id="t_manikuere"><name><text>Maniküre</text></name> </transition>
      <transition id="t_join">   <name><text>Join</text></name>  </transition>

      <!-- Jede Stelle hat genau 1 eingehende und 1 ausgehende Kante -->
      <arc id="a1" source="s_kunde_ein"      target="t_fork"/>
      <arc id="a2" source="t_fork"           target="s_haare_bereit"/>
      <arc id="a3" source="t_fork"           target="s_maniküre_bereit"/>
      <arc id="a4" source="s_haare_bereit"   target="t_haare"/>
      <arc id="a5" source="t_haare"          target="s_haare_fertig"/>
      <arc id="a6" source="s_maniküre_bereit" target="t_manikuere"/>
      <arc id="a7" source="t_manikuere"      target="s_maniküre_fertig"/>
      <arc id="a8" source="s_haare_fertig"   target="t_join"/>
      <arc id="a9" source="s_maniküre_fertig" target="t_join"/>
      <arc id="a10" source="t_join"          target="s_kunde_fertig"/>

    </page>
  </net>
</pnml>
```

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

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pnml xmlns="http://www.pnml.org/version-2009/grammar/pnml">
  <net id="muenzautomat" type="http://www.pnml.org/version-2009/grammar/ptnet">
    <name><text>Münzautomat (Basismodell)</text></name>
    <page id="p0">

      <!-- Stellen -->
      <place id="s_bereit">
        <name><text>Bereit</text></name>
        <initialMarking><text>1</text></initialMarking>
      </place>
      <place id="s_muenze_drin">
        <name><text>Münze im Automaten</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_artikel_gewaehlt">
        <name><text>Artikel gewählt</text></name>
        <initialMarking><text>0</text></initialMarking>
      </place>
      <place id="s_artikel_vorrat">
        <name><text>Artikelvorrat</text></name>
        <capacity><text>5</text></capacity>
        <initialMarking><text>5</text></initialMarking>
      </place>

      <!-- Transitionen -->
      <transition id="t_einwerfen">
        <name><text>Münze einwerfen</text></name>
      </transition>
      <transition id="t_abbrechen">
        <name><text>Abbrechen (Münze zurück)</text></name>
      </transition>
      <transition id="t_auswaehlen">
        <name><text>Artikel auswählen</text></name>
      </transition>
      <transition id="t_ausgeben">
        <name><text>Artikel ausgeben</text></name>
      </transition>
      <transition id="t_auffuellen">
        <name><text>Auffüllen</text></name>
      </transition>

      <!-- Kanten -->
      <arc id="a1" source="s_bereit"           target="t_einwerfen"/>
      <arc id="a2" source="t_einwerfen"         target="s_muenze_drin"/>
      <arc id="a3" source="s_muenze_drin"       target="t_abbrechen"/>
      <arc id="a4" source="t_abbrechen"         target="s_bereit"/>
      <arc id="a5" source="s_muenze_drin"       target="t_auswaehlen"/>
      <arc id="a6" source="t_auswaehlen"        target="s_artikel_gewaehlt"/>
      <arc id="a7" source="s_artikel_gewaehlt"  target="t_ausgeben"/>
      <arc id="a8" source="s_artikel_vorrat"    target="t_ausgeben"/>
      <arc id="a9" source="t_ausgeben"          target="s_bereit"/>
      <!-- Auffüllen wenn Vorrat leer -->
      <arc id="a10" source="t_auffuellen" target="s_artikel_vorrat">
        <inscription><text>5</text></inscription>
      </arc>

    </page>
  </net>
</pnml>
```

## Zusammenfassung

- Petri-Netze geeignet zur Modellierung logischer und nebenläufiger Prozesse
- Bestehen aus Stellen (Zustände, Bedingungen) und Transitionen (Ereignisse, Veränderungen)
- Markierte Stellen geben an, welche Zustände/Bedingungen gelten
- Stellen/Transitionen-Netze erweitern Bedingungs/Ereignis-Netze um Kantengewichte und Kapazitäten
- Verhaltenseigenschaften wie Lebendigkeit oder Beschränktheit können durch den Erreichbarkeitsgraph oder durch strukturelle Analyse bestimmt werden
