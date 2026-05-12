from lxml import etree

def local_name(element) -> str:
    """
    Extract XML tag name without namespace.
    """

    return etree.QName(element).localname

def validate_pnml(model_text: str) -> dict:
    issues = []

    try:
        # checks XML validity (e.g., closing tags)
        root = etree.fromstring(model_text.encode("utf-8"))
    except etree.XMLSyntaxError as error:
        return {
            "valid": False,
            "notation": "pnml",
            "issues": [
                {
                    "severity": "error",
                    "code": "INVALID_XML",
                    "message": "The PNML model is not well-formed XML.",
                    "details": str(error),
                    "suggestion": "Check whether all XML tags are correctly opened and closed.",
                }
            ],
        }

    # checks if <pnml> tag is at the beginning of the text
    if local_name(root) != "pnml":
        issues.append({
            "severity": "error",
            "code": "MISSING_PNML_ROOT",
            "message": "The root element must be <pnml>.",
            "suggestion": "Wrap the Petri net model inside a <pnml> root element.",
        })

    # checks if the second tag is the <net> tag
    all_elements = list(root.iter())
    nets = [
    element
    for element in all_elements
    if local_name(element) == "net"
]
    if not nets:
        issues.append({
            "severity": "error",
            "code": "MISSING_NET",
            "message": "No <net> element was found.",
            "suggestion": "Add a <net> element inside <pnml>.",
        })

    # checks if <page> tag exists because pnml organizes elements inside pages
    pages = [
    element
    for element in all_elements
    if local_name(element) == "page"
]
    if not pages:
        issues.append({
            "severity": "error",
            "code": "MISSING_PAGE",
            "message": "No <page> element was found.",
            "suggestion": "Add a <page> element inside <net>.",
        })

    places = [
    element
    for element in all_elements
    if local_name(element) == "place"
]
    transitions = [
    element
    for element in all_elements
    if local_name(element) == "transition"
]
    arcs = [
    element
    for element in all_elements
    if local_name(element) == "arc"
]

    place_ids = {place.get("id") for place in places if place.get("id")}
    transition_ids = {transition.get("id") for transition in transitions if transition.get("id")}
    node_ids = place_ids | transition_ids

    for place in places:
        # check if places have ids otherwise invalid
        if not place.get("id"):
            issues.append({
                "severity": "error",
                "code": "PLACE_MISSING_ID",
                "message": "A place is missing an id attribute.",
                "suggestion": "Every <place> must have a unique id.",
            })

    for transition in transitions:
        # check if transitions have ids otherwise invalid
        if not transition.get("id"):
            issues.append({
                "severity": "error",
                "code": "TRANSITION_MISSING_ID",
                "message": "A transition is missing an id attribute.",
                "suggestion": "Every <transition> must have a unique id.",
            })

    for arc in arcs:
        arc_id = arc.get("id", "unknown")
        source = arc.get("source")
        target = arc.get("target")

        # check if arc has source and target otherwise invalid
        if not source:
            issues.append({
                "severity": "error",
                "code": "ARC_MISSING_SOURCE",
                "message": f"Arc '{arc_id}' is missing a source.",
                "suggestion": "Add a source attribute that references a place or transition.",
            })

        elif source not in node_ids:
            issues.append({
                "severity": "error",
                "code": "ARC_INVALID_SOURCE",
                "message": f"Arc '{arc_id}' references unknown source '{source}'.",
                "suggestion": "Use the id of an existing place or transition as source.",
            })

        if not target:
            issues.append({
                "severity": "error",
                "code": "ARC_MISSING_TARGET",
                "message": f"Arc '{arc_id}' is missing a target.",
                "suggestion": "Add a target attribute that references a place or transition.",
            })

        elif target not in node_ids:
            issues.append({
                "severity": "error",
                "code": "ARC_INVALID_TARGET",
                "message": f"Arc '{arc_id}' references unknown target '{target}'.",
                "suggestion": "Use the id of an existing place or transition as target.",
            })

        # check if only place and transitions are connected not place and place or transition with transition
        if source in place_ids and target in place_ids:
            issues.append({
                "severity": "error",
                "code": "ARC_PLACE_TO_PLACE",
                "message": f"Arc '{arc_id}' connects a place directly to another place.",
                "suggestion": "Petri-net arcs must connect place → transition or transition → place.",
            })

        if source in transition_ids and target in transition_ids:
            issues.append({
                "severity": "error",
                "code": "ARC_TRANSITION_TO_TRANSITION",
                "message": f"Arc '{arc_id}' connects a transition directly to another transition.",
                "suggestion": "Petri-net arcs must connect place → transition or transition → place.",
            })

        # check for duplicate IDs
        all_ids_list = []
        
        for element in places + transitions + arcs:
            element_id = element.get("id")
            if element_id:
                all_ids_list.append(element_id)

        seen_ids = set()
        duplicate_ids = set()

        for element_id in all_ids_list:
            if element_id in seen_ids:
                duplicate_ids.add(element_id)
            else:
                seen_ids.add(element_id)

        for duplicate_id in duplicate_ids:
            issues.append({
                "severity": "error",
                "code": "DUPLICATE_ID",
                "message": f"The id '{duplicate_id}' is used more than once.",
                "suggestion": "Use unique ids for all places, transitions, and arcs.",
            })

        # check missing arc IDs
        arc_id = arc.get("id")

        if not arc_id:
            issues.append({
                "severity": "error",
                "code": "ARC_MISSING_ID",
                "message": "An arc is missing an id attribute.",
                "suggestion": "Add a unique id to every <arc>, for example id='A1'.",
            })
            arc_id = "unknown"

        # check isolated nodes (places or transitions) and produce a warning message
        connected_node_ids = set()

        for arc in arcs:
            source = arc.get("source")
            target = arc.get("target")

            if source:
                connected_node_ids.add(source)

            if target:
                connected_node_ids.add(target)

        for place_id in place_ids:
            if place_id not in connected_node_ids:
                issues.append({
                    "severity": "warning",
                    "code": "ISOLATED_PLACE",
                    "message": f"Place '{place_id}' is not connected to any arc.",
                    "suggestion": "Connect the place to a transition if it belongs to the Petri net behavior.",
                })

        for transition_id in transition_ids:
            if transition_id not in connected_node_ids:
                issues.append({
                    "severity": "warning",
                    "code": "ISOLATED_TRANSITION",
                    "message": f"Transition '{transition_id}' is not connected to any arc.",
                    "suggestion": "Connect the transition to at least one place.",
                }) 

    return {
        "valid": not any(issue["severity"] == "error" for issue in issues),
        "notation": "pnml",
        "issues": issues,
    }