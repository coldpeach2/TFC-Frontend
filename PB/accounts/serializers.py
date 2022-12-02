from rest_framework import serializers
from accounts.models import User, UserSubscription, SubscriptionPlan, PaymentHistory
from datetime import datetime, timedelta
from django.utils.dateparse import parse_datetime
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'phone_num', 'password', 'password2']
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
    }

    def validate(self, data: dict) -> dict:
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords must match.'})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Email is already in use.'})
        return data

    def save(self, **kwargs):
        user = User(first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'],
                    email=self.validated_data['email'], phone_num=self.validated_data['phone_num'], avatar=self.validated_data['avatar'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user

class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone_num')


class ProfileUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email', 'avatar', 'phone_num')
            
        def update(self, instance, validated_data):
            for key, value in validated_data.items():
                if value:
                    setattr(instance, key, value)
            instance.save()
            return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(label="password", style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid email or password", code='authorization')
        else:
            raise serializers.ValidationError("Email and password are required", code='authorization')
        attrs['user'] = user
        return attrs


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class ActivateUserSubscriptionSerializer(serializers.ModelSerializer):
    subscription_plan = SubscriptionPlanSerializer()
    class Meta:
        model = UserSubscription
        fields = ('subscription_plan', 'card_info')
        
    def validate(self, attrs):
        if self.context['request'].method == 'PUT':
            return attrs
        else:
            user = self.context['request'].user
            if UserSubscription.objects.filter(user=user).exists():
                sub = UserSubscription.objects.get(user=user).subscription_plan
                if sub.subscription_choices != 'Free':
                    raise serializers.ValidationError("You already have an active subscription!")
        return attrs
        
    def create(self, validated_data): 
        sub_choice = self.validated_data['subscription_plan']
        if sub_choice['subscription_choices'] == 'Free':
            raise serializers.ValidationError({"subscription_choices": "You already have a free account!"})
        else:
            sub_plan =  SubscriptionPlan.objects.create(subscription_choices = sub_choice)
            user_subscription = UserSubscription.objects.create(user=self.context['request'].user, subscription_plan=sub_plan, card_info=validated_data['card_info'])
            user_subscription.activate
            self.make_first_payment(user_subscription)
            return user_subscription

    def make_first_payment(self, object):
        object.make_payment()
        return object.amount_paid

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            print(instance.subscription_plan.subscription_choices)
            if key == 'card_info':
                setattr(instance, key, value)
            if key == 'subscription_plan' and value:
                if value['subscription_choices'] == 'Free':
                    instance.subscription_plan =  SubscriptionPlan.objects.create(subscription_choices = 'Free')
                    instance.deactivate
                else:
                    instance.subscription_plan = SubscriptionPlan.objects.create(subscription_choices = value['subscription_choices'])
                    instance.activate
                    self.make_first_payment(instance)
        instance.save()
        return instance    

class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'



