from authenticationapp.api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('auth', userviewsets)