from django.contrib import admin
from puliapp.models import maplist,maplist1

from import_export.admin import ImportExportModelAdmin

class maplistAdmin(ImportExportModelAdmin):
    list_display=('id', 'mapName','mapDesc','mapLat','mapLng','mapTel','mapAddr')
class maplist1Admin(ImportExportModelAdmin):
    list_display=('id','mapName','mapDesc','mapLat','mapLng','mapTel','mapAddr')

admin.site.register(maplist,maplistAdmin)
admin.site.register(maplist1,maplist1Admin)


