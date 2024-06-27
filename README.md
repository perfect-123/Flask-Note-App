# Personal Notes and To-Do List Application

Welcome to the Personal Notes and To-Do List Application! This project is a full-stack web application built using Flask that allows users to manage their personal notes and to-do lists. The application features user authentication, CRUD operations, and a responsive design.

## Features

- **User Authentication:** Secure login and registration system using Flask-Login.
- **CRUD Operations:** Create, read, update, and delete notes and to-do items.
- **Responsive Design:** Mobile-friendly and responsive interface using Bootstrap.
- **Real-time Feedback:** Flash messages for user actions.
- **Hover Actions:** Show delete button on hover for easy management of notes.

**- Currently working on adding a markdown capability. Help anyway you can!**

## Screenshots

### Login
<img width="1796" alt="Screenshot 2024-06-27 at 12 56 16 AM" src="https://github.com/perfect-123/Flask-Note-App/assets/57051815/da9e184d-d646-460f-b3e1-5ed566c98195">

### Home Page
<img width="1794" alt="Screenshot 2024-06-27 at 12 53 15 AM" src="https://github.com/perfect-123/Flask-Note-App/assets/57051815/60cf5cd1-cb87-4d0b-909b-1b6c8b18ca0f">
### Add New Note

### Edit Note
<img width="900" alt="Screenshot 2024-06-27 at 12 53 27 AM" src="https://github.com/perfect-123/Flask-Note-App/assets/57051815/5a77908b-d3b7-493e-94a0-281013b702ae">

### Todo
<img width="1792" alt="Screenshot 2024-06-27 at 12 58 18 AM" src="https://github.com/perfect-123/Flask-Note-App/assets/57051815/391e2ab0-19c1-4d89-87fa-e963a762f0c9">



![Edit Note](path/to/edit_note.png)


## Installation

1. **Clone the repository:**![Uploading Screenshot 2024-06-27 at 12.53.15 AM.png…]()

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
