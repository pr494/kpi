from rest_framework import serializers, validators
from .models import Question

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("kpi_id", "label","stakeholder_id","element_id","element_label","element_type","is_integer","is_double","has_jump","is_required","option","created_at","updated_at","placeholder","subtype","is_jump","jump_value","jump_reference")