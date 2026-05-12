from app.syntax_checker.detector import detect_notation
from app.syntax_checker.validators.uml.plantuml_validator import validate_uml
from app.syntax_checker.extractors.uml_extractor import extract_plantuml


def validate_model_syntax(model_text: str):

    notation = detect_notation(model_text)

    if notation == "uml":
        diagram = extract_plantuml(model_text)
        if diagram is None:
            return {
                "valid": False,
                "notation": "uml",
                "issues": [
                    {
                        "severity": "error",
                        "code": "NO_UML_BLOCK",
                        "message": (
                            "No PlantUML diagram block found."
                        ),
                        "suggestion": (
                            "Include a diagram between "
                            "@startuml and @enduml."
                        )
                    }
                ]
            }

        return validate_uml(diagram)

    elif notation == "bpmn":
        return validate_bpmn(model_text)

    elif notation == "pnml":
        return validate_pnml(model_text)

    else:
        return {
            "valid": False,
            "notation": "unknown",
            "issues": [
                {
                    "severity": "error",
                    "code": "UNKNOWN_FORMAT",
                    "message": "Could not detect notation"
                }
            ]
        }