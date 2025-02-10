from django.contrib import admin

from blocks.models import Block


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = (
        "currency",
        "provider",
        "number",
    )
    readonly_fields = list_display + ("blockchain_created_at",)
