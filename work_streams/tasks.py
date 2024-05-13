from kaizaninterview.celery import app


@app.task
def test_task():
    print("!!!!!!!!! THIS IS A TASK !!!!!!!!!")
