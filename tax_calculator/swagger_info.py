from drf_yasg import openapi

info = openapi.Info(
    title="Your API Title",
    default_version="v1",
    description="Description of your API",
    terms_of_service="https://example.com/terms",
    contact=openapi.Contact(email="your@email.com"),
    license=openapi.License(name="Your License"),
)
