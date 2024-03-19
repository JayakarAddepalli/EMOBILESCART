from django.contrib import admin
from .models import *


# Register your models here.





class AppleAdmin(admin.ModelAdmin):
    list_display=['Image','Name','Info','Cost','Anchors']
    prepopulated_fields = {"slug": ("Name","Cost")}

    
class OneplusAdmin(admin.ModelAdmin):
    list_display=['Image','Name','Info','Cost','Anchors']
    prepopulated_fields = {"slug": ("Name","Cost")}

class RedmiAdmin(admin.ModelAdmin):
    list_display=['Image','Name','Info','Cost','Anchors']
    prepopulated_fields = {"slug": ("Name","Cost")}

class RealmeAdmin(admin.ModelAdmin):
    list_display=['Image','Name','Info','Cost','Anchors']
    prepopulated_fields = {"slug": ("Name","Cost")}

    
class SamsungAdmin(admin.ModelAdmin):
    list_display=['Image','Name','Info','Cost','Anchors']
    prepopulated_fields = {"slug": ("Name","Cost")}

class OneplusAdmin(admin.ModelAdmin):
    list_display=['Image','Name','Info','Cost','Anchors']
    prepopulated_fields = {"slug": ("Name","Cost")}




# class RealmeAdmin(admin.ModelAdmin):
#     list_display=['Image','Name','Info','Cost']

# class RedmiAdmin(admin.ModelAdmin):
#     list_display=['Image','Name','Info','Cost']

# class SamsungAdmin(admin.ModelAdmin):
#     list_display=['Image','Name','Info','Cost']


admin.site.register(Apple,AppleAdmin)

admin.site.register(Samsung,SamsungAdmin)
admin.site.register(Redmi,RedmiAdmin)
admin.site.register(Realme,RealmeAdmin)
admin.site.register(CartItem)
admin.site.register(Oneplus,OneplusAdmin)
admin.site.register(OneplusCartItem)
admin.site.register(SamsungCartItem)
admin.site.register(RedmiCartItem)
admin.site.register(RealmeCartItem)



# admin.site.register(CartItem)

# admin.site.register(Realme,RealmeAdmin)
# admin.site.register(Redmi,RedmiAdmin)
# admin.site.register(Samsung, SamsungAdmin)

# admin.site.register(TrendingItems)

admin.site.register(Trends)