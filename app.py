from flask import Flask, render_template, request, redirect, url_for, flash
from dataclasses import dataclass, asdict
import json, os

app = Flask(__name__)
app.secret_key = 'dev-secret-key'  # replace before production
DATA_FILE = 'faculty_data.json'

@dataclass
class Faculty:
    id: int
    name: str
    department: str
    email: str
    role: str  # e.g., 'Admin' or 'Faculty'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return [Faculty(**d) for d in data]

def save_data(faculties):
    with open(DATA_FILE, 'w') as f:
        json.dump([asdict(f) for f in faculties], f, indent=2)

@app.route('/')
def index():
    faculties = load_data()
    return render_template('index.html', faculties=faculties)

@app.route('/add', methods=['GET','POST'])
def add_faculty():
    if request.method == 'POST':
        faculties = load_data()
        new_id = max([f.id for f in faculties], default=0) + 1
        f = Faculty(
            id=new_id,
            name=request.form['name'],
            department=request.form['department'],
            email=request.form['email'],
            role=request.form['role']
        )
        faculties.append(f)
        save_data(faculties)
        flash('Faculty added successfully.')
        return redirect(url_for('index'))
    return render_template('add_faculty.html')

@app.route('/delete/<int:fid>', methods=['POST'])
def delete_faculty(fid):
    faculties = load_data()
    faculties = [f for f in faculties if f.id != fid]
    save_data(faculties)
    flash('Faculty deleted.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Create an initial sample data file if missing
    if not os.path.exists(DATA_FILE):
        sample = [
            asdict(Faculty(id=1, name='Dr. A. Sharma', department='Physics', email='asharma@example.com', role='Admin')),
            asdict(Faculty(id=2, name='Ms. R. Patel', department='Chemistry', email='rpatel@example.com', role='Faculty'))
        ]
        with open(DATA_FILE, 'w') as f:
            json.dump(sample, f, indent=2)
    app.run(host='0.0.0.0', port=5000, debug=True)
