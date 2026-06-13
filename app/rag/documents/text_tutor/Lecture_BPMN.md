# Business Process Model and Notation 2.0

## Was ist ein Prozess?

„Satz von in Wechselbeziehungen stehenden Mitteln und Tätigkeiten, die Eingaben in Ergebnisse umgestalten" (DIN EN ISO 8402:1995)

„Ein Prozess ist die inhaltlich abgeschlossene, zeitliche und sachlogische Folge von Aktivitäten, die zur Bearbeitung eines betriebswirtschaftlich relevanten Objekts notwendig sind" (Enzyklopädie der Wirtschaftsinformatik)

## Was ist ein Geschäftsprozess?

Definition Geschäftsprozess: Zusammenfassung von Tätigkeiten, die zusammengenommen einen Wert für den Prozesskunden schaffen.
- Zusammenwirken von inner- und außerbetrieblichen Organisationseinheiten
- Prozesse laufen quer durch betriebliche Funktionsbereiche und sind nicht aus deren Aufgaben ableitbar

Prozessfragmentierung in arbeitsteiligen Organisationen:
- Häufig keine klar definierte Verantwortung für Gesamtprozess
- Hohe Fehleranfälligkeit durch viele Beteiligte
- Viele Übergaben führen zu Warteschlangen

## Arten von Geschäftsprozessen

Unterteilung in betriebliche und überbetriebliche Geschäftsprozesse:
- **Betriebliche Geschäftsprozesse:** vollständig innerhalb eines Unternehmens
- **Überbetriebliche Geschäftsprozesse:** unter Beteiligung verschiedener Marktteilnehmer (Kunden, Lieferanten, …)

## Warum Geschäftsprozesse modellieren?

- Existierende Prozesse müssen verstanden und gesteuert werden (Messen relevanter Kenngrößen, z. B. Zeit, Kosten, Ressourcen, …)
- Verbesserung existierender Prozesse
- Entwerfen neuer Prozesse
- Dokumentieren aller Prozesse (Kommunikation an Beteiligte!)
- Prozessautomatisierung

## Was ist BPMN?

BPMN = Business Process Model and Notation – standardisierte grafische Notation zur Beschreibung von Geschäftsprozessen.

Ziele:
- Leichte Verständlichkeit durch einfache Notation
- Leichte Adaptierbarkeit durch Unternehmensanalysten
- Übersichtliche Darstellung komplexer Geschäftsprozesse
- Überführbarkeit zu BPM Execution Languages
- Workflow-Management und Workflow-Management-Systeme

## Geschichte von BPMN

- Entwicklung geht auf die Business Process Management Initiative zurück
- 2004: Version 1.0 unter Leitung von Stephen White (IBM)
- 2005: Übernahme durch OMG
- 2011: BPMN 2.0 offiziell vorgestellt (zahlreiche Verbesserungen und Erweiterungen, z. B. Choreographiediagramm)

## Struktur von BPMN

4 Diagrammarten:
- Prozessdiagramm
- Kollaborationsdiagramm
- Konversationsdiagramm
- Choreographiediagramm

Elemente (Core Elements):
- Flow Objects
- Swimlanes
- Connecting Objects
- Data Objects
- Artifacts

## Elemente: Flow Objects

Flow Objects unterteilen sich in:
- **Activity** – eine durchzuführende Tätigkeit
- **Event** – ein eingetretenes Ereignis
- **Gateway** – eine Verzweigung oder Zusammenführung im Kontrollfluss

## Flow Objects: Activities

Eine Aktivität ist ein generischer Begriff für eine Tätigkeit, die im Rahmen eines Prozesses durchgeführt wird.

| Element | Beschreibung |
|---|---|
| Aufgabe/Task | Repräsentiert eine Arbeitseinheit |
| Transaktion | Gruppe von Aktivitäten, die logisch zusammengehören |
| Aufruf-Aktivität | Repräsentiert einen global definierten Teilprozess oder eine Aufgabe, die wiederverwendet wird |
| Manueller Task | Wird ohne IT-Unterstützung durchgeführt |
| Benutzer-Task | Wird von einem Benutzer mit IT-Unterstützung durchgeführt |
| Service-Task | Wird automatisiert durchgeführt |
| Empfangs-Task | Empfängt Nachrichten; entspricht der Semantik des Zwischenereignisses für eingetretene Nachrichten |
| Sende-Task | Sendet Nachrichten; entspricht der Semantik des Zwischenereignisses für ausgelöste Nachrichten |
| Skript-Task | Führt ein Skript direkt in der Prozess-Engine aus |
| Geschäftsregel-Task | Wertet Geschäftsregeln für ein Ergebnis oder eine Entscheidung aus |
| Teilprozess | Kein eigenständiger Prozess, sondern in den umgebenden Prozess eingebettet |
| Ereignis-Teilprozess | Wird in einem Teilprozess platziert und durch ein Startereignis ausgelöst; kann den Teilprozess abbrechen oder parallel ausgeführt werden |

