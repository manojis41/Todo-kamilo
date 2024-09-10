![apple-touch-icon](https://github.com/manojis41/Todo-kamilo/assets/126950007/7f091e38-3e3d-4aef-8241-ca2711809a08)
# Todo kamilo

It is a simple task management tool built with Flask and SQLite3. It allows users to add, update, and track their tasks, with options for both single-user and multi-user functionality.

## Features

- **Single User & Multi-User Versions**:
  - Single User: Available on the `single-user` branch.
  - Multi-User: Main branch and demo available.
- **Todo Management**:
  - Add, update, and delete todo tasks.
  - Mark tasks as completed and view them on a separate page.
- **User Management (Multi-User)**:
  - Create an account and log in to manage your tasks.
  - View demo: [Demo](https://manojis41.pythonanywhere.com)
## Installation

### Single User Version

1. **Clone the repository:**
   ```bash
   git clone -b single-user https://github.com/manojis41/Todo-kamilo.git
   ```
1. **Activate the Virtual Environment:**

   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

   - **On Windows:**
     ```bash
     .venv\Scripts\activate
     ```
3. **Run the Flask application:**
   ```bash
   flask run
   ```

### Multi-User Version

- Access the demo version [here](https://manojis41.pythonanywhere.com).

### Running the Multi-User Version Locally

To run the multi-user version of Todo Kamilo on your local machine:

1. **Clone the repository:**
   ```bash
   git clone -b multi-user https://github.com/manojis41/Todo-kamilo.git
   ```
2. **Activate the Virtual Environment:**

   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

   - **On Windows:**
     ```bash
     .venv\Scripts\activate
     ```

3. **Start the Application:**

   ```bash
    flask run
   ```

4. **Set Up User Accounts:**

   - Visit `http://127.0.0.1:5000/signup` or click the "Don't have an account yet?" link on the default page.
   - Create a new account by filling out the registration form.
   - After creating an account, you will be redirected to the login page.

5. **Login and Use the App:**

   - Enter your credentials on the login page.
   - Once logged in, you can access and use the app with multiple user support.

The multi-user version includes an extra table in the database for securely storing user credentials.

## Usage

![Todo-kamilo](https://github.com/manojis41/Todo-kamilo/assets/126950007/11332947-0733-4955-920c-155549ef2980)
- **Single User**: Run the Flask app to manage todo tasks.
- **Multi-User**: Sign up and log in to manage tasks.

## Configuration

- For the multi-user version, sign up to create an account.
- For the single-user version, ensure Python and Flask are installed. The virtual environment (`.venv`) includes necessary dependencies. If you need to set up your own, a `requirements.txt` will be added later.

## Contributing

- Feel free to contribute by starring the repo, branching, sending pull requests, or improving the project.
- <h4>Technology used</h4>
<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-original.svg"  title="CSS3" alt="CSS" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="40" height="40"/>&nbsp;
  
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python"  alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/flask/flask-original.svg" title="Flask"  alt="Flask" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original.svg" title="SQLite"  alt="SQLite" width="40" height="40"/>&nbsp;

  <img src="https://github.com/devicons/devicon/blob/master/icons/linux/linux-original.svg" title="Linux"  alt="Linux" width="40" height="40"/>&nbsp;
  <img src="https://github.com/VSCodium/vscodium/raw/master/icons/stable/codium_cnl.svg" title="VSCodium"  alt="VSCodium" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original.svg" title="Git"  alt="Git" width="40" height="40"/>&nbsp;
</div>

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

## Contact
**Email:** [contact@manoj41.com.np](mailto:contact@manoj41.com.np)
For questions or support, visit [manoj41.com.np/contact](https://manoj41.com.np/contact) or check the contact information on GitHub.

