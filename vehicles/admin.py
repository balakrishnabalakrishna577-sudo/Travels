from django.contrib import admin
from .models import AirportTransfer


@admin.register(AirportTransfer)
class AirportTransferAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'passenger_name', 'passenger_phone',
                    'transfer_type', 'airport_name', 'pickup_date', 'vehicle_type',
                    'total_amount', 'status', 'payment_status']
    list_filter = ['status', 'payment_status', 'transfer_type', 'vehicle_type']
    search_fields = ['booking_id', 'passenger_name', 'passenger_phone', 'airport_name']
    readonly_fields = ['booking_id', 'created_at']
    list_per_page = 20
