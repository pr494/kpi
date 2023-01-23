from django.db import models

# Create your models here.
class Question(models.Model):
    kpi_id = models.IntegerField(blank=True, null=True)
    stakeholder_id = models.IntegerField(blank=True, null=True)
    element_id = models.CharField(max_length=250, blank=True, null=True)
    element_label = models.TextField(blank=True, null=True)
    element_type = models.CharField(max_length=250, blank=True, null=True)
    is_integer = models.IntegerField(blank=True, null=True)
    is_double = models.IntegerField(blank=True, null=True)
    has_jump = models.IntegerField(blank=True, null=True)
    is_required = models.IntegerField(blank=True, null=True)
    option = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    regex = models.CharField(max_length=250, blank=True, null=True)
    icon = models.CharField(max_length=250, blank=True, null=True)
    label = models.CharField(max_length=250, blank=True, null=True)
    placeholder = models.CharField(max_length=250, blank=True, null=True)
    classname = models.CharField(db_column='className', max_length=250, blank=True, null=True)  # Field name made lowercase.
    subtype = models.CharField(max_length=250, blank=True, null=True)
    handle = models.CharField(max_length=250, blank=True, null=True)
    is_jump = models.IntegerField(blank=True, null=True)
    jump_value = models.CharField(max_length=250, blank=True, null=True)
    jump_reference = models.CharField(max_length=250, blank=True, null=True)
    is_group = models.IntegerField(blank=True, null=True)
    group_reference = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpi_question'