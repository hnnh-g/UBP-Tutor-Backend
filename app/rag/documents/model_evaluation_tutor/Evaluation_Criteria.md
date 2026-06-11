# Evaluation Criteria for Diagram Assessment

This document defines the correctness criteria used to assess student-submitted diagrams in three notations: BPMN 2.0 (XML), UML (PlantUML), and Petri nets (PNML). For each notation and diagram type, criteria are organized into three tiers:

- **Structural correctness** — the diagram is syntactically valid and formally well-formed.
- **Semantic correctness** — the diagram correctly represents the described scenario.
- **Modeling quality** — the diagram is clear, minimal, and follows good modeling practice.

Each criterion is stated as a checkable condition with an explanation of what correct looks like and why the criterion matters. When a criterion is not met, feedback should name the violated criterion, identify the specific element where the violation occurs, explain why it is wrong, and state what the correct form would be.

---

## BPMN 2.0 — Process Diagram

### Structural Correctness

**SC-BPMN-P-01: Valid document frame**
The document uses `<?xml version="1.0" encoding="UTF-8"?>`, a `<definitions>` root element with `xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"`, and a non-empty `targetNamespace`. Without the correct namespace the document is not valid BPMN 2.0 and cannot be processed by any BPMN engine or validator. All elements have a unique `id` attribute — no two elements may share the same `id` within the document, because sequence flows reference elements by their `id`.

**SC-BPMN-P-02: Exactly one start event per process**
Each `<process>` element contains exactly one `<startEvent>`. The start event has no incoming sequence flows. Without a start event it is undefined where the process begins; with more than one start event it is undefined which one initiates the process.

**SC-BPMN-P-03: Every path ends with an end event**
Every path through the process — including every branch coming out of every gateway — terminates at an `<endEvent>`. No task or gateway is a dead end. The end event itself has no outgoing sequence flows. An open path means the process has no defined completion for that branch, which is both structurally invalid and semantically incomplete.

**SC-BPMN-P-04: All references are valid**
Every `sourceRef` and `targetRef` on a `<sequenceFlow>` points to an element `id` that exists within the same `<process>`. A reference to a non-existing or out-of-scope id is a broken reference that makes the flow invalid.

**SC-BPMN-P-05: Sequence flows stay within the process**
`<sequenceFlow>` elements only connect elements within the same `<process>`. They cannot cross pool boundaries. Communication between different participants (pools) must use `<messageFlow>` inside a `<collaboration>`, not sequence flows. Using sequence flows across pools is a fundamental structural error.

**SC-BPMN-P-06: Sub-processes have internal start and end events**
Every `<subProcess>` contains at least one `<startEvent>` and at least one `<endEvent>` as direct children, connected by an internal sequence flow. A sub-process without these is incomplete — it has no defined entry or exit point of its own.

**SC-BPMN-P-07: Gateways used as splits have at least two outgoing flows**
A gateway that splits the flow must have at least two outgoing sequence flows, otherwise it serves no purpose as a decision or parallel point. A gateway used purely as a join may have one outgoing flow.

**SC-BPMN-P-08: Parallel gateways are symmetric**
Every `<parallelGateway>` used as a split (multiple outgoing flows) is matched by a corresponding `<parallelGateway>` used as a join (multiple incoming flows) that re-synchronizes all parallel branches before the flow continues. Without a join, the parallel paths never converge and the process cannot complete correctly.

**SC-BPMN-P-09: Event types match their role**
Catching events (`<intermediateCatchEvent>`, `<startEvent>`) are used to receive signals or wait. Throwing events (`<intermediateThrowEvent>`, `<endEvent>`) are used to send signals or terminate. The event definition element (e.g. `<messageEventDefinition>`, `<timerEventDefinition>`) must be nested inside the correct event wrapper. A `<messageEventDefinition>` inside a `<intermediateThrowEvent>` means "send a message"; inside an `<intermediateCatchEvent>` it means "wait to receive a message". Mixing them up reverses the direction of communication.

**SC-BPMN-P-10: Task types are correctly assigned**
The task element tag matches the described behavior: `<userTask>` for a human performing a task with IT support, `<serviceTask>` for an automated system call, `<sendTask>` for sending a message, `<receiveTask>` for waiting to receive a message, `<manualTask>` for a human task without IT support, `<scriptTask>` for executing a script, `<businessRuleTask>` for evaluating a business rule. A generic `<task>` is only appropriate when none of the specific types applies.

