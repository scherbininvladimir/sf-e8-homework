from celery import Celery
import requests

app = Celery('example', broker='redis://localhost', backend='redis://localhost')

@app.task
def get_python_from_html(address):
   r = {}
   try:
      r = requests.get(address)
      word_count = r.text.lower().count('python')
      return {'status_code': r.status_code,'word_count': r.text.lower().count('python')}
   except:
      return {'status_code': 'error','word_count': ''}
   
