from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # 새로운 model을 만들 때 시각 기록
    updated = models.DateTimeField(auto_now=True)  # 새로운 날짜로 update시킴

    # 데이터베이스에 등록하지 않기 위해(abstract) - 추상 모델
    class Meta:
        abstract = True
