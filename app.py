from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ismail43@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<id: {self.id}, name: {self.description}>'


db.create_all()


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/todos/create', methods=['POST'])
def create_todos():
    description = request.get_json()['description']
    add_todo = Todo(description=description)
    db.session.add(add_todo)
    db.session.commit()
    return jsonify({
        'description': add_todo.description
    })


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
