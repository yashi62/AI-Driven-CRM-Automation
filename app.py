from flask import Flask, request, jsonify, render_template
from ai_engine import AIEngine
from task_scheduler import TaskScheduler

app = Flask(__name__)
ai_engine = AIEngine()
task_scheduler = TaskScheduler()

@app.route('/')
def dashboard():
    logs = task_scheduler.get_logs()
    return render_template('dashboard.html', logs=logs)

@app.route('/ai_response', methods=['POST'])
def ai_response():
    data = request.json
    user_input = data.get('user_input', '')

    if not user_input:
        return jsonify({'error': 'Input text is required'}), 400

    try:
        response = ai_engine.generate_response(user_input)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/schedule_task', methods=['POST'])
def schedule_task():
    data = request.json
    task_name = data.get('task_name', '')
    interval = data.get('interval', 60)

    if not task_name:
        return jsonify({'error': 'Task name is required'}), 400

    try:
        task_scheduler.schedule_task(task_name, interval)
        return jsonify({'message': f'Task "{task_name}" scheduled every {interval} seconds.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
