## Warum Modellierung?

- Erklärung komplexer oder komplizierter Phänomene
  - Modell als abstrahierende Rekonstruktion der Realität
  - Beispiel: Warum erzeugt eine Ampelsteuerung Staus an einer Kreuzung?
- Gestaltung
  - Aufzeigen von Optionen zur (Um-)Gestaltung der Realwelt
  - Modell hat konstruktiven Charakter
  - Beispiel: Arbeitsteilige Entwicklung eines Web-Shops

## Hinweis

Was erwarten wir bei Software-Projekten als Dokumentation?
- Anwendungsfälle (z.B. Use Case Diagramm)
- Ablaufbeschreibung (z.B. Aktivitätsdiagramm)
- Konzeptuelles Datenmodell (z.B. Klassendiagramm)
- Architekturbeschreibung (z.B. Komponentendiagramm)
- Schnittstellendokumentation

## Modelle und Modellierung

Definitionen:
- Ein Modell ist ein abstraktes, immaterielles Abbild realer Strukturen bzw. des realen Verhaltens für Zwecke des Subjekts.
- Ein Modell ist adäquates, vereinfachendes, idealisierendes Abbild der Realität.

Modellierung ist der kreative Prozess des Modellentwurfs.

## Begriffswelt

- Modellbildung: Informationen über ein Original erschaffen
- Information: „Aussagen, die den Erkenntnis- bzw. Wissensstand eines Subjektes über ein Objekt in einer gegebenen Situation und Umwelt zur Erfüllung einer Aufgabe verbessern." [Szyperski 1980]
- Kurz: Handlungsrelevantes Wissen

## Modelldarstellung

- Ist Denken ohne Sprache möglich?
- Was ist eine Sprache?
- Modellierungssprachen:
  - Mathematik
  - Programmiersprachen
  - (Semi-formale) grafische Sprachen (auch: Modellierungsmethoden)

## Modellierung mit Entity-Relationship-Diagrammen

Zugrundeliegende Annahme: Die Realwelt besteht aus Objekten (Entities/Entitäten) und Beziehungen (Relationships) zwischen diesen.

## Grundelemente der Modellierungssprache

| Bezeichnung | Definition |
|---|---|
| Entitytyp | Generalisierende Bezeichnung für eine Vielzahl von Betrachtungsobjekten, die gemeinsame Eigenschaften aufweisen |
| Relationshiptyp | Sinnvolle Verbindung oder Beziehung zwischen zwei oder mehreren Entity-Typen |
| Attribut | Relevante Eigenschaft eines Betrachtungsobjekts |
| Schlüsselattribut | Eigenschaft, die für jede Ausprägung des Entity-Typs einzigartig ist, d.h. eine Entity eindeutig identifiziert |
| Generalisierung, Spezialisierung | Ähnliche Entity-Typen werden zu einem übergreifenden Entity-Typ (Supertyp) zusammengefasst |
| Uminterpretierter Beziehungstyp | Die Uminterpretation von Beziehungstypen wird erforderlich, um Beziehungen zwischen Beziehungstypen darstellen zu können |
| Kante | Zeigt die Verbindung zwischen den Typen auf |
| Kardinalität in (min,max)-Notation | Zeigt die minimale und maximale Beziehungsausprägung am Beziehungstyp |

Beispiel: Lieferant –(0,n)– Lieferliste –(0,m)– Artikel, mit Attributen LNr und ANr, Preis am Relationshiptyp.

## Erklärung: Schlüssel

- Schlüssel dienen zur eindeutigen Identifizierung einer Entität
- Beispiel: die ISBN eines Buches, die Personalausweisnummer einer Person
- Beispiel: Entity-Typ Person mit Attributen Vorname, Nachname und Schlüsselattribut Pers.-ID; Entity-Typ Buch mit Attributen Titel und Schlüsselattribut ISBN

## Komplexere Sachverhalte

