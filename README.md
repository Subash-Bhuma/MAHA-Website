# MAHA

Government-oriented digital workflow for discovering, evaluating, piloting, and preparing startup innovation for the appropriate procurement pathway.

## Repository Structure
- `/docs` – product, architecture, workflows, security, design system, and data model docs
- `/portal` – public-facing government-style portal prototype
- `/backend` – FastAPI vertical slice for challenge lifecycle + audit timeline

## Run Public Portal
Open `/portal/index.html` in a browser.

## Run Backend
```bash
cd /home/runner/work/MAHA-Website/MAHA-Website/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run Tests
```bash
cd /home/runner/work/MAHA-Website/MAHA-Website/backend
source .venv/bin/activate
pytest -q
```