Markierungen beschreiben den Charakter einer Aufgabe:
- `+` Teilprozess (erweiterbar)
- `|||` Mehrfachausführung (parallel)
- `≡` Mehrfachausführung (sequenziell)
- `↻` Schleife
- `~` Ad-Hoc

## Flow Objects: Events

Ein Event repräsentiert ein Ereignis innerhalb eines Geschäftsprozesses. In BPMN wird es als Kreis dargestellt. Es gibt 3 Arten von Events:
- **Startereignisse** – leiten einen Prozess ein
- **Zwischenereignisse** – treten während des Prozesses auf
- **Endereignisse** – beenden einen Prozess

Start- und Zwischenereignisse können unterbrechend oder nicht-unterbrechend sein.

| Event-Typ | Beschreibung |
|---|---|
| Blanko | Untypisierte Ereignisse; i. d. R. am Start oder Ende eines Prozesses |
| Nachricht | Empfang oder Versand von Nachrichten |
| Timer | Periodische zeitliche Ereignisse, Zeitpunkte oder Zeitspannen |
| Eskalation | Meldung an den nächsthöheren Verantwortlichen |
| Bedingung | Reaktion auf veränderte Bedingungen und Bezug auf Geschäftsregeln |
| Link | Zwei zusammengehörige Link-Ereignisse repräsentieren einen Sequenzfluss |
| Fehler | Auslösen und behandeln von definierten Fehlern |
| Abbruch | Reaktion auf abgebrochene Transaktion oder Auslösen von Abbrüchen |
| Kompensation | Behandeln oder Auslösen einer Kompensation |
| Signal | Signal über mehrere Prozesse; auf ein Signal kann mehrfach reagiert werden |
| Mehrfach | Eintreten eines von mehreren Ereignissen; Auslösen aller Ereignisse |
| Mehrfach/Parallel | Eintreten aller Ereignisse |
| Terminierung | Löst die sofortige Beendigung des Prozesses aus |

## Flow Objects: Gateways

Modellierung von Verzweigungen im Kontrollfluss von Prozessen. Dienen der Verzweigung oder Zusammenführung.

| Gateway-Typ | Beschreibung |
|---|---|
| Exklusives Gateway (XOR) | Abhängig von Verzweigungsbedingungen wird der Fluss zu genau einer Kante weitergeleitet. Bei Zusammenführung wird auf genau eine Kante gewartet. |
| Ereignis-basiertes Gateway | Stets gefolgt von Ereignissen oder Empfänger-Aufgaben. Fluss wird zu dem Ereignis geleitet, das zuerst eintritt. |
| Inklusives Gateway (OR) | Je nach vorliegenden Bedingungen werden eine oder mehrere (eingehende bzw. ausgehende) Kanten synchronisiert. |
| Paralleles Gateway (AND) | Bei Verzweigung werden alle ausgehenden Kanten gleichzeitig aktiviert. Bei Zusammenführung wird auf alle eingehenden Kanten gewartet, bevor die ausgehende Kante aktiviert wird. |
| Komplexes Gateway | Kanten werden durch komplexe Bedingungen aktiviert. Sollte nur verwendet werden, wenn das gewünschte Verhalten nicht mit Hilfe anderer Gateways beschrieben werden kann. |
| Exklusives Ereignis-basiertes Gateway | Sobald eines der nachfolgenden Ereignisse eintritt, wird der Fluss entsprechend weitergeleitet. |
| Paralleles Ereignis-basiertes Gateway | Sobald alle nachfolgenden Ereignisse eingetreten sind, wird der Prozess gestartet. |

## Swimlanes

Swimlanes dienen dazu Rollen, Zuständigkeiten oder auch Organisationsstrukturen abzubilden. Unterschieden werden Pools und Lanes.

