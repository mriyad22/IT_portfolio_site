from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .forms import ContactForm

@require_http_methods(["GET", "POST"])
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Honeypot: silently reject likely bots without exposing the check.
        if form.cleaned_data.get("website"):
            messages.success(request, "Thanks. Your message has been received.")
            return redirect("contact:contact")
        message = form.save(commit=False)
        # Do not trust forwarded headers unless a trusted proxy is configured.
        message.ip_address = request.META.get("REMOTE_ADDR") or None
        message.save()
        messages.success(request, "Thanks for reaching out. Our team will contact you soon.")
        return redirect("contact:contact")
    
    messages.error(request, "Please correct the errors below and submit again.")

    context = {
        "form": form
    }
    return render(request, "contact/contact.html", context)
