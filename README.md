![apple-touch-icon](https://github.com/manojis41/Todo-kamilo/assets/126950007/7f091e38-3e3d-4aef-8241-ca2711809a08)

# Todo Kamilo - Multi-User Version

**Todo Kamilo** is a todo list application built with Flask and SQLite3, now supporting multiple users. This README provides instructions for installing, running, and using the multi-user version locally.
 - View demo: [Demo](https://manojis41.pythonanywhere.com)

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Using the Multi-User Features](#using-the-multi-user-features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

Todo Kamilo is designed to manage tasks efficiently with a multi-user capability. Each user has their own secure account and task list.

## Installation

### Prerequisites

- Python 3.x installed on your PC.

### Clone the Repository

To get started, clone the repository:

```bash
git clone -b multi-user https://github.com/manojis41/Todo-kamilo.git
cd todo-kamilo
```

### Setting Up the Environment

1. **Create and Activate the Virtual Environment:**

   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

   - **On Windows:**
     ```bash
     .venv\Scripts\activate
     ```

   The virtual environment contains all the necessary packages, including Flask and other dependencies.

2. **Install Dependencies (if needed):**

   If the virtual environment does not include all dependencies, install them with:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Application:**

   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     python app.py
     ```

   - **On Windows:**
     ```bash
     .venv\Scripts\activate
     python app.py
     ```

2. **Access the Application:**

   Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Using the Multi-User Features

1. **Create an Account:**

   - Visit `http://127.0.0.1:5000/signup` or click the "Don't have an account yet?" link on the default page.
   - Fill out the registration form to create a new account. 

2. **Log In:**

   - After creating an account, you will be redirected to the login page.
   - Enter your credentials to log in.

3. **Access Your Task List:**

   - Once logged in, you can manage your tasks and access features specific to your account.

The multi-user version includes an additional database table for securely storing user credentials.

## Contributing

Contributions to the multi-user version are welcome! To contribute:

1. Fork the repository and create a new branch for your changes.
2. Make your improvements or fixes.
3. Submit a pull request.

Feel free to distribute and enhance this project as you see fit.
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

Todo Kamilo is licensed under the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0). See the LICENSE file for more details.

## Contact

For any inquiries or further information, please reach out:

- **GitHub:** [manojis41](https://github.com/manojis41)
- **Email:** [contact@manoj41.com.np](mailto:contact@manoj41.com.np)
- **More Contacts :** [manoj41.com.np/contact](http://manoj41.com.np/contact)