### Semantic Correctness

**SE-BPMN-P-01: The modeled process matches the description**
Every step, decision, and event explicitly described in the task is represented in the diagram. No required activity, gateway decision, or event is missing. The flow between elements reflects the described order and dependencies.

**SE-BPMN-P-02: Exclusive gateways model mutually exclusive decisions**
An `<exclusiveGateway>` (XOR) is used when exactly one of several alternative paths is taken based on a condition. Each outgoing sequence flow carries a `name` attribute describing the condition under which that path is taken. The set of conditions must be exhaustive — every possible outcome is covered by at least one outgoing flow, and no two flows are simultaneously true. An exclusive gateway where conditions overlap or are missing is semantically incorrect.

**SE-BPMN-P-03: Parallel gateways model genuinely concurrent activities**
A `<parallelGateway>` (AND) is used only when all outgoing branches must execute simultaneously and all must complete before the flow continues. It must not be used as a shorthand for "either/or" decisions. Using a parallel gateway when the activities are actually alternatives is a semantic error that changes the process behavior fundamentally.

**SE-BPMN-P-04: Event-based gateways model waiting for the first event to occur**
An `<eventBasedGateway>` is followed exclusively by catching events (message, timer, conditional, signal) or receive tasks. It models the situation where the process waits and then takes whichever path's event occurs first. All other paths are abandoned. It is incorrect to follow an event-based gateway with tasks or gateways rather than events.

**SE-BPMN-P-05: Data objects and data stores reflect described data usage**
When the task description mentions a document, record, form, or data artifact being read or produced by an activity, the corresponding `<dataObjectReference>` or `<dataStoreReference>` is present and connected to the relevant task via `<dataInputAssociation>` (reading) or `<dataOutputAssociation>` (writing). Omitting data elements when the description explicitly references them is an incomplete model.

**SE-BPMN-P-06: Loop behavior is correctly modeled**
When the description requires a step or sequence to repeat until a condition is met, this repetition is explicitly represented — either with `<standardLoopCharacteristics>` on the task, or with a backward sequence flow leading to an earlier gateway that re-evaluates the loop condition. Simply omitting the loop produces a model that fires each step at most once, which does not match the described behavior.

### Modeling Quality

**MQ-BPMN-P-01: Gateway outgoing flows are labeled with conditions**
All outgoing sequence flows from exclusive and inclusive gateways carry a meaningful `name` attribute describing when that path is taken (e.g. "Approved", "Rejected", "Stock available"). Unlabeled gateway branches make the model unreadable and ambiguous.

**MQ-BPMN-P-02: Elements are meaningfully named**
Tasks use active verb phrases that describe what is done (e.g. "Review application", "Send invoice"). Events use noun phrases or past-tense descriptions of what occurred or is awaited (e.g. "Order received", "Payment confirmed", "Timer expired"). Names are specific enough to be understood without reading the surrounding model. Generic names like "Task 1" or "Event" are not acceptable.

**MQ-BPMN-P-03: The model does not contain invented elements**
The diagram models only what the task description requires. It does not add steps, events, decisions, or data objects not derivable from the description. Over-specification adds complexity without adding correctness.

**MQ-BPMN-P-04: The correct diagram type is used**
A single process within one organizational unit uses a process diagram. When the description involves communication between two or more autonomous participants (different organizations, systems, or roles with independent processes), a collaboration diagram with separate pools and message flows is required.

---

## BPMN 2.0 — Collaboration Diagram

All structural and semantic criteria from the Process Diagram section apply to each pool's internal process. The following criteria apply additionally at the collaboration level.

### Structural Correctness

**SC-BPMN-C-01: Collaboration element wraps all participants and message flows**
A `<collaboration>` element is present and contains all `<participant>` elements and `<messageFlow>` elements. Each `<participant>` references its corresponding `<process>` via `processRef`. Without this wrapper the collaboration structure is not valid BPMN.

**SC-BPMN-C-02: Message flows connect elements in different pools**
Every `<messageFlow>` has a `sourceRef` pointing to an element in one pool's process and a `targetRef` pointing to an element in a different pool's process. A message flow between two elements within the same pool is structurally wrong — it would need to be a sequence flow instead.

