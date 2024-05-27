from kaizaninterview.celery import app
from transcripts.models import WorkInteraction
from work_streams.models import WorkStream


@app.task
def do_something_with_work_streams():
    for work_stream in WorkStream.objects.all():
        work_interaction_count = WorkInteraction.objects.filter(work_stream=work_stream).count()
        work_stream.title = f"{work_stream.title} ({work_interaction_count})"
        work_stream.save()
