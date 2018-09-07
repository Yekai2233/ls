import xadmin

from .models import Task


class TaskAdmin(object):

    list_display = ['name', 'key_word', 'target_web', 'run_time', 'status']
    search_fields = ['name', 'key_word', 'target_web', 'run_time', 'status']
    list_filter = ['name', 'key_word', 'target_web', 'run_time', 'status']


xadmin.site.register(Task, TaskAdmin)