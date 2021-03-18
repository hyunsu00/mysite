# prod.py

from .base import *  # base.py 파일의 모든 내용을 사용한다는 의미

ALLOWED_HOSTS += ("52.78.36.85",)  # 아마존 AWS Lightsail

# Nginx에 정적 파일 위치를 /home/ubuntu/projects/mysite/static 디렉터리로 등록하였으므로 STATIC_ROOT도 위와 같이 설정해야 한다.
STATIC_ROOT = BASE_DIR / 'static/'

# base.py 파일에 STATICFILES_DIRS 항목이 이미 있는데 prod.py 파일에 다시 빈 값으로 설정하는 이유는 STATIC_ROOT가 설정된 경우 
# STATICFILES_DIRS 리스트에 STATIC_ROOT와 동일한 디렉터리가 포함되어 있으면 서버 실행 시 다음과 같은 오류가 발생하기 때문이다.
STATICFILES_DIRS = []

DEBUG = False

