from datetime import datetime
from kaizaninterview.celery import app
from transcripts.models import Entry


@app.task
def do_something_with_entries():
    for entry in Entry.objects.all():
        print(entry, entry.work_interaction.title)


@app.task
def do_something_with_entry(entry_id, content):
    entry = Entry.objects.get(id=entry_id)
    entry.content = generate_content(content)
    entry.save()


def generate_content(entry):
    new_content = entry.content + " " + str(datetime.now())
    return new_content


@app.task
def do_something_once():
    print("This is a one-time task.")
