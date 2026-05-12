from app.syntax_checker.detector import detect_notation
from app.syntax_checker.validators.uml.plantuml_validator import validate_uml
from app.syntax_checker.extractors.uml_extractor import extract_plantuml
from app.syntax_checker.extractors.bpmn_extractor import extract_bpmn
from app.syntax_checker.validators.bpmn.bpmn_validator import validate_bpmn


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
        diagram = extract_bpmn(model_text)
        if diagram is None:
            return {
                "valid": False,
                "notation": "bpmn",
                "issues": [
                    {
                        "severity": "error",
                        "code": "NO_BPMN_XML_FOUND",
                        "message": "No BPMN XML block was found.",
                        "suggestion": "Include BPMN XML between <bpmn:definitions> and </bpmn:definitions>.",
                    }
                ],
            }

        return validate_bpmn(diagram)

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