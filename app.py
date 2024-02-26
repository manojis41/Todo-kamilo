from flask import Flask, render_template, request,redirect
import sqlite3 

# connect to the database 
conn = sqlite3.connect('todo.db',check_same_thread=False) 

# create a cursor object 
db = conn.cursor()   

app = Flask(__name__)
app.debug = True

if __name__ == '__main__':
    app.run()
    
@app.route('/',methods =["GET","POST"])
def home():
   db.execute("SELECT * FROM current ORDER BY id DESC")
   tasks = db.fetchall()
   return render_template('current.html',tasks=tasks)

@app.route('/completed',methods =["GET","POST"])
def completed():
   db.execute("SELECT * FROM completed ORDER BY id DESC")
   tasks = db.fetchall()
   return render_template('completed.html',tasks=tasks)

@app.route('/add',methods =["GET","POST"])
def add_task():
    if request.method == 'POST':
        task = request.form.get("task")
        db.execute(f"INSERT INTO current (task) VALUES(?)",(task,))
        
        # commit changes to the database 
        conn.commit()
    return redirect('/')

@app.route('/done',methods =["GET","POST"])
def completed_task():
    if request.method == 'POST':
        task_id = request.form.get("boxid")
        db.execute(f"INSERT INTO completed SELECT * FROM current WHERE id={task_id};")
        db.execute(f"DELETE FROM current WHERE id={task_id};")
        conn.commit()
    
    return redirect('/')

@app.route('/ongoing',methods =["GET","POST"])
def incomplete_task():
    if request.method == 'POST':
        task_id = request.form.get("boxid")
        db.execute(f"INSERT INTO current SELECT * FROM completed WHERE id={task_id};")
        db.execute(f"DELETE FROM completed WHERE id={task_id};")
        conn.commit()
    
    return redirect('/completed')
    
@app.route("/remove",methods=["GET","POST"])
def remove_task():
    if request.method == "POST":
        task_id = request.form.get("boxid")
        task_type = request.form.get("type")
        if(task_type == 'completed'or task_type == 'current'):
            db.execute(f"DELETE FROM {task_type} WHERE id={task_id};")
            conn.commit()
        if(task_type == 'completed'):
            return redirect('/completed')
    return redirect('/')

@app.route("/okay",methods=["GET","POST"])
def edit_task():
    if request.method == "POST":
        task_id = request.form.get("boxid")
        task_type = request.form.get("type")
        updated_text = request.form.get("updatedTask")
        if(task_type=='completed'or task_type=='current'):
              db.execute(f"UPDATE {task_type} SET task = '{updated_text}' WHERE id = '{task_id}'")
              conn.commit()
        if(task_type == 'completed'):
            return redirect('/completed')
    return redirect('/')
    
@app.errorhandler(404)
def handle_404(e):
    return "Something went wrong <br> Please get back to homepage <a href='/'>Current Tasks></a>"
# conn.close()        
