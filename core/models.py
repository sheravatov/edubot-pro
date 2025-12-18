from django.db import models
from django.utils.html import format_html

class TGUser(models.Model):
    tg_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name="Username")
    full_name = models.CharField(max_length=255, verbose_name="Ism-Familiya")
    balance = models.IntegerField(default=0, verbose_name="Balans (so'm)")
    
    # Limitlar
    free_pptx = models.IntegerField(default=2, verbose_name="Bepul PPTX")
    free_docx = models.IntegerField(default=2, verbose_name="Bepul DOCX")
    
    # Status
    is_blocked = models.BooleanField(default=False, verbose_name="Bloklangan")
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return f"{self.full_name} ({self.tg_id})"

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "👥 Foydalanuvchilar"

class DocHistory(models.Model):
    user = models.ForeignKey(TGUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Foydalanuvchi")
    web_user_ip = models.CharField(max_length=50, null=True, blank=True, verbose_name="Web IP")
    doc_type = models.CharField(max_length=50, choices=[('pptx', 'Taqdimot'), ('docx', 'Referat')], verbose_name="Turi")
    topic = models.TextField(verbose_name="Mavzu")
    pages = models.IntegerField(verbose_name="Hajm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def status_color(self):
        return format_html('<span style="color: green;">✔ Muvaffaqiyatli</span>')
    status_color.short_description = "Status"

    class Meta:
        verbose_name = "Hujjat Tarixi"
        verbose_name_plural = "📂 Hujjatlar Arxivi"

class Transaction(models.Model):
    user = models.ForeignKey(TGUser, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    amount = models.IntegerField(verbose_name="Summa")
    type = models.CharField(max_length=50, default="payment", verbose_name="To'lov turi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")

    class Meta:
        verbose_name = "To'lov"
        verbose_name_plural = "💰 To'lovlar"