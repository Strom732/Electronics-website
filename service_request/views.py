from django.shortcuts import render,redirect

# Create your views here.
def services(request):
    return render(request, 'services.html')
def service_request (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_type = request.POST.get('service_type')
        description = request.POST.get('description')

        # Save the service request
        ServiceRequest.objects.create(
            name=name,
            email=email,
            service_type=service_type,
            description=description
        )

        return redirect('service_request_success')
    return render(request, 'services.html' )
