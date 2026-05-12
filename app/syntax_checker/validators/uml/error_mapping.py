def normalize_plantuml_error(raw_error: str) -> dict:

    raw_error_lower = raw_error.lower()

    if "no diagram found" in raw_error_lower:
        return {
            "severity": "error",
            "code": "MISSING_DIAGRAM_BLOCK",
            "message": "No valid UML diagram block was found.",
            "suggestion": (
                "Ensure the diagram contains "
                "@startuml and @enduml."
            ),
        }

    if "syntax error" in raw_error_lower:
        return {
            "severity": "error",
            "code": "UML_SYNTAX_ERROR",
            "message": "The UML diagram contains invalid syntax.",
            "suggestion": (
                "Check relationships, declarations, "
                "and diagram structure."
            ),
        }

    return {
        "severity": "error",
        "code": "UNKNOWN_PLANTUML_ERROR",
        "message": raw_error.strip(),
        "suggestion": "Review the UML syntax.",
    }