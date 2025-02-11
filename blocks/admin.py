from django.contrib import admin

from blocks.models import Block


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = (
        "currency",
        "provider",
        "number",
        "best_block_time"
    )
    readonly_fields = list_display

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("currency", "provider")
