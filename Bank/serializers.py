from rest_framework import serializers
from Bank.models import banks, Branch

class bankserializer(serializers.ModelSerializer):
    class Meta():
        model = banks
        fields = '__all__'
class branchserializer(serializers.ModelSerializer):
    class Meta():
        model = Branch
        fields = '__all__'
