def normalize_bpmnlint_output(raw_output: str) -> list[dict]:
    """
    Converts bpmnlint CLI output into structured issue dictionaries.
    """

    issues = []

    for line in raw_output.splitlines():
        line = line.strip()

        if not line:
            continue

        # Skip file path line
        if line.endswith(".bpmn"):
            continue

        # Skip summary line, e.g. ✖ 4 problems
        if line.startswith("✖"):
            continue

        parts = line.split()

        # Expected:
        # ElementID  severity  message words...  rule-name
        if len(parts) < 4:
            continue

        element_id = parts[0]
        severity = parts[1]
        rule = parts[-1]
        message = " ".join(parts[2:-1])

        issues.append({
            "severity": severity,
            "code": rule.upper().replace("-", "_"),
            "element_id": element_id,
            "message": message,
            "rule": rule,
        })

    return issues