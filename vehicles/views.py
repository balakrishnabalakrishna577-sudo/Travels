from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import AirportTransfer
from .forms import AirportTransferForm

# Pricing per vehicle type for airport transfer
TRANSFER_PRICING = {
    'sedan': 800,
    'suv': 1200,
    'tempo': 2000,
    'bus': 3500,
}


def airport_transfer(request):
    form = AirportTransferForm()
    pricing = TRANSFER_PRICING

    if request.method == 'POST':
        form = AirportTransferForm(request.POST)
        if form.is_valid():
            transfer = form.save(commit=False)
            if request.user.is_authenticated:
                transfer.user = request.user
            base = TRANSFER_PRICING.get(transfer.vehicle_type, 800)
            transfer.total_amount = base * 2 if transfer.transfer_type == 'both' else base
            transfer.save()
            messages.success(
                request,
                f'Airport transfer booked! Booking ID: {transfer.booking_id}. We will contact you shortly.'
            )
            return redirect('airport_transfer_success', booking_id=transfer.booking_id)

    context = {
        'form': form,
        'pricing': pricing,
        'meta_title': 'Airport Pickup & Drop - Hanuman Tours and Travels',
        'meta_description': 'Book airport pickup and drop service with Hanuman Tours and Travels. AC vehicles, professional drivers.',
    }
    return render(request, 'vehicles/airport_transfer.html', context)


def airport_transfer_success(request, booking_id):
    transfer = get_object_or_404(AirportTransfer, booking_id=booking_id)
    return render(request, 'vehicles/airport_transfer_success.html', {'transfer': transfer})
