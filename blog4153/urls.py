from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # OpenAPI schema in JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI documentation
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('', include('blog_app.urls')),
]
