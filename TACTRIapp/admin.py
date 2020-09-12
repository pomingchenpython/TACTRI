from django.contrib import admin
from TACTRIapp.models import maplist,maplist1

from import_export.admin import ImportExportModelAdmin

class maplistAdmin(ImportExportModelAdmin):
    list_display=('id', 'mapName','mapDesc','mapLat','mapLng','mapTel','mapAddr')
    search_fields=['mapName'] 
class maplist1Admin(ImportExportModelAdmin):
    list_display=('id','mapName','mapDesc','mapLat','mapLng','mapTel','mapAddr')
    search_fields=['mapName'] 



           
admin.site.register(maplist,maplistAdmin)
admin.site.register(maplist1,maplist1Admin)


