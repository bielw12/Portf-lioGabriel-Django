from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Experience, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'updated_at']
    fields = [
        'name', 'title', 'bio', 'profile_image',
        'email', 'phone', 'location',
        'github_url', 'linkedin_url', 'twitter_url', 'website_url'
    ]
    
    def has_add_permission(self, request):
        # Permite apenas um perfil
        return not Profile.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    list_editable = ['proficiency', 'order']
    ordering = ['category', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'start_date', 'order']
    list_filter = ['status', 'featured', 'start_date']
    list_editable = ['featured', 'order']
    search_fields = ['title', 'description', 'technologies']
    date_hierarchy = 'start_date'
    
    fieldsets = [
        ('Informações Básicas', {
            'fields': ['title', 'short_description', 'description', 'image']
        }),
        ('URLs', {
            'fields': ['demo_url', 'github_url']
        }),
        ('Detalhes Técnicos', {
            'fields': ['technologies', 'status']
        }),
        ('Datas', {
            'fields': ['start_date', 'end_date']
        }),
        ('Controle de Exibição', {
            'fields': ['featured', 'order']
        }),
    ]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date']
    date_hierarchy = 'start_date'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read_status']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    def read_status(self, obj):
        if obj.read:
            return format_html('<span style="color: green;">✓ Lida</span>')
        return format_html('<span style="color: red;">✗ Não lida</span>')
    read_status.short_description = 'Status'
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
        self.message_user(request, f'{queryset.count()} mensagens marcadas como lidas.')
    mark_as_read.short_description = 'Marcar como lida'
    
    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
        self.message_user(request, f'{queryset.count()} mensagens marcadas como não lidas.')
    mark_as_unread.short_description = 'Marcar como não lida'


# Customização do admin
admin.site.site_header = "Portfólio - Administração"
admin.site.site_title = "Portfólio Admin"
admin.site.index_title = "Painel de Controle do Portfólio"
