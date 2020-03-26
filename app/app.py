from datetime import datetime
from flask import request, render_template, redirect
from models import db, app, Tasks, Results

@app.route("/")
def hello():
    address = request.args.get('address')
    results = Results.query.all()
    if address:
        address = address.strip()
        if not address.startswith('http://') and not address.startswith('https://'):
            address = 'http://'+address
        task = Tasks(address=address, task_status='NOT_STARTED', timestamp=datetime.now())
        db.session.add(task)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', results=results)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=False, host='0.0.0.0', port=5001)
