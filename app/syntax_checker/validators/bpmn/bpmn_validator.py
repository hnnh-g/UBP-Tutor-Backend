import subprocess
import tempfile
from pathlib import Path
from app.syntax_checker.validators.bpmn.error_mapping import normalize_bpmnlint_output


BPMNLINT_CONFIG = Path(__file__).resolve().parents[3] / ".bpmnlintrc"


def validate_bpmn(model_text: str) -> dict:

    # create temporary file to extract text from
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".bpmn",
        encoding="utf-8",
        delete=True,
    ) as temp_file:
        temp_file.write(model_text)
        temp_file.flush()

        # run validation via bpmnlint tool and apply disabled rules
        result = subprocess.run(
            [
                "npx",
                "bpmnlint",
                "--config",
                str(BPMNLINT_CONFIG),
                temp_file.name,
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )

    # return validation result
    raw_output = result.stdout or result.stderr
    issues = normalize_bpmnlint_output(raw_output)

    return {
        "valid": result.returncode == 0,
        "notation": "bpmn",
        "issues": issues,
        "raw_output": raw_output,
    }
