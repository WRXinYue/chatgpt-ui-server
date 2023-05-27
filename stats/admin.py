from django.contrib import admin


from .models import TokenUsage

# stats 模块的管理员配置
@admin.register(TokenUsage)
class TokenUsageAdmin(admin.ModelAdmin):
    list_display = ('user', 'tokens')
