import xadmin

from .models import Plans


class PlansAdmin(object):

    list_display = ['goal', 'now_status', 'author']
    search_fields = ['goal', 'author']
    list_filter = ['goal', 'author']


xadmin.site.register(Plans, PlansAdmin)
