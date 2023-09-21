from django.apps import AppConfig
import threading
from .schedule_tasks import run_schedule


class TaskConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "task"

    def ready(self):
        # Start your script in a separate thread
        script_thread = threading.Thread(target=run_schedule)
        script_thread.daemon = (
            True  # Allow the thread to exit when the main process exits
        )
        script_thread.start()
