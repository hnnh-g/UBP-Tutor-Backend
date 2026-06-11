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

## Diagrammarten: Prozessdiagramm

Stellt einen Fluss zwischen Aufgaben, Ereignissen und Entscheidungen dar, um Prozesse (in einem Unternehmen) abbilden zu können.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             targetNamespace="http://example.org/prozessdiagramm">
  <process id="prozess_vorlesung" name="Vorlesung" isExecutable="false">

    <startEvent id="start" name="Vorlesung beginnt"/>

    <sequenceFlow id="sf1" sourceRef="start" targetRef="task_laptop_ein"/>

    <task id="task_laptop_ein" name="Laptop einschalten"/>

    <sequenceFlow id="sf2" sourceRef="task_laptop_ein" targetRef="task_facebook"/>

    <serviceTask id="task_facebook" name="Mit Facebook interagieren"/>

    <sequenceFlow id="sf3" sourceRef="task_facebook" targetRef="task_laptop_aus"/>

    <task id="task_laptop_aus" name="Laptop ausschalten"/>

    <sequenceFlow id="sf4" sourceRef="task_laptop_aus" targetRef="end"/>

    <endEvent id="end" name="Vorlesung endet"/>

  </process>
</definitions>
```

## Diagrammarten: Kollaborationsdiagramm

Stellt Nachrichtenflüsse oder Kommunikation zwischen Prozessen oder Entitäten (z. B. Kunden oder Partner) dar.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/kollaboration">
  <collaboration id="collab_bachelorarbeit">

    <participant id="pool_student" name="Student" processRef="proc_student"/>
    <participant id="pool_mitarbeiter" name="Mitarbeiter" processRef="proc_mitarbeiter"/>

    <messageFlow id="mf1" name="Anfrage" sourceRef="task_thema_versenden" targetRef="task_thema_erhalten"/>
    <messageFlow id="mf2" name="Konkretisiere das bitte in Hinblick auf Y" sourceRef="task_aenderung_machen" targetRef="task_aenderung_erhalten"/>
    <messageFlow id="mf3" name="Ich habe die Vorschläge im Exposé eingearbeitet" sourceRef="task_expose_schicken" targetRef="task_expose_erhalten"/>

  </collaboration>

  <process id="proc_student" name="Student">
    <startEvent id="start_s"/>
    <sequenceFlow id="sf_s1" sourceRef="start_s" targetRef="task_thema_versenden"/>
    <task id="task_thema_versenden" name="Thema für Abschlussarbeit versenden"/>
    <sequenceFlow id="sf_s2" sourceRef="task_thema_versenden" targetRef="task_aenderung_erhalten"/>
    <task id="task_aenderung_erhalten" name="Änderungsvorschläge erhalten"/>
    <sequenceFlow id="sf_s3" sourceRef="task_aenderung_erhalten" targetRef="task_expose_schicken"/>
    <task id="task_expose_schicken" name="Exposé schicken"/>
    <sequenceFlow id="sf_s4" sourceRef="task_expose_schicken" targetRef="end_s"/>
    <endEvent id="end_s"/>
  </process>

  <process id="proc_mitarbeiter" name="Mitarbeiter">
    <startEvent id="start_m"/>
    <sequenceFlow id="sf_m1" sourceRef="start_m" targetRef="task_thema_erhalten"/>
    <task id="task_thema_erhalten" name="Thema für Abschlussarbeit erhalten"/>
    <sequenceFlow id="sf_m2" sourceRef="task_thema_erhalten" targetRef="task_aenderung_machen"/>
    <task id="task_aenderung_machen" name="Änderungsvorschläge machen"/>
    <sequenceFlow id="sf_m3" sourceRef="task_aenderung_machen" targetRef="task_expose_erhalten"/>
    <task id="task_expose_erhalten" name="Exposé erhalten"/>
    <sequenceFlow id="sf_m4" sourceRef="task_expose_erhalten" targetRef="end_m"/>
    <endEvent id="end_m"/>
  </process>
</definitions>
```

## Diagrammarten: Konversationsdiagramm

