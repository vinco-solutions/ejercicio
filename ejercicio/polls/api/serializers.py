from rest_framework import serializers
from polls.models import Question
from django.utils import timezone

class question_serializer(serializers.ModelSerializer):

    days_since_created = serializers.SerializerMethodField('get_days_since_created')

    def get_days_since_created(self, obj):
        days = (timezone.now().date() - obj.pub_date.date())/(24*60*60)
        return days

    class Meta:
        model = Question
        fields = "__all__"
        extra_fields = ['days_since_created']

        def validate(self,data):
            print(data)
            if len(data['question_text'])<=10:
                raise serializers.ValidationError('Field with less than ten characters')
            return data




class question_serializer_test(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField('date published')
    
    def validate_question_text(self,value):
            if len(value)<=10:
                raise serializers.ValidationError('Field with less than ten characters')
            return value