- Eine Beziehung kann n Entitäten miteinander verknüpfen
- Beispiel: Ein Projekt wird von mehreren Mitarbeitern bearbeitet und durch mehrere Kostenstellen finanziert
- Beteiligt: Entity-Typen Kostenstelle, Person, Projekt mit einem ternären Relationshiptyp
- Abbildung von hierarchischen Strukturen, z.B. Organisationseinheiten
- Beispiel: Ein Unternehmen ist in mehreren Abteilungen strukturiert, die wiederum beliebig viele Unterabteilungen besitzen können.
- Rekursiver Relationshiptyp: Abteilung –[1,1]– besteht aus –[0,n]– Abteilung

## Unterschied zwischen „Entity" und „Entity-Typ"

- Entity-Typ: abstrakte Klasse, z.B. Lieferant mit Attributen LNr, LName, Standort, Servicegrad
- Entities: konkrete Ausprägungen, z.B.:
  - 0295, Müller KG, München, 85%
  - 3840, Meier AG, Köln, 92%
  - 1201, Handel OHG, Dresden, 89%

## „How to Find the Object"

Konzeptuelle Modellierung – Aussagen:
- „Studenten besuchen eine Vorlesung"
- „Vorlesungen werden von Dozenten gehalten"
- „Vorlesungen finden in einem Raum statt"
- „Ein Raum enthält Stühle, Tische und ein Whiteboard"

Fragen: Was sind hier die Entitätstypen, Beziehungstypen und Attribute?

Hinweis zu „konzeptuell": Von späteren Implementierungsentscheidungen abstrahierend. Ein konzeptuelles Modell kann zu verschiedenen Implementierungen führen.

## Implementierungsalternativen: Daten- und Datenbankmodelle

- Konzeptuelles/semantisches Datenmodell: Beschreibung der fachlichen Anforderungen des in der Datenbank abzubildenden Realitätsausschnitts
- Datenbankmodell: Konkrete, Datenbankmanagementsystem-bezogene Umsetzung des Datenmodells

Schichten: Betriebliche Realwelt → Konzeptionelles Schema → Datenmodell → Datenbankmodell → Externe Schemata (über Transformationsregeln und Abstraktion)

## ER-Diagramme und relationale Datenbanken

- Modellierung ist kein Selbstzweck
- ER-Diagramme beschreiben die konzeptuelle Sicht auf Daten
- Konzeptuelle Sicht muss auf technische Implementierung (Datenbanktabellen) übertragen werden

## 1:n Beziehungen

Beziehung: Person –1– gehört zu –n– Org.-Einheit

Tabelle Person: PkPersId, Vorname, Nachname, FkOrgId
- 001, Claus, Rautenstrauch, 12345
- 002, Jubran, Rajub, 12345
- 007, James, Blond, 42235

Tabelle OrgEinheit: PkOrgId, Name, Standort
- 12345, AG WI, Magdeburg
- 42235, MI 5, London

## n:m Beziehungen

Beziehung: Person –[0,m]– bearbeitet –[0,n]– Projekt

- Eine Person bearbeitet mehrere Projekte.
- Mehrere Personen bearbeiten ein Projekt.
- Es gibt Personen, die kein Projekt bearbeiten.
- Es gibt Projekte, die von niemandem bearbeitet werden.

Tabelle Person: PkPersId, Vorname, Nachname
Tabelle Projekt: PkProjektId, Name
Tabelle Projektmitarbeiter (Zwischentabelle): FkPersId, FkProjektId

## Implementierungsalternativen: XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Lieferanten>
  <Lieferant>
    <LNr>1234</LNr>
    <LName>Müller KG</LName>
    <Standort>Magdeburg</Standort>
    <Servicegrad>90%</Servicegrad>
  </Lieferant>
  <Lieferant>
    <LNr>5678</LNr>
    <LName>SASD GmbH</LName>
    <Standort>Berlin</Standort>
    <Servicegrad>80%</Servicegrad>
  </Lieferant>
  <Lieferant>
    <LNr>1212</LNr>
    <LName>Tele 50000 AG</LName>
    <Standort>Stendal</Standort>
    <Servicegrad>34%</Servicegrad>
  </Lieferant>
