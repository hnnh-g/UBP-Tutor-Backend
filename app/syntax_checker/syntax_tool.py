from app.syntax_checker.detector import detect_notation
from app.syntax_checker.validators.uml.plantuml_validator import validate_uml
from app.syntax_checker.extractors.uml_extractor import extract_plantuml
from app.syntax_checker.extractors.bpmn_extractor import extract_bpmn, strip_bpmndi
from app.syntax_checker.validators.bpmn.bpmn_validator import validate_bpmn
from app.syntax_checker.extractors.pnml_extractor import extract_pnml
from app.syntax_checker.validators.pnml.pnml_validator import validate_pnml


def validate_model_syntax(model_text: str):
    # Every branch also returns the extracted diagram under "diagram", so the
    # caller can ship exactly what was validated. The model sometimes wraps a
    # diagram in a foreign document (e.g. BPMN nested inside <pnml>), and the
    # extractors quietly drop that wrapper - returning the raw response instead
    # would deliver something the validator never checked.
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
                ],
                "diagram": None,
            }

        result = validate_uml(diagram)
        result["diagram"] = diagram
        return result

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
                "diagram": None,
            }

        # DI holds only layout coordinates, so it is stripped for linting - but
        # kept in the returned diagram, because bpmn-js needs it to render.
        result = validate_bpmn(strip_bpmndi(diagram))
        result["diagram"] = diagram
        return result

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
                "diagram": None,
            }

        result = validate_pnml(diagram)
        result["diagram"] = diagram
        return result

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
            "diagram": None,
        }