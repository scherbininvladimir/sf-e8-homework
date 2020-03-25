import nsq
import pickle
from models import db, Tasks, Results

def handler(message):
    msg = pickle.loads(message.body)
    task_id = int(msg.get('task_id'))
    result = msg.get('result')
    task_item = Tasks.query.filter_by(id=task_id).first()
    result_item = Results(address=task_item.address, words_count=result.get('words_count', None))
    try:
        status_code = int(result.get('status_code'))
        task_item.http_status = status_code
        result_item.http_status_code = status_code
    except:
        pass
    db.session.add(task_item)
    db.session.add(result_item)
    db.session.commit()
    print(task_item.address, result)
    return True

r = nsq.Reader(message_handler=handler,
        nsqd_tcp_addresses=['127.0.0.1:4150'],
        topic='python', 
        channel='channel', lookupd_poll_interval=15)

if __name__ == '__main__':
    nsq.run()