</Lieferanten>
```

## Vom ER-Diagramm zum Datenbankmodell

- Aus dem Fachkonzept wird das DV-Konzept abgeleitet:
  - Fachkonzept: Semantische Datenmodelle (ER-Diagramm)
  - DV-Konzept: Relationales Modell, Hierarchisches Modell, Dokumentenmodell …
- Das Datenmodell wird in ein spezielles Datenbankmodell überführt:
  - Überführung als Tabelle → relationales Datenbankmanagementsystem
  - Überführung als Dokument → XML

Beispiel: Lieferant liefert Artikel → relationale Darstellung als Tabellen Lieferant, liefert, Artikel.

## Auszeichnungssprachen

Idee von Auszeichnungssprachen:
- Auszeichnung von Daten durch zusätzlichen Text (Markup) in einem Dokument
- Meta-Informationen werden ebenfalls übertragen und ausgewertet

Markup enthält Informationen über das Dokument:
- Dokumentstruktur
- Dokumentinhalt
- Dokumentverarbeitung

Beispiele:
- Struktur: `<titel>Neuer Vorstand bei der Trinktechnik AG</titel>`
- Inhalt: Neuer Vorstand bei der `<firma>Trinktechnik AG</firma>`
- Verarbeitung: `<fett>Neuer Vorstand bei der Trinktechnik AG</fett>`

## Extensible Markup Language (XML)

- XML ist eine Meta-Auszeichnungssprache, mit der verschiedenste Markup-Sprachen definiert werden können
- Es existieren Regeln zur Bildung von XML-Dokumenten:
  - XML-Syntaxregeln führen zu wohlgeformten Dokumenten
  - XML-Grammatiken führen zu validen Dokumenten
- XML ist für den Einsatz im WWW angepasst: plattformunabhängig, maschinenlesbar
- XML ermöglicht Beschreibung, Austausch, Darstellung und Manipulation von strukturierten Daten

## XML – Technologien

Zusammenspiel verschiedener Technologien ermöglicht Trennung von Inhalt, Struktur und Formatierung:
- Inhalt: XML-Tags
- Struktur: Document Type Definitions (DTD), XML Stylesheets (XSD)
- Formatierung: Extensible Style Sheet Language (XSL), Cascading Style Sheets (CSS)

## XML – Inhalt

XML-Tags:
- Können beliebig, individuellen Zielen entsprechend, benannt werden

XML-Syntaxregeln:
- XML-Deklaration am Anfang
- XML-Dokument muss ein Wurzelelement beinhalten, das alle anderen Elemente umfasst
- Elemente müssen korrekt geschachtelt sein
- Tags müssen immer geschlossen werden
- Attributwerte immer in Anführungszeichen
- Groß-/Kleinschreibung wird unterschieden

Entspricht ein XML-Dokument den Regeln, wird es als wohlgeformt bezeichnet.

```xml
<?xml version="1.0"?>
<Produkt>
  <Name>Kaltgetränkeautomat</Name>
  <Preis Waehrung="EUR">698,00</Preis>
  <Preis Waehrung="DM">1366,00</Preis>
</Produkt>
```

## XML – Beispieldokument

```xml
<?xml version="1.0"?>
<Kunde>
  <Kund-Nr>3416484</Kund-Nr>
  <Name>Bayer</Name>
  <Adresse>
    <Str>Waldweg</Str>
    <Nr>12</Nr>
    <PLZ>39106</PLZ>
    <Ort>Magdeburg</Ort>
  </Adresse>
  <Status>3</Status>
