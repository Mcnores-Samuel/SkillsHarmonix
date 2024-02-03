from django.contrib import admin


class BusinessProfileAdmin(admin.ModelAdmin):
    """Business profile admin.
    This class is used to display the business profile model
    in the admin site.
    """
    list_display = ('representative', 'business_name',
                    'address', 'city', 'state',
                    'zipcode', 'phone', 'email')
    search_fields = ('representative', 'business_name',
                     'address', 'city', 'state')
