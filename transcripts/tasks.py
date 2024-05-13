from kaizaninterview.celery import app
from transcripts.models import Entry


@app.task
def do_something_with_entries():
    for entry in Entry.objects.all():
        print(entry, entry.work_interaction.title)
        # do something with the entry


@app.task
def do_something_with_entry(entry_id):
    entry = Entry.objects.get(id=entry_id)
    # make this race condition free
