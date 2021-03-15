# local.py

from .base import *  # base.py 파일의 모든 내용을 사용한다는 의미

# 디버그 툴바 설정
if DEBUG:
    INTERNAL_IPS = ("127.0.0.1",)
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

ALLOWED_HOSTS += ("127.0.0.1",)
