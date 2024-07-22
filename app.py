from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище задач в виде списка словарей
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_title = request.form['title']
        task_description = request.form['description']
        tasks.append({'title': task_title, 'description': task_description})
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = tasks[task_id]
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('update_task.html', task=task, task_id=task_id)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