- **Pools:** Repräsentieren abstrakte Rollen (z. B. „Kunde" oder „Lieferant") oder konkrete Instanziierungen dieser Rollen. Ein Pool besitzt Lanes.
- **Lanes:** Unterteilen Pools mit dem Zweck, Aktivitäten oder Zuständigkeiten innerhalb eines Pools zu modellieren. Eine Lane befindet sich stets innerhalb eines Pools.
- **Nachrichtenflüsse:** Dienen dazu, den Informationsfluss über organisatorische Grenzen hinweg zu modellieren. Sie fließen dabei zwischen verschiedenen Pools. Verbunden werden können dabei neben den Pools selber auch Aktivitäten oder Events in diesen.

## Verbindende Objekte

6 Arten von Verbindungsobjekten:

| Element | Beschreibung |
|---|---|
| Sequenzfluss | Definiert die Reihenfolge von Aktivitäten |
| Bedingter Sequenzfluss | Enthält eine Bedingung und definiert, wann der Fluss benutzt wird |
| Standard-Sequenzfluss | Wird genutzt, wenn keine Bedingung einer Verzweigung zutrifft |
| Nachrichtenfluss | Repräsentiert den Austausch von Nachrichten (zwischen Pools) |
| Datenassoziation | Dient der Annotierung von Datenobjekten an Ablaufelemente |
| Gerichtete Datenassoziation | Zeigt die Richtung des Datenflusses an |

## Connecting Objects: Beispiel

Dasselbe Beispiel wie bei Swimlanes, nun mit expliziter Darstellung der Verbindungstypen (Nachrichtenfluss zwischen Pools, Sequenzfluss innerhalb der Pools, Datenassoziation für Datenobjekte).

## Data Objects

2 Arten, Daten zu repräsentieren: Data Stores und Data Objects.

| Element | Beschreibung |
|---|---|
| Datenobjekt | Repräsentiert Informationen, die in einem Prozess verwendet werden (z. B. E-Mails, Dokumente, Datensätze) |
| Listen-Datenobjekt | Repräsentiert eine Gruppe von Informationen, z. B. eine Liste mit Bestellpositionen |
| Dateninput | Repräsentiert einen externen Input, der von einer Aktivität gelesen wird und nach außen sichtbare Eingabeschnittstelle des Prozesses |
| Datenoutput | Repräsentiert einen Output, der durch einen Prozess erzeugt wird und nach außen sichtbare Ausgabeschnittstelle des Prozesses |
| Datenspeicher | Repräsentiert einen Speicher, auf den prozessübergreifend sowohl lesend als auch schreibend zugegriffen werden kann |

## Artifacts

BPMN unterscheidet 2 Arten von Artefakten: Gruppen und Annotationen.

- **Gruppe:** Gruppiert Elemente innerhalb einer Kategorie. Das Nutzen beeinflusst nicht den Kontrollfluss, sondern dient vielmehr der Dokumentation des Modells.
- **Text-Annotation:** Dient dazu, dem Leser des Modells zusätzliche Informationen bereitzustellen.

## Übungsaufgabe: Bewertung einer Bachelorarbeit

Prozessbeschreibung:
- Der Professor erhält die Nachricht, dass die BA angemeldet ist, trägt sich die Abgabefrist in den Kalender ein und wartet.
- Anschließend erhält er entweder die Bachelorarbeit oder die Frist läuft ab.
  - Nach Fristablauf erkundigt er sich beim Prüfungsamt und bekommt mitgeteilt, dass keine Verlängerung gewährt wurde (Prozess endet) oder eine Verlängerung gewährt wurde (neue Frist eintragen, erneut warten).
- Nach Erhalt der Bachelorarbeit liest er diese. Entdeckt er ein Plagiat, hört er auf zu lesen, meldet das Plagiat dem Prüfungsamt, und der Prozess endet.
- Gab es kein Plagiat, schreibt er das Gutachten. Wird er dabei traurig, schaltet er Musik an und hört diese, bis entweder 10 Minuten vergangen sind oder er nicht mehr traurig ist; dann schaltet er sie aus.
- Nach Fertigstellung des Gutachtens teilt er dem Studenten den Verteidigungstermin mit und erhält eine Terminbestätigung. Er kündigt den Termin allgemein an.
- Wenn der Verteidigungstermin erreicht ist, hört er den Vortrag des Studenten und verkündet die Note.