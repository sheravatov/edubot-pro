from django.contrib import admin
from django.db.models import Sum, Count
from .models import TGUser, DocHistory, Transaction

admin.site.site_header = "EduBot Pro Boshqaruv"
admin.site.site_title = "EduBot Admin"
admin.site.index_title = "Statistika va Boshqaruv"

@admin.register(TGUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'full_name', 'username', 'balance', 'free_pptx', 'free_docx', 'is_blocked', 'joined_at')
    search_fields = ('full_name', 'username', 'tg_id')
    list_filter = ('is_blocked', 'joined_at')
    list_editable = ('balance', 'is_blocked', 'free_pptx', 'free_docx')
    ordering = ('-joined_at',)

@admin.register(DocHistory)
class DocAdmin(admin.ModelAdmin):
    list_display = ('topic', 'doc_type', 'pages', 'user', 'web_user_ip', 'status_color', 'created_at')
    list_filter = ('doc_type', 'created_at')
    search_fields = ('topic', 'user__full_name')

@admin.register(Transaction)
class TransAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'created_at')
    list_filter = ('created_at', 'type')