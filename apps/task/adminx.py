import xadmin

from .models import Task


class TaskAdmin(object):

    list_display = ['name', 'ctime', 'key_word', 'target_web', 'run_day', 'run_time', 'status', 'search_url']
    search_fields = ['name', 'ctime', 'key_word', 'target_web', 'run_day', 'run_time', 'status', 'search_url']
    list_filter = ['name', 'ctime', 'key_word', 'target_web', 'run_day', 'run_time', 'status', 'search_url']

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(TaskAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Task, TaskAdmin)