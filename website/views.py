from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request,'website/index.html')
def precautions(request):
    return render(request,'website/precautions.html')
def infectious(request):
    return render(request,'website/infectious.html')
def noncommunicable(request):
    return render(request,'website/noncommunicable.html')
def genetic(request):
    return render(request,'website/genetic.html')
def neurological(request):
    return render(request,'website/neurological.html')
def mental(request):
    return render(request,'website/mental.html')
def deficiency(request):
    return render(request,'website/deficiency.html')
def preinfectious(request):
    return render(request,'website/preinfectious.html')
def prenoncommunicable(request):
    return render(request,'website/prenoncommunicable.html')
def pregenetic(request):
    return render(request,'website/pregenetic.html')
def preneurological(request):
    return render(request,'website/preneurological.html')
def premental(request):
    return render(request,'website/premental.html')
def predeficiency(request):
    return render(request,'website/predeficiency.html')
def predictions(request):
    return render(request,'website/base.html')

def success(request):
    return render(request,'website/success.html')

def streamlit_view(request):
    return render(request, "streamlit_embed.html")

def contact_view(request):
    return render(request, 'website/contact.html')



from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject", "Contact Form Submission")
        message = request.POST.get("message")
        selected_options = request.POST.getlist("selected_options")  # Get multiple selected options

        selected_options_text = ", ".join(selected_options) if selected_options else "No options selected"

        full_message = f"""
        Name: {name}
        Email: {email}
        Selected Predictions: {selected_options_text}

        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            'nandakasireddy@gmail.com',  # Replace with your sender email
            ['kasireddynandakumarreddy2003@gmail.com'],  # Replace with recipient email
            fail_silently=False,
        )
        
        return redirect("success")  # Redirect to success page

    return render(request, "website/contact.html")

def success_view(request):
    return render(request, "website/success.html")

def my_view(request):
    options = [
        {'value': 'heart_model', 'label': 'Heart Disease'},
        {'value': 'hiv_model', 'label': 'HIV/AIDS'},
        {'value': 'skin_model', 'label': 'Skin Disease'},
        {'value': 'breast_model', 'label': 'Breast Cancer'},
        {'value': 'corona_model', 'label': 'COVID-19'},
        {'value': 'lung_model', 'label': 'Lung Disease'},
        {'value': 'obesity_model', 'label': 'Obesity'},
        {'value': 'prostate_model', 'label': 'Prostate Cancer'},
        {'value': 'malaria_model', 'label': 'Malaria'},
        {'value': 'diabetes_model', 'label': 'Diabetes'}
    ]
    return render(request, 'your_template.html', {'options': options})





