.PHONY: test-backend run-backend install-backend coverage

install-backend:
	cd backend && pip install -r requirements.txt

run-backend:
	cd backend && python app.py

test-backend:
	cd backend && python -m pytest -v

coverage:
	cd backend && python -m pytest --cov=app --cov-report=term-missing -v