import subprocess
import tempfile
from pathlib import Path
from app.syntax_checker.validators.uml.error_mapping import normalize_plantuml_error

PLANTUML_JAR = (
    Path(__file__).resolve().parents[3]
    / "tools"
    / "plantuml.jar"
)

def validate_uml(model_text: str):
    with tempfile.TemporaryDirectory() as tmp:

        # create temporary file that contains the diagram
        file_path = Path(tmp) / "diagram.puml"
        file_path.write_text(model_text)

        # execute terminal command from python code
        result = subprocess.run(
            [
                "java",
                "-jar",
                str(PLANTUML_JAR),
                "--check-syntax",
                str(file_path),
            ],
            capture_output=True,
            text=True
        )

        if not PLANTUML_JAR.exists():
            return {
                "valid": False,
                "notation": "uml",
                "issues": [
                    {
                        "severity": "error",
                        "code": "PLANTUML_JAR_NOT_FOUND",
                        "message": f"PlantUML jar not found at: {PLANTUML_JAR}",
                    }
                ],
            }

        if result.returncode == 0:
            return {
                "valid": True,
                "notation": "uml",
                "issues": []
            }
        return {
            "valid": False,
            "notation": "uml",
            "issues": [
                normalize_plantuml_error(
                    result.stderr or result.stdout
                )
            ]
        }
    