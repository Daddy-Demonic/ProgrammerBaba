# import os
# from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Configuration
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'xlsx', 'docx', 'pptx', 'mp4', 'avi', 'mov', 'wmv'}
# app.secret_key = 'supersecretkey'

# # Ensure upload directory exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# # Simple in-memory user database
# users_db = {
#     "admin": {"password": "adminpass", "role": "admin"},
#     "student1": {"password": "studentpass", "role": "student"},
#     "teacher1": {"password": "teacherpass", "role": "teacher"},
# }

# # Helper function to check allowed file extensions
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# # Existing route for viewing lectures
# @app.route('/')
# def index():
#     # Assuming you have an existing route for home or dashboard
#     return render_template('index.html')

# # New route to upload notes
# @app.route('/notes/upload', methods=['GET', 'POST'])
# def upload_notes():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             flash('File successfully uploaded')
#             return redirect(url_for('view_notes'))

#     return render_template('upload_notes.html')

# # New route to view uploaded notes
# @app.route('/notes', methods=['GET'])
# def view_notes():
#     # List all files in the upload folder
#     files = os.listdir(app.config['UPLOAD_FOLDER'])
#     files = [f for f in files if allowed_file(f)]
#     return render_template('notes.html', files=files)

# # Route to download files
# @app.route('/uploads/<filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# # Include your existing routes and features here...

# if __name__ == '__main__':
#     app.run(debug=True)
