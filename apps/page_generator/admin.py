from django.contrib import admin
from .models.person import *
from .models.table import *
from .models.common_models import *

admin.site.register(Person)
admin.site.register(PhoneNumber)
admin.site.register(Table)
admin.site.register(TableCodeColumn)
admin.site.register(TableDirectionColumn)
admin.site.register(PageGenerator)