Stellt Gruppen von Nachrichten (genannt „Communications") und deren Relationen zwischen Prozessen und Teilnehmern dar.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/konversation">
  <collaboration id="konv_review">

    <participant id="part_student" name="Student"/>
    <participant id="part_mitarbeiter" name="Mitarbeiter"/>

    <conversation id="conv1" name="Review anbahnen und abschließen">
      <participantRef>part_student</participantRef>
      <participantRef>part_mitarbeiter</participantRef>
    </conversation>

  </collaboration>
</definitions>
```

## Diagrammarten: Choreographiediagramm

Stellt die Interaktion von Teilnehmern mit Aktivitäten und Benutzern oder von Ressourcen und den daraus resultierenden Nachrichten dar.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/choreographie">
  <choreography id="choreo_abschlussarbeit" name="Abschlussarbeit Bewertung">

    <startEvent id="choreo_start"/>

    <sequenceFlow id="csf1" sourceRef="choreo_start" targetRef="ctask1"/>

    <choreographyTask id="ctask1" name="Letztes Korrekturlesen der Abschlussarbeit durch den Betreuer"
                      initiatingParticipantRef="cpart_student">
      <participantRef>cpart_student</participantRef>
      <participantRef>cpart_mitarbeiter</participantRef>
      <messageFlowRef>cmf_abschlussarbeit</messageFlowRef>
      <messageFlowRef>cmf_anmerkungen</messageFlowRef>
    </choreographyTask>

    <sequenceFlow id="csf2" sourceRef="ctask1" targetRef="ctask2"/>

    <choreographyTask id="ctask2" name="Aufforderung zum Einarbeiten der Anmerkungen"
                      initiatingParticipantRef="cpart_mitarbeiter">
      <participantRef>cpart_student</participantRef>
      <participantRef>cpart_mitarbeiter</participantRef>
    </choreographyTask>

    <sequenceFlow id="csf3" sourceRef="ctask2" targetRef="ctask3"/>

    <choreographyTask id="ctask3" name="Bewertung der finalisierten Abschlussarbeit durch den Professor"
                      initiatingParticipantRef="cpart_student">
      <participantRef>cpart_student</participantRef>
      <participantRef>cpart_professor</participantRef>
      <messageFlowRef>cmf_finale_abschlussarbeit</messageFlowRef>
      <messageFlowRef>cmf_note</messageFlowRef>
    </choreographyTask>

    <sequenceFlow id="csf4" sourceRef="ctask3" targetRef="choreo_end"/>

    <endEvent id="choreo_end"/>

    <participant id="cpart_student" name="Student"/>
    <participant id="cpart_mitarbeiter" name="Mitarbeiter"/>
    <participant id="cpart_professor" name="Professor"/>

    <messageFlow id="cmf_abschlussarbeit" name="Abschlussarbeit"
                 sourceRef="cpart_student" targetRef="ctask1"/>
    <messageFlow id="cmf_anmerkungen" name="Anmerkungen"
                 sourceRef="cpart_mitarbeiter" targetRef="ctask1"/>
    <messageFlow id="cmf_finale_abschlussarbeit" name="finale Abschlussarbeit"
                 sourceRef="cpart_student" targetRef="ctask3"/>
    <messageFlow id="cmf_note" name="Note"
                 sourceRef="cpart_professor" targetRef="ctask3"/>

  </choreography>
</definitions>
```

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

## Beispiel: Ad-Hoc und Schleife

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/adhoc-schleife">
  <process id="proc_zusteller" name="Zeitungszustellung" isExecutable="false">

    <startEvent id="start"/>
    <sequenceFlow id="sf1" sourceRef="start" targetRef="task_zur_arbeit"/>

    <task id="task_zur_arbeit" name="zur Arbeit fahren"/>
    <sequenceFlow id="sf2" sourceRef="task_zur_arbeit" targetRef="sub_zentrale"/>

    <!-- Teilprozess: Zentrale betreten (paralleles Gateway innen) -->
    <subProcess id="sub_zentrale" name="Zentrale betreten">
      <startEvent id="sub_start"/>
      <sequenceFlow id="sub_sf1" sourceRef="sub_start" targetRef="gw_par_split"/>
      <parallelGateway id="gw_par_split"/>
      <sequenceFlow id="sub_sf2" sourceRef="gw_par_split" targetRef="task_karte"/>
      <sequenceFlow id="sub_sf3" sourceRef="gw_par_split" targetRef="task_detektor"/>
      <task id="task_karte" name="Schlüsselkarte verifizieren"/>
      <task id="task_detektor" name="Metalldetektor passieren"/>
      <sequenceFlow id="sub_sf4" sourceRef="task_karte" targetRef="gw_par_join"/>
      <sequenceFlow id="sub_sf5" sourceRef="task_detektor" targetRef="gw_par_join"/>
      <parallelGateway id="gw_par_join"/>
      <sequenceFlow id="sub_sf6" sourceRef="gw_par_join" targetRef="sub_end"/>
      <endEvent id="sub_end"/>
    </subProcess>

    <sequenceFlow id="sf3" sourceRef="sub_zentrale" targetRef="sub_fahrt"/>

    <!-- Ad-Hoc Teilprozess: Fahrt vorbereiten -->
    <adHocSubProcess id="sub_fahrt" name="Fahrt vorbereiten" ordering="Parallel">
      <task id="task_fahrzeug_pruefen" name="Fahrzeug prüfen"/>
      <task id="task_verkehr" name="Verkehrsinfos prüfen"/>
      <task id="task_beladen" name="Fahrzeug beladen"/>
    </adHocSubProcess>

    <sequenceFlow id="sf4" sourceRef="sub_fahrt" targetRef="task_zielgebiet"/>

    <task id="task_zielgebiet" name="Ins Zielgebiet fahren"/>
    <sequenceFlow id="sf5" sourceRef="task_zielgebiet" targetRef="task_zeitung"/>

    <!-- Mehrfachausführung sequenziell -->
    <task id="task_zeitung" name="Zeitung zustellen">
      <multiInstanceLoopCharacteristics isSequential="true"/>
    </task>
    <dataObjectReference id="dor_abonnenten" name="Liste der Abonnenten"/>
    <dataInputAssociation id="dia1" sourceRef="dor_abonnenten" targetRef="task_zeitung"/>

    <sequenceFlow id="sf6" sourceRef="task_zeitung" targetRef="task_zurueck"/>

    <task id="task_zurueck" name="zurückfahren"/>
    <sequenceFlow id="sf7" sourceRef="task_zurueck" targetRef="gw_event"/>

    <!-- Ereignis-basiertes Gateway: kein Parkplatz frei vs. Parkplatz frei -->
    <eventBasedGateway id="gw_event"/>
    <sequenceFlow id="sf8" name="kein Parkplatz frei" sourceRef="gw_event" targetRef="task_block"/>
    <sequenceFlow id="sf9" name="Parkplatz frei" sourceRef="gw_event" targetRef="task_parken"/>

    <!-- Schleife-Task: um den Block fahren -->
    <task id="task_block" name="um den Block fahren">
      <standardLoopCharacteristics testBefore="false">
        <loopCondition xsi:type="tFormalExpression">kein Parkplatz frei</loopCondition>
      </standardLoopCharacteristics>
    </task>
    <sequenceFlow id="sf10" name="bis Parkplatz frei" sourceRef="task_block" targetRef="task_parken"/>

    <task id="task_parken" name="parken"/>
    <sequenceFlow id="sf11" sourceRef="task_parken" targetRef="task_nach_hause"/>

    <task id="task_nach_hause" name="nach Hause fahren"/>
    <sequenceFlow id="sf12" sourceRef="task_nach_hause" targetRef="end"/>

    <endEvent id="end"/>

  </process>
</definitions>
```

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

## Flow Objects: Beispiel 1

Bestellverarbeitung mit exklusivem Gateway.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/bestellung">
  <process id="proc_bestellung" name="Bestellverarbeitung" isExecutable="false">

    <startEvent id="start">
      <messageEventDefinition/>
    </startEvent>
    <dataObjectReference id="dor_bestellung" name="Bestellung"/>
    <sequenceFlow id="sf1" sourceRef="start" targetRef="task_bestand"/>

    <serviceTask id="task_bestand" name="Bestand prüfen"/>
    <sequenceFlow id="sf2" sourceRef="task_bestand" targetRef="gw_xor"/>

    <exclusiveGateway id="gw_xor"/>
    <sequenceFlow id="sf3" name="Waren vorhanden" sourceRef="gw_xor" targetRef="task_verarbeiten"/>
    <sequenceFlow id="sf4" name="Waren nicht vorhanden" sourceRef="gw_xor" targetRef="task_absage"/>

    <userTask id="task_verarbeiten" name="Bestellung verarbeiten"/>
    <sequenceFlow id="sf5" sourceRef="task_verarbeiten" targetRef="end_ok"/>
    <endEvent id="end_ok"/>

    <userTask id="task_absage" name="Absage formulieren"/>
    <sequenceFlow id="sf6" sourceRef="task_absage" targetRef="end_absage"/>
    <endEvent id="end_absage"/>

  </process>
</definitions>
```

## Flow Objects: Beispiel 2

Geburtstagseinladung mit ereignis-basiertem Gateway.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/geburtstag">
  <process id="proc_geburtstag" name="Geburtstagseinladung" isExecutable="false">

    <startEvent id="start"/>
    <sequenceFlow id="sf1" sourceRef="start" targetRef="task_einladung"/>

    <task id="task_einladung" name="Einladung zum Geburtstag verschicken"/>
    <sequenceFlow id="sf2" sourceRef="task_einladung" targetRef="gw_event"/>

    <!-- Ereignis-basiertes Gateway: reagiert auf das zuerst eintretende Ereignis -->
    <eventBasedGateway id="gw_event"/>

    <sequenceFlow id="sf3" sourceRef="gw_event" targetRef="catch_zusage"/>
    <sequenceFlow id="sf4" sourceRef="gw_event" targetRef="catch_absage"/>
    <sequenceFlow id="sf5" sourceRef="gw_event" targetRef="catch_timer"/>

    <intermediateCatchEvent id="catch_zusage" name="Zusage eingetroffen">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sf6" sourceRef="catch_zusage" targetRef="task_freuen"/>

    <intermediateCatchEvent id="catch_absage" name="Absage eingetroffen">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sf7" sourceRef="catch_absage" targetRef="task_traurig"/>

    <intermediateCatchEvent id="catch_timer" name="4 Wochen verstrichen">
      <timerEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sf8" sourceRef="catch_timer" targetRef="task_rueckfrage"/>

    <task id="task_freuen" name="Sich freuen"/>
    <task id="task_traurig" name="Traurig sein"/>
    <task id="task_rueckfrage" name="Rückfrage bei potentiellem Gast"/>

  </process>
</definitions>
```

## Swimlanes

Swimlanes dienen dazu Rollen, Zuständigkeiten oder auch Organisationsstrukturen abzubilden. Unterschieden werden Pools und Lanes.

- **Pools:** Repräsentieren abstrakte Rollen (z. B. „Kunde" oder „Lieferant") oder konkrete Instanziierungen dieser Rollen. Ein Pool besitzt Lanes.
- **Lanes:** Unterteilen Pools mit dem Zweck, Aktivitäten oder Zuständigkeiten innerhalb eines Pools zu modellieren. Eine Lane befindet sich stets innerhalb eines Pools.
- **Nachrichtenflüsse:** Dienen dazu, den Informationsfluss über organisatorische Grenzen hinweg zu modellieren. Sie fließen dabei zwischen verschiedenen Pools. Verbunden werden können dabei neben den Pools selber auch Aktivitäten oder Events in diesen.

## Swimlanes: Beispiel

Anfrage für Betreuung einer Bachelorarbeit – Ausschnitt.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/swimlanes-beispiel">
  <collaboration id="collab_sw">
    <participant id="pool_sw_student" name="Student" processRef="proc_sw_student"/>
    <participant id="pool_sw_professor" name="Professor" processRef="proc_sw_professor"/>
    <messageFlow id="mf_sw1" name="Anfrage" sourceRef="catch_anfrage_s" targetRef="catch_anfrage_p"/>
    <messageFlow id="mf_sw2" name="Anforderung Exposé" sourceRef="throw_bitte_p" targetRef="catch_bitte_s"/>
  </collaboration>

  <process id="proc_sw_student" name="Student">
    <laneSet>
      <lane id="lane_student" name="Student">
        <flowNodeRef>start_s</flowNodeRef>
        <flowNodeRef>task_anfrage_form</flowNodeRef>
        <flowNodeRef>catch_anfrage_s</flowNodeRef>
        <flowNodeRef>catch_bitte_s</flowNodeRef>
      </lane>
    </laneSet>
    <startEvent id="start_s"/>
    <sequenceFlow id="sf_sw_s1" sourceRef="start_s" targetRef="task_anfrage_form"/>
    <task id="task_anfrage_form" name="Anfrage für Betreuung der Bachelorarbeit formulieren"/>
    <sequenceFlow id="sf_sw_s2" sourceRef="task_anfrage_form" targetRef="catch_anfrage_s"/>
    <intermediateThrowEvent id="catch_anfrage_s" name="Anfrage versendet">
      <messageEventDefinition/>
    </intermediateThrowEvent>
    <sequenceFlow id="sf_sw_s3" sourceRef="catch_anfrage_s" targetRef="catch_bitte_s"/>
    <intermediateCatchEvent id="catch_bitte_s" name="Bitte um Exposé erhalten">
      <messageEventDefinition/>
    </intermediateCatchEvent>
  </process>

  <process id="proc_sw_professor" name="Professor">
    <laneSet>
      <lane id="lane_professor" name="Professor">
        <flowNodeRef>catch_anfrage_p</flowNodeRef>
        <flowNodeRef>task_bitte_form</flowNodeRef>
        <flowNodeRef>throw_bitte_p</flowNodeRef>
      </lane>
    </laneSet>
    <intermediateCatchEvent id="catch_anfrage_p" name="Anfrage erhalten">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sf_sw_p1" sourceRef="catch_anfrage_p" targetRef="task_bitte_form"/>
    <task id="task_bitte_form" name="Bitte um Exposé formulieren"/>
    <sequenceFlow id="sf_sw_p2" sourceRef="task_bitte_form" targetRef="throw_bitte_p"/>
    <intermediateThrowEvent id="throw_bitte_p" name="Bitte um Exposé verschickt">
      <messageEventDefinition/>
    </intermediateThrowEvent>
  </process>
</definitions>
```

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

## Beispiel: Anfrage für Betreuung einer Bachelorarbeit

Vollständiges Kollaborationsdiagramm mit zwei Pools (Student und Professor), Nachrichtenflüssen, Datenobjekten und Sequenzflüssen.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/bachelorarbeit-anfrage">
  <collaboration id="collab_ba">
    <participant id="pool_student" name="Student" processRef="proc_student"/>
    <participant id="pool_professor" name="Professor" processRef="proc_professor"/>

    <messageFlow id="mf1" name="Anfrage" sourceRef="throw_anfrage" targetRef="catch_anfrage"/>
    <messageFlow id="mf2" name="Anforderung Exposé" sourceRef="throw_bitte_expose" targetRef="catch_bitte_expose"/>
    <messageFlow id="mf3" name="Exposé" sourceRef="throw_expose" targetRef="catch_expose"/>
  </collaboration>

  <process id="proc_student" name="Student">
    <laneSet>
      <lane id="lane_s" name="Student">
        <flowNodeRef>start_s</flowNodeRef>
        <flowNodeRef>task_anfrage</flowNodeRef>
        <flowNodeRef>throw_anfrage</flowNodeRef>
        <flowNodeRef>catch_bitte_expose</flowNodeRef>
        <flowNodeRef>task_expose_formulieren</flowNodeRef>
        <flowNodeRef>throw_expose</flowNodeRef>
      </lane>
    </laneSet>

    <startEvent id="start_s"/>
    <sequenceFlow id="sfs1" sourceRef="start_s" targetRef="task_anfrage"/>

    <task id="task_anfrage" name="Anfrage für Betreuung der Bachelorarbeit formulieren"/>
    <sequenceFlow id="sfs2" sourceRef="task_anfrage" targetRef="throw_anfrage"/>

    <intermediateThrowEvent id="throw_anfrage" name="Anfrage versendet">
      <messageEventDefinition/>
    </intermediateThrowEvent>
    <sequenceFlow id="sfs3" sourceRef="throw_anfrage" targetRef="catch_bitte_expose"/>

    <intermediateCatchEvent id="catch_bitte_expose" name="Bitte um Exposé erhalten">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sfs4" sourceRef="catch_bitte_expose" targetRef="task_expose_formulieren"/>

    <task id="task_expose_formulieren" name="Exposé formulieren"/>
    <sequenceFlow id="sfs5" sourceRef="task_expose_formulieren" targetRef="throw_expose"/>

    <intermediateThrowEvent id="throw_expose" name="Exposé verschicken">
      <messageEventDefinition/>
    </intermediateThrowEvent>

    <dataObjectReference id="dor_expose" name="Exposé"/>
    <dataOutputAssociation id="doa1" sourceRef="task_expose_formulieren" targetRef="dor_expose"/>
    <dataInputAssociation id="dia1" sourceRef="dor_expose" targetRef="throw_expose"/>
  </process>

  <process id="proc_professor" name="Professor">
    <laneSet>
      <lane id="lane_p" name="Professor">
        <flowNodeRef>catch_anfrage</flowNodeRef>
        <flowNodeRef>task_bitte_formulieren</flowNodeRef>
        <flowNodeRef>throw_bitte_expose</flowNodeRef>
        <flowNodeRef>catch_expose</flowNodeRef>
        <flowNodeRef>task_expose_pruefen</flowNodeRef>
        <flowNodeRef>gw_expose</flowNodeRef>
        <flowNodeRef>task_anmeldung</flowNodeRef>
        <flowNodeRef>task_kommentarlos</flowNodeRef>
        <flowNodeRef>end_p</flowNodeRef>
      </lane>
    </laneSet>

    <intermediateCatchEvent id="catch_anfrage" name="Anfrage erhalten">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sfp1" sourceRef="catch_anfrage" targetRef="task_bitte_formulieren"/>

    <task id="task_bitte_formulieren" name="Bitte um Exposé formulieren"/>
    <sequenceFlow id="sfp2" sourceRef="task_bitte_formulieren" targetRef="throw_bitte_expose"/>

    <intermediateThrowEvent id="throw_bitte_expose" name="Bitte um Exposé verschickt">
      <messageEventDefinition/>
    </intermediateThrowEvent>
    <sequenceFlow id="sfp3" sourceRef="throw_bitte_expose" targetRef="catch_expose"/>

    <intermediateCatchEvent id="catch_expose" name="Exposé erhalten">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sfp4" sourceRef="catch_expose" targetRef="task_expose_pruefen"/>

    <task id="task_expose_pruefen" name="Exposé prüfen"/>
    <sequenceFlow id="sfp5" sourceRef="task_expose_pruefen" targetRef="gw_expose"/>

    <exclusiveGateway id="gw_expose"/>
    <sequenceFlow id="sfp6" sourceRef="gw_expose" targetRef="task_anmeldung"/>
    <sequenceFlow id="sfp7" sourceRef="gw_expose" targetRef="task_kommentarlos"/>

    <task id="task_anmeldung" name="Anmeldung unterschreiben"/>
    <sequenceFlow id="sfp8" sourceRef="task_anmeldung" targetRef="end_p"/>

    <task id="task_kommentarlos" name="Kommentarlos ignorieren"/>
    <sequenceFlow id="sfp9" sourceRef="task_kommentarlos" targetRef="end_p"/>

    <endEvent id="end_p"/>
  </process>
</definitions>
```

## Übungsaufgabe: Bewertung einer Bachelorarbeit

Prozessbeschreibung:
- Der Professor erhält die Nachricht, dass die BA angemeldet ist, trägt sich die Abgabefrist in den Kalender ein und wartet.
- Anschließend erhält er entweder die Bachelorarbeit oder die Frist läuft ab.
  - Nach Fristablauf erkundigt er sich beim Prüfungsamt und bekommt mitgeteilt, dass keine Verlängerung gewährt wurde (Prozess endet) oder eine Verlängerung gewährt wurde (neue Frist eintragen, erneut warten).
- Nach Erhalt der Bachelorarbeit liest er diese. Entdeckt er ein Plagiat, hört er auf zu lesen, meldet das Plagiat dem Prüfungsamt, und der Prozess endet.
- Gab es kein Plagiat, schreibt er das Gutachten. Wird er dabei traurig, schaltet er Musik an und hört diese, bis entweder 10 Minuten vergangen sind oder er nicht mehr traurig ist; dann schaltet er sie aus.
- Nach Fertigstellung des Gutachtens teilt er dem Studenten den Verteidigungstermin mit und erhält eine Terminbestätigung. Er kündigt den Termin allgemein an.
- Wenn der Verteidigungstermin erreicht ist, hört er den Vortrag des Studenten und verkündet die Note.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             targetNamespace="http://example.org/bachelorarbeit-bewertung">
  <process id="proc_bewertung" name="Bewertung einer Bachelorarbeit" isExecutable="false">

    <!-- Start: BA ist angemeldet (Nachrichtenereignis) -->
    <startEvent id="start">
      <messageEventDefinition/>
    </startEvent>
    <dataObjectReference id="dor_ba_angemeldet" name="BA ist angemeldet"/>

    <sequenceFlow id="sf1" sourceRef="start" targetRef="gw_xor_start"/>

    <!-- XOR-Gateway: Eingehende Nachricht trigerrt parallelen Pfad -->
    <exclusiveGateway id="gw_xor_start"/>
    <sequenceFlow id="sf2" sourceRef="gw_xor_start" targetRef="task_frist_eintragen"/>

    <task id="task_frist_eintragen" name="Abgabefrist im Kalender eintragen"/>
    <sequenceFlow id="sf3" sourceRef="task_frist_eintragen" targetRef="gw_event_wait"/>

    <!-- Ereignis-basiertes Gateway: BA erhalten ODER Frist abgelaufen -->
    <eventBasedGateway id="gw_event_wait"/>
    <sequenceFlow id="sf4" sourceRef="gw_event_wait" targetRef="catch_ba_erhalten"/>
    <sequenceFlow id="sf5" sourceRef="gw_event_wait" targetRef="catch_frist_ablauf"/>

    <!-- Pfad 1: BA erhalten -->
    <intermediateCatchEvent id="catch_ba_erhalten" name="BA erhalten">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <dataObjectReference id="dor_ba" name="BA"/>
    <dataInputAssociation id="dia_ba" sourceRef="dor_ba" targetRef="catch_ba_erhalten"/>
    <sequenceFlow id="sf6" sourceRef="catch_ba_erhalten" targetRef="task_lesen"/>

    <task id="task_lesen" name="Bachelorarbeit lesen">
      <multiInstanceLoopCharacteristics isSequential="true"/>
    </task>
    <sequenceFlow id="sf7" sourceRef="task_lesen" targetRef="gw_plagiat"/>

    <!-- XOR: Plagiat entdeckt? -->
    <exclusiveGateway id="gw_plagiat"/>
    <sequenceFlow id="sf8" name="Plagiat entdeckt" sourceRef="gw_plagiat" targetRef="task_plagiat_melden"/>
    <sequenceFlow id="sf9" name="Plagiat" sourceRef="gw_plagiat" targetRef="task_gutachten"/>

    <task id="task_plagiat_melden" name="Plagiat ans Prüfungsamt melden">
      <messageEventDefinition/>
    </task>
    <sequenceFlow id="sf10" sourceRef="task_plagiat_melden" targetRef="end_plagiat"/>
    <endEvent id="end_plagiat">
      <messageEventDefinition/>
    </endEvent>

    <!-- Gutachten schreiben -->
    <task id="task_gutachten" name="Gutachten schreiben">
      <multiInstanceLoopCharacteristics isSequential="true"/>
    </task>
    <sequenceFlow id="sf11" sourceRef="task_gutachten" targetRef="gw_traurig"/>

    <!-- Ereignis-basiertes Gateway: traurig? -->
    <eventBasedGateway id="gw_traurig"/>
    <sequenceFlow id="sf12" name="traurig" sourceRef="gw_traurig" targetRef="task_musik_an"/>
    <sequenceFlow id="sf13" sourceRef="gw_traurig" targetRef="task_termin_mitteilen"/>

    <task id="task_musik_an" name="Musik anschalten"/>
    <sequenceFlow id="sf14" sourceRef="task_musik_an" targetRef="gw_event_musik"/>

    <!-- Ereignis-basiertes Gateway: 10 Minuten ODER nicht mehr traurig -->
    <eventBasedGateway id="gw_event_musik"/>
    <sequenceFlow id="sf15" sourceRef="gw_event_musik" targetRef="catch_10min"/>
    <sequenceFlow id="sf16" sourceRef="gw_event_musik" targetRef="catch_nicht_traurig"/>

    <intermediateCatchEvent id="catch_10min" name="10 Minuten vergangen">
      <timerEventDefinition/>
    </intermediateCatchEvent>
    <intermediateCatchEvent id="catch_nicht_traurig" name="nicht mehr traurig">
      <conditionalEventDefinition/>
    </intermediateCatchEvent>

    <sequenceFlow id="sf17" sourceRef="catch_10min" targetRef="gw_xor_musik_join"/>
    <sequenceFlow id="sf18" sourceRef="catch_nicht_traurig" targetRef="gw_xor_musik_join"/>

    <exclusiveGateway id="gw_xor_musik_join"/>
    <sequenceFlow id="sf19" sourceRef="gw_xor_musik_join" targetRef="task_musik_aus"/>

    <task id="task_musik_aus" name="Musik ausschalten"/>
    <sequenceFlow id="sf20" sourceRef="task_musik_aus" targetRef="task_termin_mitteilen"/>

    <!-- Termin mitteilen und Bestätigung empfangen -->
    <task id="task_termin_mitteilen" name="Student Termin der Verteidigung mitteilen">
      <messageEventDefinition/>
    </task>
    <sequenceFlow id="sf21" sourceRef="task_termin_mitteilen" targetRef="catch_terminbestaetigung"/>

    <intermediateCatchEvent id="catch_terminbestaetigung" name="Terminbestätigung">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sf22" sourceRef="catch_terminbestaetigung" targetRef="task_termin_ankuendigen"/>

    <task id="task_termin_ankuendigen" name="Termin ankündigen">
      <signalEventDefinition/>
    </task>
    <dataObjectReference id="dor_ankuendigung" name="Ankündigung"/>
    <dataOutputAssociation id="doa_ankuendigung" sourceRef="task_termin_ankuendigen" targetRef="dor_ankuendigung"/>
    <sequenceFlow id="sf23" sourceRef="task_termin_ankuendigen" targetRef="catch_verteidigung"/>

    <intermediateCatchEvent id="catch_verteidigung" name="Verteidigungstermin erreicht">
      <timerEventDefinition/>
    </intermediateCatchEvent>
    <dataObjectReference id="dor_termin" name="Termin"/>
    <dataInputAssociation id="dia_termin" sourceRef="dor_termin" targetRef="catch_verteidigung"/>
    <sequenceFlow id="sf24" sourceRef="catch_verteidigung" targetRef="task_vortrag"/>

    <task id="task_vortrag" name="Vortrag hören"/>
    <sequenceFlow id="sf25" sourceRef="task_vortrag" targetRef="task_note"/>

    <task id="task_note" name="Note verkünden">
      <messageEventDefinition/>
    </task>
    <sequenceFlow id="sf26" sourceRef="task_note" targetRef="end_normal"/>
    <endEvent id="end_normal">
      <messageEventDefinition/>
    </endEvent>

    <!-- Pfad 2: Frist abgelaufen -->
    <intermediateCatchEvent id="catch_frist_ablauf" name="Frist abgelaufen">
      <timerEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sf27" sourceRef="catch_frist_ablauf" targetRef="task_erkundigung"/>

    <task id="task_erkundigung" name="Erkundigung beim Prüfungsamt einholen"/>
    <sequenceFlow id="sf28" sourceRef="task_erkundigung" targetRef="gw_verlaengerung"/>

    <eventBasedGateway id="gw_verlaengerung"/>
    <sequenceFlow id="sf29" name="keine Verlängerung gewährt" sourceRef="gw_verlaengerung" targetRef="end_keine_verlaengerung"/>
    <sequenceFlow id="sf30" name="Verlängerung gewährt" sourceRef="gw_verlaengerung" targetRef="catch_verlaengerung"/>

    <endEvent id="end_keine_verlaengerung">
      <terminateEventDefinition/>
    </endEvent>

    <intermediateCatchEvent id="catch_verlaengerung" name="Verlängerung gewährt">
      <messageEventDefinition/>
    </intermediateCatchEvent>
    <sequenceFlow id="sf31" sourceRef="catch_verlaengerung" targetRef="task_neue_frist"/>

    <task id="task_neue_frist" name="Neue Frist im Kalender eintragen"/>
    <sequenceFlow id="sf32" sourceRef="task_neue_frist" targetRef="gw_event_wait"/>

  </process>
</definitions>
```
