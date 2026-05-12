import re

def extract_bpmn(text: str) -> str | None:
    """
    Extract BPMN XML from text input.
    """

    patterns = [
        # Normal BPMN with namespace prefix
        r"<bpmn:definitions[\s\S]*?</bpmn:definitions>",

        # BPMN without prefix
        r"<definitions[\s\S]*?</definitions>",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return match.group(0).strip()

    return None


def strip_bpmndi(xml: str) -> str:
    """
    Remove the bpmndi diagram interchange section from BPMN XML.
    It contains only visual layout coordinates and is not needed for LLM evaluation.
    """
    return re.sub(r"<bpmndi:BPMNDiagram[\s\S]*?</bpmndi:BPMNDiagram>", "", xml).strip()