**SC-BPMN-C-03: No sequence flows cross pool boundaries**
`<sequenceFlow>` elements only connect elements within a single process. Cross-pool communication is exclusively expressed with `<messageFlow>`. A sequence flow crossing a pool boundary is a structural violation that breaks the independence of participants.

**SC-BPMN-C-04: Sending and receiving sides are correctly typed**
For each message flow, the sending side uses either a throwing message event (`<intermediateThrowEvent>` with `<messageEventDefinition>`) or a `<sendTask>`. The receiving side uses either a catching message event (`<intermediateCatchEvent>` or `<startEvent>` with `<messageEventDefinition>`) or a `<receiveTask>`. Using plain tasks on both ends is permissible only when no specific event semantics are required.

### Semantic Correctness

**SE-BPMN-C-01: Each pool contains the complete process of its participant**
Each pool models the full perspective of one autonomous participant. Internal decisions, steps, and waiting states that belong to a participant appear in that participant's pool. No participant's internal logic is placed in another participant's pool.

**SE-BPMN-C-02: All inter-participant communication is represented as message flows**
Every exchange of information between participants described in the task — every request, response, notification, or data transfer — is represented as a message flow. A missing message flow means a described interaction is absent from the model.

---

## BPMN 2.0 — Lanes

**SC-BPMN-L-01: Lanes are nested inside a pool**
Every `<lane>` element is a child of a `<laneSet>`, which is itself a direct child of a `<process>`. Lanes are not standalone elements and cannot exist outside a pool.

**SC-BPMN-L-02: Every flow element is assigned to a lane**
All flow nodes (tasks, events, gateways) in a process that uses lanes are listed in exactly one `<lane>` via `<flowNodeRef>` entries. No flow element is left unassigned. An unassigned element makes the lane structure meaningless for that element.

**SC-BPMN-L-03: Lane assignments match the described responsibilities**
Each flow node is assigned to the lane corresponding to the role or department responsible for it according to the task description. Placing a task in the wrong actor's lane is a semantic error — it misrepresents accountability.

---

## UML — Class Diagram

### Structural Correctness

**SC-UML-CD-01: Valid document frame**
The diagram is enclosed between `@startuml` and `@enduml`. Only class diagram syntax is used inside the block. Mixing activity, sequence, or state diagram syntax into a class diagram causes rendering failures.

**SC-UML-CD-02: Classifier keywords are correct**
Concrete, instantiable types use `class`. Types that cannot be directly instantiated and may define abstract methods use `abstract class`. Pure behavioral contracts with no implementation use `interface`. Fixed sets of named constants use `enum`. Using the wrong keyword misrepresents the type's role in the design.

**SC-UML-CD-03: All members declare visibility and types**
Every attribute is prefixed with a visibility modifier (`+` public, `-` private, `#` protected, `~` package) and declares its type with `: Type`. Every method is prefixed with a visibility modifier, lists its parameter types, and declares its return type. Members without visibility or types are incomplete and cannot be assessed for correctness.

**SC-UML-CD-04: Abstract methods are annotated with {abstract}**
Methods that have no implementation and must be overridden by subclasses are marked `{abstract}`. These may only appear inside `abstract class` or `interface` classifiers. A concrete `class` with `{abstract}` methods is contradictory.

**SC-UML-CD-05: Relationship arrows point in the correct direction**
Inheritance (`--|>`): the arrow points from the subclass (more specific) to the superclass (more general). Realization (`..|>`): the arrow points from the implementing class to the interface it implements. Directed association (`-->`): the arrow points from the class that holds the reference to the class being referenced. Aggregation (`o--`) and composition (`*--`): the hollow or filled diamond is placed on the side of the whole, not the part. Reversing any of these arrows inverts the modeled relationship.

**SC-UML-CD-06: Multiplicities are present on associations**
Every association, aggregation, and composition carries multiplicity annotations on both ends (e.g. `"1"`, `"0..1"`, `"0..*"`, `"1..*"`). Missing multiplicities leave the cardinality of the relationship undefined, which is one of the most informative aspects of a class diagram.

**SC-UML-CD-07: Interface implementation uses realization, not inheritance**
A class that fulfills the contract of an interface uses the dashed realization arrow `..|>`. The solid inheritance arrow `--|>` is reserved for class-to-class or interface-to-interface generalization. Using `--|>` for an interface implementation is semantically wrong because it implies inheritance of state, not just behavioral contract.

