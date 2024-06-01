from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB upload limit

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def init_db():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS grievances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        address TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        email_address TEXT NOT NULL,
        grievance_type TEXT NOT NULL,
        grievance_details TEXT NOT NULL,
        image_path TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    full_name = request.form['full_name']
    address = request.form['address']
    phone_number = request.form['phone_number']
    email_address = request.form['email_address']
    grievance_type = request.form['grievance_type']
    grievance_details = request.form['grievance_details']
    file = request.files['file']

    # Check if the file is present
    if file.filename == '':
        return redirect(request.url)

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Insert form data into the SQLite database
        try:
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            cur.execute('''
                INSERT INTO grievances (
                    full_name, address, phone_number, email_address,
                    grievance_type, grievance_details, image_path
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (full_name, address, phone_number, email_address,
                  grievance_type, grievance_details, file_path))
            
            conn.commit()
        except sqlite3.OperationalError as e:
            return f"A database error occurred: {e}"
        finally:
            conn.close()

        return 'Form submitted and file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
