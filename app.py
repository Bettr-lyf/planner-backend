
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-key-123')

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client.planner_db

def login_required(f):
    # Placeholder for future authentication
    return f

@app.route('/')
@login_required
def index():
    goals = {
        'daily': list(db.goals.find({'type': 'daily'})),
        'weekly': list(db.goals.find({'type': 'weekly'})),
        'monthly': list(db.goals.find({'type': 'monthly'}))
    }
    return render_template('index.html', goals=goals)

@app.route('/add-goal', methods=['GET', 'POST'])
@login_required
def add_goal():
    if request.method == 'POST':
        goal = {
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'type': request.form.get('type'),
            'created_at': datetime.utcnow()
        }
        db.goals.insert_one(goal)
        flash('Goal added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_goal.html')

@app.route('/reflect', methods=['GET', 'POST'])
@login_required
def reflect():
    if request.method == 'POST':
        reflection = {
            'rating': int(request.form.get('rating')),
            'notes': request.form.get('notes'),
            'date': datetime.utcnow()
        }
        db.reflections.insert_one(reflection)
        flash('Reflection added!', 'success')
        return redirect(url_for('index'))
    return render_template('reflect.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