### Semantic Correctness

**SE-UML-CD-01: The class hierarchy matches the described domain**
Every generalization ("is-a"), specialization, and interface realization described in the task is present. Inheritance is only used for genuine "is-a" relationships, not for "has-a" or "uses" relationships. An inheritance relationship where the subtype is not truly a more specific version of the supertype is a semantic error.

**SE-UML-CD-02: Composition and aggregation reflect the correct lifecycle dependency**
Composition (`*--`) is used when the part cannot exist independently of the whole and is destroyed when the whole is destroyed (e.g. an order line without an order). Aggregation (`o--`) is used when the part has an independent lifecycle and can exist without the whole (e.g. an employee without a department). The two are not interchangeable. Using composition where aggregation is correct (or vice versa) misrepresents the domain.

**SE-UML-CD-03: Permanent references are associations, not dependencies**
When class A permanently holds a reference to class B as an attribute, this is a structural association modeled with `-->`. A dependency (`..>`) models only a temporary or implicit usage (e.g. B appears as a local variable or parameter in a method of A). Using a dependency where a structural association is meant understates the coupling between the classes.

**SE-UML-CD-04: All described attributes and operations are present**
Every attribute and method explicitly mentioned in the task description appears in the correct class with the correct name, type, and visibility. No required member is missing or placed in the wrong class.

**SE-UML-CD-05: Multiplicities match the described cardinalities**
The multiplicity on each end of every association exactly reflects the constraint described in the task. For example, "a customer may have zero or more accounts" requires `"0..*"` on the Account end, not `"1"` or `"*"` without the lower bound.

### Modeling Quality

**MQ-UML-CD-01: Class names are singular nouns**
Classes represent a type, not a collection. Names are singular nouns (e.g. `Customer`, `Order`, `Product`), not plural (e.g. `Customers`, `Orders`).

**MQ-UML-CD-02: Method names are verb phrases**
Operations describe actions. Names are verb phrases (e.g. `calculateTotal()`, `sendNotification()`, `getBalance()`), not noun phrases (`totalCalculation`, `notification`).

**MQ-UML-CD-03: The diagram contains only what the task requires**
No classes, attributes, methods, or relationships are added that cannot be derived from the task description. Invented model elements add noise and may be penalized as incorrect additions.

---

## UML — Component Diagram

### Structural Correctness

**SC-UML-KD-01: System building blocks are declared as components**
Each independent deployable unit is declared as a `component` (using the `component` keyword or the `[Name]` shorthand). Packages may group components logically but are not substitutes for component declarations.

**SC-UML-KD-02: Interface notation is correct**
A provided interface — one that a component offers to others — is connected with a solid line (`component - interface`, the lollipop notation). A required interface — one that a component needs from elsewhere — uses the socket notation (`component --( interface`). Direct dependencies between components that do not go through named interfaces use `-->`. Mixing up provided and required notation misrepresents which component offers and which component depends.

### Semantic Correctness

**SE-UML-KD-01: All described system components are present**
Every subsystem, service, module, or deployable artifact mentioned in the task description appears as a component in the diagram. Missing components mean parts of the described architecture are unmodeled.

**SE-UML-KD-02: Dependency direction matches the described communication**
If component A calls or uses component B, the dependency arrow or required interface points from A toward B. Reversing the direction misrepresents which component depends on which.

**SE-UML-KD-03: Named interfaces are used when the task specifies contracts**
When the task describes components communicating through a named interface or API contract, that interface is modeled explicitly as a named interface element rather than a plain dependency arrow. The interface name must match the contract name used in the description.

---

## UML — Use Case Diagram

### Structural Correctness

**SC-UML-UC-01: System boundary encloses all system use cases**
All use cases that are part of the system under design are placed inside a `rectangle` (system boundary). Actors are placed outside. Use cases outside the system boundary or actors inside it misrepresent what belongs to the system.

**SC-UML-UC-02: Actors are external roles**
Actors represent roles or entities that interact with the system from outside its boundary — human users, external systems, time-based triggers. Internal components, databases, or subsystems are not actors.

