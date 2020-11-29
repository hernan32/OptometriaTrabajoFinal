from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


def index(request):
    return render(request, "index/index.html")


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: Googlebot",
        "Disallow: /",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")