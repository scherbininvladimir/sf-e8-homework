from time import sleep
from models import db, Tasks, Results
from get_python_from_html import get_python_from_html
from celery.exceptions import TimeoutError


while True:
    for task in Tasks.query.filter_by(task_status='NOT_STARTED'):
        queue = get_python_from_html.delay(task.address)
        task.task_status='PENDING'
        db.session.add(task)
        db.session.commit()  
        try:
            result = queue.get(timeout=1)
            try:
                task.http_status = int(result.get('status_code'))
                result_item = Results(address=task.address, words_count=int(result.get('word_count')), http_status_code=int(result.get('status_code')))
            except:
                result_item = Results(address=task.address)
            print(task.address)
            print(queue.status)
            print(result)
            
        except: 
            result_item = Results(address=task.address)
        db.session.add(result_item)
        task.task_status='FINISHED'
        db.session.add(task)
        db.session.commit()    

    sleep(10)