</Kunde>
```

## XML – Hierarchischer Aufbau

```xml
<?xml version="1.0"?>
<Rechnung>
  <Auftraggeber>
    <KundenNr>25562-556E</KundenNr>
    <Name>Universität Augsburg</Name>
    <Adresse>Universitätsstrasse 16, 86135 Augsburg</Adresse>
    <Datum>01.01.2002</Datum>
  </Auftraggeber>
  <Rechnungspositionen>
    <Rechnungsposition>
      <Artikel>Heissgetränkeautomat G45</Artikel>
      <Anzahl>10</Anzahl>
      <Preis Waehrung="EUR">1000</Preis>
    </Rechnungsposition>
  </Rechnungspositionen>
</Rechnung>
```

Hierarchischer Aufbau als Baum: Rechnung → Auftraggeber (KundenNr, Name, Adresse, Datum), Rechnungspositionen → Rechnungsposition (Artikel, Anzahl, Preis)

## XML – Struktur

Individuelle Auszeichnungssprache:
- Angabe einer formalen Grammatik, um nur syntaktisch korrekte Dokumente zuzulassen
- Zwei Arten der Definition in der Praxis: Document Type Definition (DTD), XML-Schema Description Language (XSD)
- Prüfung der Konformität eines Dokuments durch XML-Parser: Ist das Dokument wohlgeformt? Entspricht es den Regeln der Grammatik (ist es gültig/valide)?

Allgemeine Definition einer Grammatik mit der erweiterten Backus-Naur-Form (EBNF):

| Notation | Bedeutung |
|---|---|
| A B | A gefolgt von B |
| A \| B | A oder B |
| [ A ] | nichts oder A |
| { A } bzw. A* | nichts, A oder beliebige Wiederholung von A |
| A+ | A oder beliebige Wiederholung von A |
| ( A \| B ) C | AC oder BC |

Grammatik-Beispiel:
```
Rechnung := Auftraggeber Rechnungspositionen
Auftraggeber := KundenNr Name Adresse Datum
Rechnungspositionen := Position+ Gesamtpreis
Position := Artikel Anzahl Preis
```

## XML – Document Type Definition (DTD)

Struktur: `<!ELEMENT name model>`
- Name: Name des Elements
- Model: Erlaubter Inhalt für das Element

Syntax des Inhaltsmodells:

| Notation | Bedeutung |
|---|---|
| a | a muss genau einmal auftreten |
| a? | a kann einmal oder keinmal auftreten |
| a+ | a muss einmal und kann mehrmals auftreten |
| a* | a kann keinmal, einmal oder mehrmals auftreten |
| a, b | b folgt auf a |
| a \| b | entweder a oder b |
| (a, b) \| (b, a) | a folgt auf b oder umgekehrt |
| #PCDATA | Zeichenkette |

```xml
<!ELEMENT Rechnung (Auftraggeber,Rechnungspositionen)>
<!ELEMENT Auftraggeber (KundenNr,Name,Adresse,Datum)>
<!ELEMENT Rechnungspositionen (Position+,Gesamtpreis)>
<!ELEMENT Position (Artikel,Anzahl,Preis)>
<!ELEMENT KundenNr (#PCDATA)>
<!ELEMENT Preis (#PCDATA)>
<!ATTLIST Preis Waehrung CDATA>
```

## DTD – Beispiel

```xml
<!ELEMENT Rechnung (Auftraggeber,Rechnungspositionen)>
<!ELEMENT Auftraggeber (KundenNr,Name,Adresse,Datum)>
<!ELEMENT Rechnungspositionen (Position+,Gesamtpreis)>
<!ELEMENT Position (Artikel,Anzahl,Preis)>
<!ELEMENT KundenNr (#PCDATA)>
<!ELEMENT Preis (#PCDATA)>
<!ATTLIST Preis Waehrung CDATA>
<!ELEMENT Gesamtpreis (#PCDATA)>
<!ATTLIST Gesamtpreis Waehrung CDATA>
```

```xml
<?xml version="1.0"?>
<Rechnung>
  <Auftraggeber>
    <KundenNr>25562-556E</KundenNr>
    <Name>Universität Augsburg</Name>
    <Adresse>Universitätsstrasse 16, 86135 Augsburg</Adresse>
    <Datum>01.01.2002</Datum>
  </Auftraggeber>
  <Rechnungspositionen>
    <Position>
      <Artikel>Heissgetränkeautomat G45</Artikel>
      <Anzahl>10</Anzahl>
      <Preis Waehrung="EUR">1000</Preis>
    </Position>
    <Gesamtpreis Waehrung="EUR">10000</Gesamtpreis>
  </Rechnungspositionen>
</Rechnung>
```

## XML – Schema Description Language (XSD)

Struktur:
- Ist ein XML-Dokument
- Schema ist immer Wurzelelement
- Verwendung von Namensräumen (für das Schema selbst, für das Dokument)

Vorteile:
- Schemata sind in XML geschrieben und können mit den selben Werkzeugen wie XML-Dokumente eingelesen werden
- Erweiterte Typdefinitionen für Elemente möglich (beliebige Strukturen)
- Angabe von Wertebereichen möglich

Nachteile:
- Sehr umfangreich und komplex

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="Artikel" type="Artikeltyp"/>
  ...
```

## XML-Schema – Aufbau

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="Artikel" type="Artikeltyp"/>
  <xs:complexType name="Artikeltyp">
    <xs:sequence>
      <xs:element name="Bezeichnung" type="xs:string"/>
      <xs:element name="Preis" type="xs:decimal"/>
    </xs:sequence>
    <xs:attribute name="id" type="xs:integer" use="required"/>
  </xs:complexType>
</xs:schema>
```

Einfache Datentypen:
- `<xs:element name="Bezeichnung" type="xs:string"/>`
- Weitere Datentypen: xs:decimal, xs:integer, xs:boolean, xs:date, xs:time
- `<xs:attribute name="id" type="xs:integer" use="required"/>`
  - default=".." legt einen Standardwert fest
  - fixed=".." überschreibt den Wert in der Datei

Komplexe Datentypen:
- `<xs:sequence>…</xs:sequence>` – mehrere Elemente in einer festen Reihenfolge

## XML – Formatierung

Extensible Style Sheet Language (XSL):
- Formatvorlagen für XML-Dokumente
- Speicherung der Darstellungsinformationen
- Verschiedene Präsentationsformen durch Austausch der Formatvorlage

Formatierungsmöglichkeiten:
- Hinzufügen von statischem Text (z.B. HTML-Tags)
- Umordnen, Duplizieren, Sortieren und bedingte Ausgabe von Inhalten
- Berechnung neuer Inhalte aus alten

XSL verwendet XPath (XML Path Language):
- Adressierung und Selektion von Inhaltsteilen durch Angabe des Pfades im XML-Baum
- Auch als Abfragesprache verwendbar
- XSL Transformation (XSLT) konvertiert XML-Dokument gemäß der XSL-Formatvorlage

## XML – Transformation

Prozess:
1. Darstellung des XML-Dokuments als hierarchischer Baum und Auswahl der gewünschten Elemente mittels XPath (z.B. /Position/Anzahl)
2. Transformation in HTML gemäß XSLT-Formatvorlage

## XSL – Transformation (XSLT)

XML-Datei:
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/xsl" href="Rechnungen.xsl"?>
<Rechnung>
  <Rechnungskopf>
    <Name>Maier</Name>
    <Vorname>Wilhelm</Vorname>
  </Rechnungskopf>
  <Rechnungspositionen>
    <Position id="1">
      <Artikel>Gummibären</Artikel>
      <Anzahl>200</Anzahl>
      <Preis>1,50</Preis>
      <Zeilensumme>300,00</Zeilensumme>
    </Position>
    <Position id="2">
      <Artikel>Kaugummi</Artikel>
      <Anzahl>15</Anzahl>
      <Preis>0,90</Preis>
      <Zeilensumme>13,50</Zeilensumme>
    </Position>
    <Gesamtsumme>313,50</Gesamtsumme>
  </Rechnungspositionen>
</Rechnung>
```

XSL-Datei:
```xml
<?xml version="1.0"?>
<xsl:transform version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>Lieferschein</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th align="left">Anzahl</th>
            <th align="left">Artikel</th>
          </tr>
          <xsl:for-each select="/Rechnung/Rechnungspositionen/Position">
            <tr>
              <td><xsl:value-of select="Anzahl"/></td>
              <td><xsl:value-of select="Artikel"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:transform>
```

## XPath – Syntax

Auffinden von Elementen:
- `/Rechnung/Rechnungspositionen/Position` – wählt alle Elemente auf die dieser Pfad passt
- `//Datum` – wählt alle "Datum"-Elemente

Auswählen unbekannter Elemente:
- `/*/*/Name` – wählt alle "Name"-Elemente die zwei Vorfahren haben
- `/Rechnung/Rechnungspositionen/*` – selektiert alle Elemente unterhalb der Rechnungspositionen

Auswahl bestimmter Elemente:
- `/Rechnung/Rechnungspositionen/Position[Artikel='Kaugummi']` – wählt alle Positionen die den Artikel „Kaugummi" beinhalten
- `//Rechnungskopf[Name]` – selektiert alle Rechnungsköpfe, die ein Element Name enthalten

Auffinden von Attributen:
- `//*[@id]` – sucht alle Elemente, die ein Attribut "id" haben
- `//Position[@*]` – wählt alle "Position"-Elemente, die irgendein Attribut haben


## Kardinalitäten: Beziehungen zwischen Mengen

| Beziehungstyp | Beispiel | Kardinalitäten |
|---|---|---|
| 1:1 | Mann verheiratet Frau | (1,1) – (1,1) |
| 1:N | Abteilung hat Arbeitsplatz | (1,1) – (1,n) |
| N:1 | Vorlesung wird gehalten von Professor | (1,1) – (0,n) |
| M:N | Student besucht Vorlesung | (0,n) – (0,m) |

## Generalisierung und Spezialisierung

Entity-Typen werden zu einem übergreifenden Entity-Typ (Supertyp) zusammengefasst bzw. ein Entity-Typ wird in einzelne Typen zerlegt.

- Generalisierung: Betrachtung vom Speziellen (Subtyp) zum Allgemeinen (Supertyp)
- Spezialisierung: Betrachtung vom Allgemeinen (Supertyp) zum Speziellen (Subtyp)

Attribute:
- Eigenschaften (Attribute) der Supertypen werden auf Subtypen vererbt
- Gemeinsame Attribute werden dem Supertyp zugewiesen
- Untergeordnete Entity-Typen (Subtypen) besitzen nur noch speziell sie ausweisende Eigenschaften

Beispiel: Supertyp Geschäftspartner mit Subtypen Kunde und Lieferant.

## Beispiel: „Puzzle"

Entity-Typen: Student, Puzzle, Teil, Tierpuzzle, Gebäudepuzzle, Einzelgebäude, Gebäudegruppe

Beziehungen:
- Student –(0,m)– löst –(0,x)– Puzzle
- Puzzle –(1,1)– besteht aus –(2,n)– Teil
- Puzzle ist-a Tierpuzzle oder Gebäudepuzzle (Generalisierung/Spezialisierung)
- Gebäudepuzzle ist-a Einzelgebäude oder Gebäudegruppe

Attribute: Puzzle: Anzahl Teile; Tierpuzzle: Lebensraum; Gebäudepuzzle: Baukosten; Einzelgebäude: Höhe; Gebäudegruppe: Anzahl der Geb.

## Beispiel: „Mitarbeiter"

1. Ein Mitarbeiter mit Nachname, Vorname, Adresse und Gehalt wird identifiziert durch seine Mitarbeiternummer.
2. Ein Produkt (mit Produktnummer und Name) wird von vielen, aber mindestens einem Mitarbeiter produziert und ein Mitarbeiter produziert viele Produkte.
3. In einem Projekt, identifiziert durch die Projektnummer und gekennzeichnet mit einer Beschreibung, arbeiten viele Mitarbeiter in unterschiedlichen Rollen mit einer eindeutigen RollenNr und einer Beschreibung und ein Mitarbeiter arbeitet in vielen Projekten.
4. Ein Mitarbeiter arbeitet genau in einer Abteilung und in einer Abteilung arbeiten mehrere Mitarbeiter.
5. Eine Abteilung wird gekennzeichnet durch eine Abteilungsnummer (eindeutig) und durch einen Abteilungsnamen.
6. Eine Abteilung gehört genau zu einem (numerisch gekennzeichneten) Unternehmen; ein Unternehmen besteht aus mehreren Abteilungen.

## Lösung „Mitarbeiter"

Entity-Typen: Mitarbeiter, Produkt, Projekt, Abteilung, Unternehmen

Beziehungen und Kardinalitäten:
- Produkt –(0,m)– wird produziert von –(1,n)– Mitarbeiter
- Mitarbeiter –(0,b)– wird bearbeitet von Mitarbeiter in Rolle –(0,a)– Projekt (ternärer Beziehungstyp mit Attributen RollenNr, Beschreibung)
- Mitarbeiter –(2,x)– arbeitet in –(1,1)– Abteilung
- Abteilung –(2,y)– gehört zu –(1,1)– Unternehmen

Attribute:
- Mitarbeiter: Mitarbeiternummer (Schlüssel), Vorname, Nachname, Adresse, Gehalt
- Produkt: Produktnummer (Schlüssel), Name
- Projekt: Projektnummer (Schlüssel), Beschreibung
- Abteilung: Abteilungsnummer (Schlüssel), Abteilungsname
- Unternehmen: Unternehmensnr (Schlüssel)

## Tools: z.B. draw.io

draw.io ist ein kostenloses Werkzeug zur grafischen Modellierung, das u.a. Entity-Relationship-Diagramme und UML-Diagramme unterstützt.

## Modelle

- Modellbildung ist Informationsarbeit.
- Modelle können kommuniziert werden – sie dienen dem Informationsaustausch zwischen Menschen und/oder Maschinen.
- Drei Bedeutungen der Modell-Original-Abbildungen im Zeitverlauf:
  - Rekonstruieren
  - Konstruieren
  - Entwerfen

## Rekonstruieren

- Etymologisch: „wiederherstellen", „nachbilden" eines ursprünglichen Zustands
- Modellierung: Erstellung eines Modells, welches einen Originalzustand der Vergangenheit beschreibt
- Beispiele: SW-Reengineering Modelle, Risikomodelle (Aktien), Referenzmodelle, Periodensystem, Aminosäure Codons, Fachsprachen

## Konstruieren

- Etymologisch: „errichten", „erbauen" oder „zusammenschichten"
- Modellierung: Aus Modell wird das Original erstellt; Original kann ebenfalls Modell sein
- Beispiele: Konstruktionszeichnungen, Source Code, CAD/CAM Modelle

## Entwerfen

- Etymologisch: „ein Bild gestalten", „literarisches und geistiges Gestalten", vorausgedachtes Vorläufiges
- Modellierung: Zustand eines zukünftigen Originals; Annahme: Transformation des gegenwärtigen Originals möglich (Konstruktionshypothese)
- Beispiele: Gebäudearchitekturen, Systemarchitekturen
