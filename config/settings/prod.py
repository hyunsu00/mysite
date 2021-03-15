# prod.py

from .base import *  # base.py 파일의 모든 내용을 사용한다는 의미

ALLOWED_HOSTS += ("52.78.36.85",)  # 아마존 AWS Lightsail
