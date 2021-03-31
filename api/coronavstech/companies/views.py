from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.coronavstech.companies.models import Company
from api.coronavstech.companies.serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request: Request) -> Response:
    """
    sends email with request payload
    sender: 4testing.tech@gmail.com
    receiver: 4testing.tech@gmail.com
    """
    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email="4testing.tech@gmail.com",
        recipient_list=["4testing.tech@gmail.com"]
    )
    return Response({"status": "success", "info": "email sent successfully"}, status=200)
