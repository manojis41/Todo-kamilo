from flask import Flask, render_template, request, redirect, session, url_for
from os import urandom
from bcrypt import checkpw, gensalt, hashpw
from sqlite3 import connect

# connect to the database
conn = connect('todo.db', check_same_thread=False)
db = conn.cursor()

app = Flask(__name__)
app.debug = True

app.secret_key = urandom(24)


@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db.execute("SELECT password FROM users WHERE username= ?", (username,))
        usrdata = db.fetchone()
        if usrdata:
            password = password.encode("utf-8")
            stored_password = usrdata[0]
            if checkpw(password, stored_password):
                session['user'] = username
                return redirect(url_for('home'))
            else:
                message = "Incorrect Password"
        else:
            message = "Incorrect username."

        return render_template("login.html", message=message)

    return render_template("login.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db.execute("SELECT username FROM users WHERE username =? ", (username,))
        existing_user = db.fetchone()
        if existing_user:
            message = "The username is already taken try another"
            return render_template("signup.html", message=message)
        else:
            salt = gensalt(rounds=10)
            password = password.encode("utf-8")
            hashed_password = hashpw(password, salt)
            db.execute("INSERT INTO users (username,password) VALUES(?,?)",
                       (username, hashed_password))
            return redirect(url_for('login'))
    return render_template("signup.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session['user'] = None
    return redirect('/login')


@app.route('/current', methods=["GET", "POST"])
def home():
    user = session.get('user')
    if user == None:
        return redirect(url_for('login'))
    db.execute("SELECT * FROM current WHERE user=? ORDER BY id DESC", (user,))
    tasks = db.fetchall()
    return render_template('current.html', tasks=tasks, user=user)


@app.route('/completed', methods=["GET", "POST"])
def completed():
    user = session.get('user')
    if user == None:
        return redirect(url_for('login'))
    db.execute("SELECT * FROM completed WHERE user=? ORDER BY id DESC", (user,))
    tasks = db.fetchall()
    return render_template('completed.html', tasks=tasks, user=user)


@app.route('/add', methods=["GET", "POST"])
def add_task():
    user = session.get('user')
    if user == None:
        user = 'public'
    if request.method == 'POST':
        task = request.form.get("task")
        db.execute(f"INSERT INTO current (task,user) VALUES(?,?)", (task, user))

        # commit changes to the database
        conn.commit()
    return redirect(url_for('home'))


@app.route('/done', methods=["GET", "POST"])
def completed_task():
    if request.method == 'POST':
        task_id = request.form.get("boxid")
        db.execute(
            f"INSERT INTO completed SELECT * FROM current WHERE id={task_id};")
        db.execute(f"DELETE FROM current WHERE id={task_id};")
        conn.commit()

    return redirect('/current')


@app.route('/ongoing', methods=["GET", "POST"])
def incomplete_task():
    if request.method == 'POST':
        task_id = request.form.get("boxid")
        db.execute(
            f"INSERT INTO current SELECT * FROM completed WHERE id={task_id};")
        db.execute(f"DELETE FROM completed WHERE id={task_id};")
        conn.commit()

    return redirect('/completed')


@app.route("/remove", methods=["GET", "POST"])
def remove_task():
    if request.method == "POST":
        task_id = request.form.get("boxid")
        task_type = request.form.get("type")
        if (task_type == 'completed' or task_type == 'current'):
            db.execute(f"DELETE FROM {task_type} WHERE id={task_id};")
            conn.commit()
        if (task_type == 'completed'):
            return redirect('/completed')
    return redirect('/current')


@app.route("/okay", methods=["GET", "POST"])
def edit_task():
    if request.method == "POST":
        task_id = request.form.get("boxid")
        task_type = request.form.get("type")
        updated_text = request.form.get("updatedTask")
        if (task_type == 'completed' or task_type == 'current'):
            db.execute(
                f"UPDATE {task_type} SET task = '{updated_text}' WHERE id = '{task_id}'")
            conn.commit()
        if (task_type == 'completed'):
            return redirect('/completed')
    return redirect('/current')


@app.errorhandler(404)
def handle_404(e):
    return render_template("error.html")
# conn.close()
