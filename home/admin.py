from django.contrib import admin

from .models import Services,Brands,RecentWorks,Contactus,Testimonials,Blog,Feedback
import csv
from django.http import HttpResponse
from django.utils.html import format_html
from import_export.admin import ExportActionModelAdmin
from import_export.formats.base_formats import XLSX
from io import BytesIO
from import_export.formats.base_formats import XLSX
class FeedbackAdmin(ExportActionModelAdmin):
    list_display = (
        'name', 'phone', 'customer_type', 'service_satisfaction', 
        'vehicle_condition', 'staff_friendliness', 'price_rating', 
        'additional_feedback', 'created_at'
    )
    list_filter = ('customer_type', 'service_satisfaction', 'vehicle_condition')
    search_fields = ('name', 'phone')

    def get_export_formats(self):
        return [XLSX]  # Export format options (XLSX for Excel)

    def export_all_as_xlsx(self, request, queryset):
        from import_export.resources import modelresource_factory

        # Create a resource from the model
        Resource = modelresource_factory(model=self.model)
        resource = Resource()
        dataset = resource.export()

        # Create an Excel response
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={self.model._meta.verbose_name_plural}.xlsx'

        # Write data to the response
        with BytesIO() as output:
            export_format = XLSX()
            export_format.export_data(dataset, file_format=export_format, stream=output)
            response.write(output.getvalue())

        return response

    export_all_as_xlsx.short_description = "Export All as XLSX"

    def get_actions(self, request):
        actions = super().get_actions(request)
        # Adding a custom action for exporting all data
        actions['export_all_as_xlsx'] = (
            self.export_all_as_xlsx,
            'export_all_as_xlsx',
            'Export All as XLSX'
        )
        return actions
admin.site.register(Services)
admin.site.register(Brands)
admin.site.register(RecentWorks)
admin.site.register(Contactus)
admin.site.register(Testimonials)
admin.site.register(Blog)
admin.site.register(Feedback, FeedbackAdmin)