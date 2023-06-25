from celery.schedules import crontab

broker_url = 'redis://redis:6379/0'
result_backend = 'redis://redis:6379/0'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Kolkata'
enable_utc = True

beat_schedule = {
    'run-data-test-everyday-midnight': {
        'task': 'celery_worker.tasks.data_test',
        'schedule': crontab(hour=0, minute=0),
        'args': (),
    },
}

task_routes = {
    'main.data_test': {'queue': 'default'},
}
