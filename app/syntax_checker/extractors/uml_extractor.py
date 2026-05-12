import re

def extract_plantuml(text: str) -> str | None:
    """
    Extract PlantUML block from text.
    """

    pattern = r"@startuml.*?@enduml"

    match = re.search(
        pattern,
        text,
        re.DOTALL
    )

    if match:
        return match.group(0)

    return None
