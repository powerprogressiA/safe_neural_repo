# Safe Neural Repo

A modular and safety-focused neural project structure.

## 📂 Structure


## ⚙️ Setup (Ubuntu 24.04)
```bash
git clone https://github.com/powerprogressiA/safe_neural_repo.git
cd safe_neural_repo
python3 -m venv venv && source venv/bin/activate
pip install poetry
poetry install
pytest -v

poetry run pytest

poetry run black .
poetry run flake8 .
poetry run isort .
poetry run mypy .


---

## 🧠 6. Add example mock module

```bash
cat <<'EOF' > hal/mock_interfaces.py
import random
import time

def mock_eeg_sensor():
    """Simulate EEG data reading."""
    time.sleep(0.1)
    return {"timestamp": time.time(), "channels": [random.random() for _ in range(3)]}

def mock_camera_frame():
    """Simulate camera frame capture."""
    time.sleep(0.05)
    return {"timestamp": time.time(), "pixels": [random.randint(0, 255) for _ in range(10)]}