**SC-UML-UC-03: Relationship arrows are correctly directed**
`<<include>>`: the arrow points from the base use case (the one that triggers the behavior) to the included use case (the behavior that is always invoked). `<<extend>>`: the arrow points from the extending use case (the optional or conditional addition) to the base use case (the one being extended). Reversing either arrow inverts the semantic direction of the relationship.

### Semantic Correctness

**SE-UML-UC-01: All described actors are present**
Every external party, user role, or external system described in the task is represented as an actor. Each actor's associations correctly reflect which use cases they initiate or participate in.

**SE-UML-UC-02: All described functional goals are present as use cases**
Every distinct functional capability the system must provide, as stated in the task, is a use case. Use cases are named from the actor's perspective using verb phrases (e.g. "Place order", "Generate report"). Missing use cases mean missing functional requirements.

**SE-UML-UC-03: include is used for mandatory, always-executed sub-behavior**
`<<include>>` models a piece of behavior that is always and unconditionally executed as part of the base use case. It is not used for optional or conditional behavior. A common mistake is using `<<include>>` where `<<extend>>` is meant because the sub-behavior seems "related" rather than mandatory.

**SE-UML-UC-04: extend is used for optional or condition-dependent behavior**
`<<extend>>` models behavior that is added to the base use case only under specific conditions. The condition under which the extension applies must be either stated in the task description or clearly inferable from it. Using `<<extend>>` for behavior that always occurs (which should be `<<include>>`) is a semantic error.

**SE-UML-UC-05: Generalization correctly models specialization**
Actor generalization (`<|--`) is only used when one actor is a specialized version of another and inherits all of its associations. Use case generalization is used when one use case is a concrete specialization of a more abstract one. Generalization is not used as a synonym for `<<include>>` or `<<extend>>`.

---

## UML — Activity Diagram

### Structural Correctness

**SC-UML-AD-01: Every diagram has exactly one start node and at least one end node**
The diagram begins with `start`. Every execution path ends with `stop` (ends the current flow) or `end` (ends all flows). No path is left without a termination. An activity diagram with an open path is structurally incomplete.

**SC-UML-AD-02: Action nodes use correct syntax**
Every action is written as `:Action name;` — the colon opens the node and the semicolon closes it. Missing either delimiter prevents the parser from recognizing the action and causes a rendering error.

**SC-UML-AD-03: Conditional branches are syntactically closed**
Every `if (condition) then (label)` block is completed with a matching `endif`. An unclosed `if` is a syntax error that makes the diagram unparseable.

**SC-UML-AD-04: Fork/join blocks are complete and synchronized**
Every `fork` block is completed with `end fork`. All branches between `fork` and `end fork` are parallel and all must complete before the flow at `end fork` continues. A missing `end fork` breaks the synchronization and leaves parallel branches permanently diverged.

**SC-UML-AD-05: Swimlane assignments are unambiguous**
When swimlanes are used, every action node falls inside a declared `|Lane name|` section. There are no actions placed between two swimlane declarations in a way that makes their lane assignment ambiguous.

### Semantic Correctness

**SE-UML-AD-01: All described steps appear in the correct sequence**
Every action mentioned in the task description appears as an action node, and the control flow between them reflects the described order. Steps are not reordered, merged, or omitted.

**SE-UML-AD-02: Every decision point is modeled with a labeled `if` node**
Every branching point described in the task appears as an `if (condition)` decision node. The branch labels match the conditions described. A decision without labels, or a decision with the wrong number of branches, is a semantic error.

**SE-UML-AD-03: Parallel execution uses fork/join**
When the task states that two or more activities happen simultaneously or can happen in any order without depending on each other, they are placed inside a `fork`/`end fork` block. Modeling concurrent activities sequentially misrepresents the described behavior.

**SE-UML-AD-04: Swimlane assignments reflect described responsibility**
Each action is placed in the swimlane of the actor, role, or system that performs it according to the task description. Assigning an action to the wrong lane misrepresents who is responsible.

---

## UML — Sequence Diagram

### Structural Correctness

**SC-UML-SD-01: All participants are declared before use**
Every actor, system component, or object that sends or receives a message is declared as a lifeline (`actor`, `participant`, `database`, `boundary`, `control`, `entity`) at the top of the diagram before it appears in a message. An undeclared participant cannot be rendered.

