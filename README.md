# Faculty Portal Dashboard

A simple Flask-based Faculty Portal Dashboard (demo project) with features:
- List faculty
- Add faculty
- Delete faculty (simple POST action)
- Data stored in faculty_data.json (flat-file for demo)

## Run locally
1. Create virtualenv: `python -m venv venv && source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Open http://127.0.0.1:5000

## Notes
- This is a simple educational demo. For production, use a database, authentication, and secure secret keys.
