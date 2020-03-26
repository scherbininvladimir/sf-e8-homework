import tornado.ioloop
import nsq
import pickle
from celery.exceptions import TimeoutError

from models import db, Tasks, Results

from get_python_from_html import get_python_from_html


def run_queue():
    for task in Tasks.query.filter_by(task_status='NOT_STARTED'):
        queue = get_python_from_html.delay(task.address)
        task.task_status='PENDING'
        db.session.add(task)
        db.session.commit()  
        try:
            result = {'task_id': task.id, 'result': queue.get(timeout=10)}
            writer.pub('python', pickle.dumps(result))
            print(queue.status, task.address)           
        except: 
            pass        
        task.task_status='FINISHED'
        db.session.add(task)
        db.session.commit()

if __name__ == '__main__':
    writer = nsq.Writer(['sf-e8-nsqd:4150'])
    tornado.ioloop.PeriodicCallback(run_queue, 10000).start()
    nsq.run()
