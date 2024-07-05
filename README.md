# Sticky Notes Application

This is a simple Django application for managing sticky notes. Users can create, edit, and delete notes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7+
- Django 4.2+
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/sticky-notes.git
    cd sticky-notes
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On MacOS/Linux
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional, for accessing the admin site):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application in your browser:**

    Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- **Home Page:** Displays a list of all notes.
- **Create Note:** Click "Add a new note" to create a new note.
- **Edit Note:** Click on a note's title to view details and then click "Edit" to modify it.
- **Delete Note:** Click on a note's title to view details and then click "Delete" to remove it.

