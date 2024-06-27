# Personal Notes and To-Do List Application

Welcome to the Personal Notes and To-Do List Application! This project is a full-stack web application built using Flask that allows users to manage their personal notes and to-do lists. The application features user authentication, CRUD operations, and a responsive design.

## Features

- **User Authentication:** Secure login and registration system using Flask-Login.
- **CRUD Operations:** Create, read, update, and delete notes and to-do items.
- **Responsive Design:** Mobile-friendly and responsive interface using Bootstrap.
- **Real-time Feedback:** Flash messages for user actions.
- **Hover Actions:** Show delete button on hover for easy management of notes.

## Screenshots

### Home Page
![Home Page](path/to/home_page.png)

### Add New Note
![Add New Note](path/to/add_new_note.png)

### Edit Note<img width="1800" alt="Screenshot 2024-06-26 at 12 36 32 PM" src="https://github.com/perfect-123/Flask-Note-App/assets/57051815/f4cf7185-cc1e-43f5-8da2-4f41b2316ff2">

![Edit Note](path/to/edit_note.png)

### Delete Note
![Delete Note](path/to/delete_note.png)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/notes-todo-app.git
cd notes-todo-app
```
**Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**Install dependencies:**
```bash
pip install -r requirements.txt
```
**Set up the database:**
```bash
flask db init
flask db migrate
flask db upgrade
```
**Run the application**
```bash
flask run
```
## Usage
- Home Page: View your notes and to-do items.
- Add Note: Click on "Add New Note" to create a new note.
- Edit Note: Click on an existing note to edit it.
- Delete Note: Hover over a note and click the delete button to remove it.
- To-Do List: Manage your to-do items in a similar manner.
- Technologies Used
- Languages: Python, HTML, CSS, JavaScript
- Frameworks: Flask, Bootstrap
- Database: SQLite, SQLAlchemy
- Tools: Flask-Login, Jinja2, Git

## Contributing
- Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact me at perfect.ackah1@gmail.com.
