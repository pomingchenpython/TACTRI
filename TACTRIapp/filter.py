class maplistAdmin(admin.ModelAdmin):
    list_display=('id', 'mapName','mapDesc','mapLat','mapLng','mapTel','mapAddr')
    search_fields=['mapName'] 
class maplist1Admin(admin.ModelAdmin):
    list_display=('id', 'mapName','mapDesc','mapLat','mapLng','mapTel','mapAddr')
    search_fields=['mapName']  
admin.site.register(maplist,maplistAdmin)
admin.site.register(maplist1,maplist1Admin)