**SC-UML-SD-02: Activation bars are paired**
Every `activate X` statement is matched by a corresponding `deactivate X` at the point where the participant stops processing. Unpaired activation bars either leave a participant permanently active or produce a rendering inconsistency.

**SC-UML-SD-03: Combined fragments are closed**
Every `alt`, `opt`, `loop`, or `par` block ends with `end`. Nested fragments must be closed in innermost-first order. An unclosed fragment is a syntax error.

**SC-UML-SD-04: Arrow types reflect call semantics**
A synchronous call — where the sender blocks and waits for a reply — uses `->`. The corresponding reply uses `-->`. An asynchronous call — where the sender does not wait — uses `->>`. Using synchronous arrows for asynchronous calls or omitting reply arrows for synchronous calls misrepresents how the participants interact.

### Semantic Correctness

**SE-UML-SD-01: All described message exchanges are present in the correct order**
Every interaction described in the task — every request, response, notification, or data transfer — appears in the diagram. Messages are ordered top-to-bottom in the same sequence as described. A missing message means a described interaction is absent; a wrong order means the described temporal sequence is not respected.

**SE-UML-SD-02: Each message is sent from and received by the correct participants**
The source and target of every arrow match the described sender and receiver. Reversing a message direction reverses who initiates and who responds.

**SE-UML-SD-03: Conditional and optional interactions use the correct fragment type**
When the task describes alternative scenarios (if/else), they are enclosed in `alt` with labeled guards for each branch. Optional interactions (may or may not happen) use `opt`. Leaving conditional behavior outside a combined fragment makes the diagram appear unconditional when it is not.

**SE-UML-SD-04: Return messages are present for synchronous calls**
When a synchronous call produces a return value or acknowledgment mentioned in the task, the corresponding reply message with `-->` is present. Omitting a return message implies the call either produces no result or is asynchronous, which may contradict the description.

---

## UML — State Diagram

### Structural Correctness

**SC-UML-STD-01: Initial pseudo-state is present**
Every state diagram has exactly one `[*] --> FirstState` transition as the entry point. Without it, it is undefined which state the system starts in.

**SC-UML-STD-02: A final state is reachable**
At least one state has an outgoing transition to `[*]` (the final pseudo-state), indicating that the lifecycle of the modeled object can end. A state diagram with no reachable final state models a system that never terminates, which is only correct if the task explicitly requires it.

**SC-UML-STD-03: Composite states contain their own initial pseudo-state**
Every `state X { ... }` composite state contains `[*] --> SubStateName` as the entry point into its sub-states. Without this, it is undefined which sub-state is entered when the composite state is reached.

**SC-UML-STD-04: Transition labels follow the correct syntax**
Transitions use the syntax `StateA --> StateB : trigger [guard] / action`. Each part (trigger, guard, action) is optional, but when present must be syntactically correct. Guards are enclosed in square brackets; actions follow a forward slash. A guard without brackets or an action without a slash will be misinterpreted.

### Semantic Correctness

**SE-UML-STD-01: All described states are present**
Every distinct condition or mode of the modeled system mentioned in the task appears as a state node. Merging distinct states into one, or omitting states entirely, produces a model that cannot represent all described behaviors.

**SE-UML-STD-02: All described state transitions are present**
Every event or condition that causes the system to move from one state to another, as described in the task, is represented as a labeled transition. A missing transition means a described state change cannot occur in the model.

**SE-UML-STD-03: Guards are present when transitions are conditional**
When the task specifies that a transition only fires under a certain condition (e.g. "only if the counter is less than 3"), that condition appears as a guard `[condition]` on the transition. A transition without a guard where one is required fires unconditionally, changing the modeled behavior.

**SE-UML-STD-04: Entry, exit, and do-activities are placed on the correct state**
`entry /`, `exit /`, and `do /` actions belong to the state in which they occur and are declared as part of that state's definition (e.g. `StateName : entry / action`). They are not placed on transition labels. Misplacing them changes when the action executes.

**SE-UML-STD-05: Composite states are used for hierarchical behavior**
When the task describes a state that itself contains sub-states or internal behavior (e.g. an "Unlocked" state with sub-menus for different operations), a composite state `state Unlocked { ... }` is used. Flattening composite states to the top level loses the hierarchical structure and may duplicate transitions that apply to all sub-states.

---

## Petri Nets (PNML)

### Structural Correctness

