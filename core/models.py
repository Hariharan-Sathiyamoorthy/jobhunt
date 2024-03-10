
from django.db import models

from django.contrib.auth.models import User



# Create your models here.


class Whishlist(models.Model):
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    closing_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    move_to_applied = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Whishlist"


    def __str__(self):
        return self.company_name
    def moveToApplied(self):
        self.move_to_applied = True
        self.save()

        applied = Applied(
            role=self.role,
            company_name=self.company_name,
            location=self.location,
            basic_salary=self.basic_salary,
            closing_date=self.closing_date,
            created_by=self.created_by
        )
        applied.save()
        return applied
    


class Applied(models.Model):
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    closing_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    move_to_rejected = models.BooleanField(default=False)
    move_to_interview = models.BooleanField(default=False)

    def moveToRejected(self):
        self.move_to_rejected = True
        self.save()

        rejected = Rejected(
            role=self.role,
            company_name=self.company_name,
            location=self.location,
            basic_salary=self.basic_salary,
            created_by=self.created_by
        )
        rejected.save()

        return rejected
    def moveToInterview(self):
        self.move_to_interview = True
        self.save()

        interview = Interview(
            role=self.role,
            company_name=self.company_name,
            location=self.location,
            basic_salary=self.basic_salary,
            created_by=self.created_by
        )
        interview.save()

        return interview

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Applied"

    def __str__(self):
        return self.company_name
    
class Interview(models.Model):
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    interview_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    move_to_offer = models.BooleanField(default=False)
    move_to_rejected = models.BooleanField(default=False)

    def moveToRejected(self):
        self.move_to_rejected = True
        self.save()

        rejected = Rejected(
            role=self.role,
            company_name=self.company_name,
            location=self.location,
            basic_salary=self.basic_salary,
            created_by=self.created_by
        )
        rejected.save()

        return rejected

    def moveToOffer(self):
        self.move_to_offer = True
        self.save()

        offer = Offer(
            role=self.role,
            company_name=self.company_name,
            location=self.location,
            basic_salary=self.basic_salary,
            created_by=self.created_by
        )
        offer.save()

        return offer


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Interview"
    def __str__(self):
        return self.company_name
    
class Offer(models.Model):
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Offer"
    def __str__(self):
        return self.company_name
    
class Rejected(models.Model):
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    reason = models.TextField(null=True, blank=True)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Rejected"
    def __str__(self):
        return self.company_name
    