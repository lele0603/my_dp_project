from django.contrib import admin
from TestModel.models import Test, Contact, Tag

# Register your models here.
# admin.site.register([Test, Contact, Tag])


class TagInLine(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    #fields = ('name', 'email')
    # 折叠展示
    # fieldsets = (
    #     ['Main', {
    #         'fields': ('name', 'email'),
    #     }],
    #     ['Advance', {
    #         'classes': ('collapse',),  # CSS
    #         'fields': ('age',),
    #     }]
    # )
    list_display = ('name', 'age', 'email')
    search_fields = ('name',)
    inlines = [TagInLine]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