**SC-PNML-01: Valid document frame**
The document uses `<?xml version="1.0" encoding="UTF-8"?>`, a `<pnml>` root element with `xmlns="http://www.pnml.org/version-2009/grammar/pnml"`, a `<net>` element with a `type` attribute set to a valid net type URI, and a `<page>` element that contains all net elements. Without the correct namespace and structure the document is not valid PNML and cannot be loaded by any Petri net tool.

**SC-PNML-02: All elements have unique IDs**
Every `<place>`, `<transition>`, and `<arc>` has an `id` attribute that is unique within the document. Arcs reference places and transitions by their `id`; duplicate or missing IDs cause broken references.

**SC-PNML-03: The net is bipartite — arcs only connect places to transitions or transitions to places**
Every `<arc>` connects either a place (as `source`) to a transition (as `target`), or a transition (as `source`) to a place (as `target`). An arc between two places or two transitions violates the bipartite property that defines a Petri net. Such an arc is not a modeling choice but a structural error.

**SC-PNML-04: All arc source and target references are valid**
The `source` and `target` attributes of every `<arc>` point to an `id` that exists in the same document as either a `<place>` or a `<transition>`. A reference to a non-existing id is a broken arc that makes the net invalid.

**SC-PNML-05: Every place declares an initial marking**
Every `<place>` contains an `<initialMarking><text>n</text></initialMarking>` child element where n is a non-negative integer. The initial marking defines the starting state of the system. A missing initial marking leaves the place's starting token count undefined; in most tools this defaults to 0, but making it explicit is required for a correct and unambiguous model.

**SC-PNML-06: Arc weights are declared explicitly when greater than 1**
When a transition must consume or produce more than one token on a particular arc, that arc carries an `<inscription><text>n</text></inscription>` element stating the weight. In a model where some arcs have non-default weights, all arcs should have explicit inscriptions to avoid ambiguity about which weight is intended.

**SC-PNML-07: Place capacities are declared when the modeled system has resource limits**
When the modeled scenario imposes an upper bound on how many tokens a place can hold (e.g. a bounded buffer), the place carries a `<capacity><text>k</text></capacity>` element. Without this declaration, a place is unbounded by default, and any resource constraint modeled by the capacity is lost.

### Semantic Correctness

**SE-PNML-01: The initial marking correctly reflects the described starting state**
The `initialMarking` of each place accurately represents the initial conditions of the modeled scenario. Places whose associated condition is true at the start receive 1 token (in B/E nets) or the appropriate number of tokens (in S/T nets). Places whose condition is initially false receive 0 tokens. An incorrect initial marking produces a net that starts in the wrong state.

**SE-PNML-02: At least one transition is enabled under the initial marking**
Under the initial marking, at least one transition must be enabled — meaning its preset places all hold enough tokens. A net where no transition can ever fire is in a deadlock from the start, which is a modeling error unless the task explicitly describes a system that is immediately blocked.

**SE-PNML-03: Concurrency is modeled with fork and join**
When the task describes activities that can happen simultaneously or independently, the fork/join pattern is used: one transition with multiple output arcs (fork) enables independent downstream transitions, and one transition with multiple input arcs (join) waits for all parallel branches to complete before the flow continues. Omitting the join means the parallel branches never synchronize and the process cannot reach any common successor state.

**SE-PNML-04: Conflict models non-deterministic choice between alternatives**
When the task describes a point where one of several alternatives is chosen, a single input place has multiple outgoing arcs to different transitions. Only one of them can fire (consuming the shared token), making the others no longer enabled. This correctly models non-deterministic choice. Missing this shared place — for example, giving each transition its own independent input — removes the conflict and makes the alternatives independent, which is semantically wrong.

**SE-PNML-05: Cycles correctly model repeated behavior**
When the task describes a process that repeats — a loop — the net contains a directed cycle: a transition eventually produces a token in a place that is in its own preset (directly or via intermediate places), re-enabling it or an earlier transition. The cycle covers all the steps described as repeating. An incomplete cycle, or no cycle where one is required, produces a model that fires each step at most once.

**SE-PNML-06: Arc weights match the described resource quantities**
When the task specifies that a transition consumes or produces a specific number of tokens (e.g. "each production cycle deposits 2 units into the buffer"), the corresponding arc inscription equals that number. Using a default weight of 1 when the description calls for a different quantity is a semantic error that changes the firing behavior of the net.

