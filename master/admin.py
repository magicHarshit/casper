from models import  City, Area, Locality, LocalityArea, Region, State, Country, PinCode
from django.contrib import admin
from forms import CityAdminForm,RegionAdminForm






class StateAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "name", )}

class CityRegionInline( admin.TabularInline ):
    model = City.region.through
    extra = 1

class CityAdmin( admin.ModelAdmin ):
    search_fields = ['name']
    prepopulated_fields = {"slug": ( "name", )}
    form = CityAdminForm
    inlines = ( CityRegionInline, )

class RegionStateInline( admin.TabularInline ):
    model = Region.state.through
    extra = 1

class RegionAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "name", )}
    form = RegionAdminForm
    inlines = ( RegionStateInline, )

class AreaAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "name", )}
    model = Area
    list_filter = ['city']

class LocalityAreaInline( admin.TabularInline ):
    model = LocalityArea
    extra = 1

class LocalityAdmin( admin.ModelAdmin ):
    list_display = ( 'name', )
    prepopulated_fields = {"slug": ( "name", )}
    inlines = ( LocalityAreaInline, )
    model = Locality
    list_filter = ['area__name']

class CountryAdmin( admin.ModelAdmin ):

    model = Country
    list_display = [ 'name' ]
    ordering = ['name']
    search_fields = ['name']
    prepopulated_fields = {"slug": [ 'name' ]}

class PinCodeAdmin( admin.ModelAdmin ):
    model = PinCode



admin.site.register( PinCode, PinCodeAdmin )
admin.site.register( Country, CountryAdmin )
admin.site.register( State, StateAdmin )
admin.site.register( Region, RegionAdmin )
admin.site.register( City, CityAdmin )
admin.site.register( Area, AreaAdmin )
admin.site.register( Locality, LocalityAdmin )
