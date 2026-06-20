dataset = [
    # --- BPMN: Modell-Evaluierung ---
    {
        "question": "Bewerte die folgende Antwort: „Artefakte wie Gruppen und Text-Annotationen sind in BPMN essenziell, da sie den Kontrollfluss eines Prozesses verändern und steuern."",
        "ground_truth": "Die Antwort ist falsch. Artefakte beeinflussen den Kontrollfluss eines Prozesses nicht. Sie dienen vielmehr der reinen Dokumentation des Modells und stellen dem Leser zusätzliche Informationen bereit.",
    },
    {
        "question": "Bewerte die folgende Antwort: „Der Sequenzfluss wird in BPMN genutzt, um den Austausch von E-Mails und Nachrichten zwischen zwei völlig unabhängigen Unternehmen darzustellen."",
        "ground_truth": "Die Antwort ist falsch. Für den Austausch von Nachrichten zwischen verschiedenen Entitäten oder Teilnehmern wird der Nachrichtenfluss verwendet. Der Sequenzfluss definiert hingegen die zeitliche und logische Reihenfolge von Aktivitäten innerhalb eines Prozesses.",
    },
    {
        "question": "Bewerte die folgende Antwort: „Ein Ereignis (Event) in BPMN wird als Kreis dargestellt und kann entweder ein Startereignis, ein Zwischenereignis oder ein Endereignis sein."",
        "ground_truth": "Die Antwort ist richtig. Ein Event repräsentiert ein Ereignis innerhalb eines Geschäftsprozesses, wird als Kreis modelliert und es wird genau in diese drei Arten (Start, Zwischen, Ende) unterschieden, wobei Start- und Zwischenereignisse zusätzlich unterbrechend oder nicht-unterbrechend sein können.",
    },
    {
        "question": "Bewerte die folgende Antwort: „Der Nachrichtenfluss (Message Flow) wird in BPMN verwendet, um die strikte zeitliche Reihenfolge von Aktivitäten innerhalb eines einzelnen Pools zu definieren."",
        "ground_truth": "Die Antwort ist falsch. Der beschriebene Zweck trifft auf den Sequenzfluss zu. Der Nachrichtenfluss repräsentiert stattdessen den Austausch von Nachrichten zwischen verschiedenen Entitäten oder Teilnehmern (also über Pool-Grenzen hinweg).",
    },
    {
        "question": "Bewerte die folgende Antwort: „Ein Manueller Task (Manual Task) zeichnet sich dadurch aus, dass er von einem Benutzer zwingend mit IT-Unterstützung durchgeführt wird."",
        "ground_truth": "Die Antwort ist falsch. Ein Manueller Task wird per Definition ohne IT-Unterstützung durchgeführt. Ein Task, der von einem Benutzer mit IT-Unterstützung ausgeführt wird, ist stattdessen ein Benutzer-Task (User Task).",
    },
    {
        "question": "Bewerte die folgende Antwort: „Eine Text-Annotation ist ein steuerndes Element (Flow Object), das den Kontrollfluss eines Geschäftsprozesses direkt verändert und verzweigt."",
        "ground_truth": "Die Antwort ist falsch. Eine Text-Annotation gehört zu den Artefakten (Artifacts) und beeinflusst den Kontrollfluss nicht. Sie dient lediglich der Dokumentation und stellt dem Leser zusätzliche Informationen zum Modell bereit.",
    },
    {
        "question": "Bewerte die folgende Antwort: „Ja, ein Timer (Zeit-Ereignis) in BPMN kann verwendet werden, um auf periodische zeitliche Ereignisse, spezifische Zeitpunkte oder Zeitspannen zu reagieren."",
        "ground_truth": "Die Antwort ist richtig. Ein Timer in BPMN gehört zu den Ereignissen (Events) und wird exakt für die Abbildung von periodischen Ereignissen, bestimmten Zeitpunkten oder abgelaufenen Zeitspannen eingesetzt.",
    },
    {
        "question": "Bewerte die folgende Antwort: „Ja, ein Datenspeicher (Data Store) wird in BPMN verwendet, um Daten darzustellen, auf die ausschließlich innerhalb eines einzelnen Teilprozesses zugegriffen werden kann."",
        "ground_truth": "Die Antwort ist falsch. Ein Datenspeicher repräsentiert einen Speicher, auf den explizit prozessübergreifend sowohl lesend als auch schreibend zugegriffen werden kann.",
    },
    {
        "question": "Bewerte die folgende Antwort: „Prozessfragmentierung in arbeitsteiligen Organisationen ist ein großer Vorteil, weil dadurch jeder Mitarbeiter die volle Verantwortung für den Gesamtprozess übernimmt und Warteschlangen bei der Übergabe vermieden werden."",
        "ground_truth": "Die Antwort ist falsch. Prozessfragmentierung führt in der Praxis oft genau zum Gegenteil: Es gibt häufig keine klar definierte Verantwortung für den Gesamtprozess, die Fehleranfälligkeit steigt durch die vielen Beteiligten, und die zahlreichen Übergaben zwischen den Stationen führen zu Warteschlangen und Verzögerungen.",
    },
    {
        "question": "Bewerte die folgende Antwort: „Eine Aufruf-Aktivität (Call Activity) wird in BPMN verwendet, um einen lokalen Teilprozess darzustellen, der ausschließlich für dieses eine Diagramm gültig ist und nicht wiederverwendet werden kann."",
        "ground_truth": "Die Antwort ist falsch. Eine Aufruf-Aktivität repräsentiert einen Teilprozess oder eine Aufgabe, welche global definiert sind und eben genau deshalb im aktuellen Prozess wiederverwendet werden können. Ein normaler Teilprozess ist hingegen fest in den umgebenden Prozess eingebettet.",
    },
    # --- Petri-Netze ---
    {
        "question": "Was ist ein Petri-Netz?",
        "ground_truth": "Ein Petri-Netz ist ein gerichteter bipartiter Graph, der aus Stellen (Places), Transitionen (Transitions) und einer Flussrelation (Arcs) besteht. Es dient zur Modellierung von nebenläufigen Prozessen, Kausalität und Ressourcenverbrauch.",
    },
    {
        "question": "Was repräsentieren Stellen und Transitionen in einem Petri-Netz?",
        "ground_truth": "Stellen repräsentieren Zustände, Bedingungen oder Ressourcen. Transitionen repräsentieren Ereignisse, Aktionen oder Aktivitäten, die den Systemzustand verändern.",
    },
    {
        "question": "Was ist eine Markierung in einem Petri-Netz?",
        "ground_truth": "Eine Markierung (Marking) beschreibt den aktuellen Zustand des Netzes. Sie gibt an, wie viele Marken (Tokens) sich in welchen Stellen befinden.",
    },
    {
        "question": "Wann ist eine Transition aktiviert (enabled)?",
        "ground_truth": "Eine Transition ist aktiviert, wenn alle Stellen in ihrem Vorbereich (Pre-Set) mindestens eine Marke besitzen und keine Stelle in ihrem Nachbereich (Post-Set) blockiert ist.",
    },
    {
        "question": "Was passiert, wenn eine Transition feuert (schaltet)?",
        "ground_truth": "Beim Feuern wird aus jeder Stelle im Vorbereich eine Marke entfernt und in jede Stelle im Nachbereich eine Marke hinzugefügt. Dadurch entsteht eine neue Markierung.",
    },
    {
        "question": "Was ist der Unterschied zwischen Kausalität und Nebenläufigkeit?",
        "ground_truth": "Kausalität bedeutet, dass das Feuern einer Transition das Feuern einer anderen direkt ermöglicht oder erzwingt. Nebenläufigkeit (Concurrency) liegt vor, wenn mehrere Transitionen unabhängig voneinander feuern können.",
    },
    {
        "question": "Was ist ein Konflikt in Petri-Netzen?",
        "ground_truth": "Ein Konflikt liegt vor, wenn mehrere Transitionen um dieselbe Marke konkurrieren und nur eine von ihnen feuern kann.",
    },
    {
        "question": "Was bedeutet es, dass ein Petri-Netz lebendig (live) ist?",
        "ground_truth": "Ein Petri-Netz ist lebendig, wenn von jeder erreichbaren Markierung aus jede Transition mindestens einmal feuern kann. Es gibt keine toten Transitionen.",
    },
    {
        "question": "Was ist der Vorbereich (Pre-Set) und Nachbereich (Post-Set) einer Transition?",
        "ground_truth": "Der Vorbereich enthält alle Stellen, von denen eine Kante zur Transition führt. Der Nachbereich enthält alle Stellen, zu denen eine Kante von der Transition führt.",
    },
    {
        "question": "Warum werden Petri-Netze häufig für die Modellierung von Geschäftsprozessen verwendet?",
        "ground_truth": "Petri-Netze eignen sich sehr gut zur Modellierung von nebenläufigen Prozessen, Ressourcenkonflikten, Synchronisation und Kausalitätsbeziehungen in komplexen Systemen.",
    },
    # --- UML ---
    {
        "question": "Was ist der Unterschied zwischen einer Assoziation und einer Aggregation in UML-Klassendiagrammen?",
        "ground_truth": "Eine Assoziation beschreibt eine allgemeine Beziehung zwischen Klassen ohne Besitzverhältnis. Eine Aggregation ist eine spezielle Form der Assoziation, die eine „Ganzes-Teil"-Beziehung darstellt, wobei die Teile unabhängig vom Ganzen existieren können.",
    },
    {
        "question": "Was ist Vererbung (Generalization) in UML?",
        "ground_truth": "Vererbung (Generalization) ist eine Beziehung zwischen einer Oberklasse und einer oder mehreren Unterklassen. Die Unterklassen erben Attribute und Methoden der Oberklasse und können diese erweitern oder überschreiben.",
    },
    {
        "question": "Was ist der Unterschied zwischen Aggregation und Komposition?",
        "ground_truth": "Bei einer Aggregation können die Teile unabhängig vom Ganzen existieren. Bei einer Komposition (starke Ganzes-Teil-Beziehung) existieren die Teile nicht ohne das Ganze – wenn das Ganze zerstört wird, werden auch die Teile zerstört.",
    },
    {
        "question": "Wofür wird ein Use-Case-Diagramm verwendet?",
        "ground_truth": "Ein Use-Case-Diagramm beschreibt die funktionalen Anforderungen eines Systems aus Sicht der Nutzer. Es zeigt Akteure, Use Cases und deren Beziehungen (Include, Extend).",
    },
    {
        "question": "Was ist eine Assoziationsklasse in UML?",
        "ground_truth": "Eine Assoziationsklasse ist eine Klasse, die einer Assoziation zugeordnet ist. Sie wird verwendet, wenn die Beziehung zwischen zwei Klassen selbst Attribute oder Methoden besitzt.",
    },
    {
        "question": "Erkläre den Unterschied zwischen einer Klasse und einem Objekt in UML.",
        "ground_truth": "Eine Klasse ist eine Beschreibung der Struktur und des Verhaltens (Blaupause). Ein Objekt ist eine konkrete Instanz dieser Klasse zur Laufzeit.",
    },
    {
        "question": "Was bedeutet Multiplizität in UML-Klassendiagrammen?",
        "ground_truth": "Multiplizität gibt an, wie viele Instanzen einer Klasse mit Instanzen einer anderen Klasse in Beziehung stehen können (z. B. 1, 0..1, 0..*, 1..*).",
    },
    {
        "question": "Wofür dient ein Sequenzdiagramm?",
        "ground_truth": "Ein Sequenzdiagramm zeigt die zeitliche Abfolge von Nachrichten und Interaktionen zwischen Objekten oder Komponenten eines Systems.",
    },
    {
        "question": "Was ist der Unterschied zwischen einer gerichteten und einer ungerichteten Assoziation?",
        "ground_truth": "Eine ungerichtete Assoziation zeigt nur, dass eine Beziehung existiert. Eine gerichtete Assoziation (mit Pfeil) zeigt die Navigationsrichtung – von welcher Klasse aus auf die andere zugegriffen werden kann.",
    },
    {
        "question": "Was ist ein Interface in UML und wie wird es dargestellt?",
        "ground_truth": "Ein Interface definiert eine vertragliche Schnittstelle ohne Implementierung. Es wird als Klasse mit dem Stereotyp «interface» oder als Kreis (Lollipop-Notation) dargestellt.",
    },
]
