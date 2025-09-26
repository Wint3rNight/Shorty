from django.db import models,transaction
from django.contrib.auth.models import User
from django.db.models import F 
from django.conf import settings
from .utils import encode,generate_salt,create_unique_id_from_pk_and_salt

class ShortenedURL(models.Model):
    id=models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url=models.URLField(max_length=2048)
    short_code=models.CharField(max_length=15, unique=True, blank=True, null=True, db_index=True)
    salt=models.PositiveIntegerField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    click_count=models.PositiveIntegerField(default=0)

    class Meta:
        ordering=['created_at']
    
    def __str__(self):
        return f'{self.short_code}->{self.original_url[:50]}'

    def generate_and_save_short_code(self):
        if not self.pk:
            raise ValueError("Instance must be saved before calling this method.")
        while True:
            try:
                with transaction.atomic():
                    salt=generate_salt()
                    unique_id=create_unique_id_from_pk_and_salt(self.pk,salt)
                    short_code=encode(unique_id)
                    print(f"Looping -> PK: {self.pk}, Salt: {salt}, Code: {short_code}")
                    if not ShortenedURL.objects.filter(short_code=short_code).exists():
                        self.salt=salt
                        self.short_code=short_code
                        self.save(update_fields=['salt','short_code'])
                        break
            except Exception:
                continue
            #except Exception as e:
                #print(f"!!! INFINITE LOOP DETECTED, HIDDEN ERROR: {e}")
                #continue
