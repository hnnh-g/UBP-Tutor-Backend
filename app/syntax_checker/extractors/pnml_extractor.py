import re


def extract_pnml(text: str) -> str | None:
    """
    Extract PNML XML from text input.
    """

    pattern = r"<pnml[\s\S]*?</pnml>"

    match = re.search(pattern, text)

    if match:
        return match.group(0).strip()

    return None