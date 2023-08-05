from django.contrib import admin
from models.news import News


class NewsAdmin(admin.ModelAdmin):
    # eigenaar, publicatie datum en de publiceren tot datum
    list_display = ('title', 'changed_by', 'get_owner', 'publish_from', 'publish_to', 'is_global', 'is_sticky')
    list_filter = ['publish_from', 'is_global']
    search_fields = ['title', 'changed_by__userprofile__name', 'text']

    readonly_fields = ['highlight_from']

admin.site.register(News, NewsAdmin)
