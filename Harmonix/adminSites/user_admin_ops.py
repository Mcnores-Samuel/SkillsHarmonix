from django.contrib.auth.admin import UserAdmin


class HarmonixUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name',
                    'user_type', 'is_staff', 'is_active',
                    'date_joined', 'last_login')
    list_filter = ('user_type',)
    search_fields = ('username', 'email', 'first_name', 'last_name',
                     'user_type', 'is_staff', 'is_active')
    ordering = ('is_staff',)
    readonly_fields = ('id', 'date_joined', 'last_login')
