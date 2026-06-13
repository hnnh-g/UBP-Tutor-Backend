from app.syntax_checker.detector import detect_notation
from app.syntax_checker.validators.uml.plantuml_validator import validate_uml
from app.syntax_checker.extractors.uml_extractor import extract_plantuml
from app.syntax_checker.extractors.bpmn_extractor import extract_bpmn
from app.syntax_checker.validators.bpmn.bpmn_validator import validate_bpmn
from app.syntax_checker.extractors.pnml_extractor import extract_pnml
from app.syntax_checker.validators.pnml.pnml_validator import validate_pnml


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
        diagram = extract_pnml(model_text)

        if diagram is None:
            return {
                "valid": False,
                "notation": "pnml",
                "issues": [
                    {
                        "severity": "error",
                        "code": "NO_PNML_XML_FOUND",
                        "message": "No PNML XML block was found.",
                        "suggestion": "Include a PNML model between <pnml> and </pnml>.",
                    }
                ],
            }

        return validate_pnml(diagram)

    else:
        return {
            "valid": False,
            "notation": "unknown",
            "issues": [
                {
                    "severity": "error",
                    "code": "UNKNOWN_NOTATION",
                    "message": "Could not detect diagram notation (not UML, BPMN, or PNML).",
                    "suggestion": "Ensure the diagram starts with @startuml, <bpmn:definitions>, or <pnml>.",
                }
            ],
        }