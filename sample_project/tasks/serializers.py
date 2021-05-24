from rest_framework import serializers
from tasks.models import Neo

class NeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neo
        fields = ('id', 'neo_reference_id' , 'name', 'nasa_jpl_url', 'is_potentially_hazardous_asteroid')


    

