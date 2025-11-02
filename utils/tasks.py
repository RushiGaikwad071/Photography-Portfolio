from celery import shared_task
import time

@shared_task
def sample_background_task(name):
    print(f"Starting long task for {name}...")
    time.sleep(5)
    print(f"Task completed for {name}")
    return f"Task completed for {name}"
