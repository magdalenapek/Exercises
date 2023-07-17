from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review, PhysicianUser
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist', )
        #fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    #len_name = serializers.SerializerMethodField
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatfromSerializer(serializers.ModelSerializer):
    #len_name = serializers.SerializerMethodField
   # watchlist = WatchListSerializer(many=True, read_only=True) #nazwa tego musi być taka sama jak releted name ustalony w modelu
    watchlist = serializers.StringRelatedField(many=True) # odnosi sie do metody __str__ w modelu - czyli zwroci tylko tytuł
    #primarykey related field zwraca pk 

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def get_len_name(self,object): #object ma dostep do kazdego pola w obiekcie
    #     return len(object.name)

    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Name and Description should be different!")
    #     else:
    #         return data

    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value



# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")


# class MovieSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description= serializers.CharField()
#     active= serializers.BooleanField()

#     def create(self, validated_data): ----------------------------- nie trzeba tego robić w ModelSerializerze
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data): #instance to stare dane, a validated data to nowe dane 
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name and Description should be different!")
#         else:
#             return data

    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

