from rest_framework import serializers                       # usually used for custom serializers
# from rest_framework.serializers import ModelSerializer     # more specific class for django models
from watchlist_app.models import Movie


#B MODELSERILIZER :
class MovieSerializer(serializers.ModelSerializer):    # class MovieSerializer(ModelSerializer): for ModelSerializer
    len_name = serializers.SerializerMethodField()   # additional field added
    
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']            # Add fields to be displayed
        # exclude = ['active']                              # Add fields to be excluded


    def get_len_name(self, object):  # additional field defined
        # length = len(object.name)
        return len(object.name)    

        
    # OBJECT-level validation ; Validating the whole model object    #2*
    def validate(self, data):

        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description cannot be same')
        else:
            return data
    


    # FIELD-level validation : validating name field in models    #1*
    def validate_name(self, value):

        if len(value) < 3:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value







#A  SERIALIZER :
# # VALIDATORS : validating name field in models     #3*
# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError('Name is too short!')


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])   #3
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data): # instance carries the old value while validated data has the new value
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    

#     # OBJECT-level validation ; Validating the whole model object    #2*
#     def validate(self, data):

#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description cannot be same')
#         else:
#             return data
    


#     # FIELD-level validation : validating name field in models    #1*
#     # def validate_name(self, value):

#     #     if len(value) < 3:
#     #         raise serializers.ValidationError('Name is too short!')
#     #     else:
#     #         return value