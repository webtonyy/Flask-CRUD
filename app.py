from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(title=data.get("title"),id = task_id_control, desc=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"New task was added successfully"})

@app.route('/tasks', methods=['GET'])
def see_tasks():
    global task_id_control
    task_list = []
    for task in tasks:
        task_list.append(task.todict())

#task_list = [task.todict for task in tasks]


    output = {
                "tasks": task_list,
                "total_tasks":len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for i in tasks:
        if i.id == id:
            return jsonify(i.todict())
        
    return jsonify({"message":"ID not found"}), 404

@app.route("/tasks/<int:id>", methods=['PUT'])
def complete_task(id):
    task = None
    for i in tasks:
        if i.id == id:
            task = i
    if task == None:
        return jsonify({"message":"ID not found"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.desc = data['description']
    task.status = data['status']
    
    return jsonify({"message":"Task updated successfully"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def del_task(id):
    global task_id_control
    task = None
    for i in tasks:
        if i.id == id:
            task = i
        elif i.id>id:
            i.id -=1

    if task == None:
        return jsonify({"message":"ID not found"}), 404
    
        

    tasks.remove(task)
    task_id_control -= 1
    return jsonify({"message":"Task deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)