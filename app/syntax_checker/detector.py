def detect_notation(model_text: str) -> str:
    text = model_text.strip().lower()

    if "@startuml" in text and "@enduml" in text:
        return "uml"
    if "<bpmn:definitions" in text or "xml" in text or ("<definitions" in text and "bpmn" in text):
        return "bpmn"

    if text.startswith("<pnml") or "pnml" in text:
        return "pnml"

    return "unknown"