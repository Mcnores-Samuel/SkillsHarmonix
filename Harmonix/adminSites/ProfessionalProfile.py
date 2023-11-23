from django.contrib import admin


class ProfessionalProfileAdmin(admin.ModelAdmin):
    """Professional profile admin.
    This class is used to display the professional profile model
    in the admin site.
    """
    list_display = ('jobseeker', 'first_name', 'last_name', 'address', 'city', 'state',
                    'zipcode', 'phone', 'email')
    search_fields = ('user', 'first_name', 'last_name', 'address', 'city', 'state')