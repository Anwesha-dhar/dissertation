from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    script_dir = Path(__file__).parent
    python_exe = sys.executable

    # Always install requirements first (prefer local file in this folder)
    local_req = script_dir / "requirements.txt"
    root_req = script_dir.parent / "requirements.txt"

    try:
        print("Upgrading pip/setuptools/wheel ...")
        subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"], check=True)

        if local_req.exists():
            print(f"Installing dependencies from {local_req} ...")
            subprocess.run([python_exe, "-m", "pip", "install", "-r", str(local_req)], check=True)
        elif root_req.exists():
            print(f"Installing dependencies from {root_req} ...")
            subprocess.run([python_exe, "-m", "pip", "install", "-r", str(root_req)], check=True)
        else:
            print("No requirements.txt found. Skipping dependency installation.")
    except subprocess.CalledProcessError as exc:
        print(f"Dependency installation failed (exit code {exc.returncode}).")
        return exc.returncode

    # Collect Python scripts in this directory, excluding this runner and obvious non-targets
    candidates = []
    for p in sorted(script_dir.glob("*.py")):
        name_lower = p.name.lower()
        if name_lower in {"runme.py"}:
            continue
        candidates.append(p)

    if not candidates:
        print("No Python scripts found to run in this folder.")
        return 1

    print(f"Running {len(candidates)} scripts using {python_exe} ...\n")
    for script_path in candidates:
        print(f"=== Running {script_path.name} ===")
        result = subprocess.run([python_exe, str(script_path)])
        if result.returncode != 0:
            print(f"Script failed: {script_path.name} (exit code {result.returncode})")
            return result.returncode
        print("")

    print("All scripts completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


