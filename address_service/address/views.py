import json
from django.http import JsonResponse
from .models import Address
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_or_update_address(request):
    if request.method == 'POST':
        try:
            # Parse incoming JSON data
            data = json.loads(request.body)
            address_id = data.get('AddressID')
            patient_id = data.get('PatientID')
            address_line1 = data.get('AddressLine1')
            address_line2 = data.get('AddressLine2')
            city = data.get('City')
            state = data.get('State')
            zip_code = data.get('ZipCode')

            # Create or update the address in the database
            address, created = Address.objects.update_or_create(
                address_id=address_id,
                defaults={
                    'patient_id': patient_id,
                    'address_line1': address_line1,
                    'address_line2': address_line2,
                    'city': city,
                    'state': state,
                    'zip_code': zip_code
                }
            )

            if created:
                return JsonResponse({'status': 'success', 'message': 'Address created successfully'}, status=201)
            else:
                return JsonResponse({'status': 'success', 'message': 'Address updated successfully'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)