**SE-PNML-07: Place capacities match the described resource bounds**
When the task describes an upper limit on a resource (e.g. "the buffer can hold at most 6 items"), the corresponding place has a `<capacity>` matching that bound. A missing or incorrect capacity allows the place to accumulate more tokens than the scenario permits, producing physically impossible states.

**SE-PNML-08: The correct net type is used**
A Condition/Event (B/E) net is appropriate when the scenario only requires binary conditions (true/false) and each transition consumes and produces exactly one token. A Place/Transition (S/T) net is required when quantities, counts, or multi-token transfers are described. Using a B/E net where an S/T net is needed results in a model that cannot express the required resource quantities.

**SE-PNML-09: All described conditions, resources, and events are represented**
Every state, condition, resource, or buffer described in the scenario appears as a named place. Every event, activity, or state-changing action appears as a named transition. Nothing required by the task description is omitted. Missing places or transitions mean parts of the modeled behavior are absent.

### Modeling Quality

**MQ-PNML-01: Place names describe conditions or states**
A place represents a condition that is true (place holds a token) or false (place is empty). Place names should be noun phrases or predicate descriptions of that condition (e.g. "Order received", "Resource available", "Buffer full"). Verb-phrase names are inappropriate for places.

**MQ-PNML-02: Transition names describe events or actions**
A transition represents something that happens — an event or an activity. Transition names should be verb phrases (e.g. "Accept order", "Start production", "Release lock"). Noun-phrase names (e.g. "Order acceptance") are less clear and suggest a state rather than an event.

**MQ-PNML-03: No isolated places or transitions**
Every place is connected to at least one arc, and every transition is connected to at least one arc. An isolated place can never gain or lose tokens and has no effect on the net's behavior. An isolated transition can never fire. Both indicate a modeling error — either an element was added by mistake, or a required arc connecting it to the rest of the net was forgotten.

**MQ-PNML-04: The net subtype is respected when specified**
When the task asks for a specific Petri net subtype, its structural constraints must hold:
- **B/E net**: every arc weight is 1 and every place capacity is 1; places hold at most one token at any time.
- **S/T net**: arc weights and/or capacities greater than 1 are used where the scenario requires them; places may hold multiple tokens.
- **Marked Graph**: every place has exactly one incoming arc and exactly one outgoing arc. Conflicts are structurally impossible; only concurrency can be modeled.
- **State Machine**: every transition has exactly one incoming arc and exactly one outgoing arc. Concurrency is structurally impossible; only sequential and conflicting behavior can be modeled.
- **Free Choice Net**: for every place p, all transitions in the postset of p share p as their only input place — choice and concurrency are both possible but never arise from the same place simultaneously.

---

## General Criteria (All Notations)

**GEN-01: The diagram is complete**
The diagram represents every entity, relationship, action, state, or event mentioned in the task description. A submission that correctly models only a subset of the described scenario is incomplete. Completeness is assessed against the task description, not against what might be implied or inferred.

**GEN-02: The diagram does not invent elements**
The diagram contains only elements required by or directly derivable from the task description. Elements not grounded in the description — invented classes, extra transitions, unlisted actors, additional tasks — are not acceptable additions even if they might make the model more realistic.

**GEN-03: The correct notation is used**
The diagram is produced in the notation required by the task: BPMN 2.0 XML syntax, PlantUML syntax for UML, or PNML syntax for Petri nets. A diagram in the wrong notation cannot satisfy the modeling requirements regardless of its content.

**GEN-04: The correct diagram type is used within the notation**
Within a notation, the correct diagram type is used. For example, a BPMN collaboration diagram is not replaced by a process diagram when multiple participants are described; a UML activity diagram is not replaced by a sequence diagram when a process flow is required.

**GEN-05: All elements are meaningfully named**
Every place, transition, task, event, gateway, class, state, actor, and use case carries a name that conveys its meaning without requiring additional context. Anonymous elements (identified only by id) are not acceptable except for purely structural connector nodes where no meaningful label can be given.

**GEN-06: Names match the terminology of the task description**
Element names closely reflect the terminology used in the task description. Arbitrarily different names — while potentially not wrong — make the diagram harder to verify against the task and suggest that the student may not have understood the domain.
