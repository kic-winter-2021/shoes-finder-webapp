from django.db import models


class Brand(models.Model):
    # 브랜드 코드
    brandcode = models.PositiveSmallIntegerField(primary_key=True)
    # 브랜드 명
    brandname = models.CharField(max_length=30)
    url = models.CharField(max_length=100)

    def __str__(self):
        return f'Brand[{self.brandcode}={self.brandname}]'
