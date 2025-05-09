from rest_framework import serializers
from .models import * 

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Expenses
        fields = [
            'id', 'extension', 'remittance', 
            'stationery', 'altar', 
            'bouquet', 'others'
        ]
    
    def update(self, instance, validated_data): 
        print('In expenses serializer')
        print('validated_data', validated_data)

        # Update instance fields
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        return instance

    # def update(self, validated_data): 
    #     print('In expenses serializer')
    #     print('validated_data', validated_data)
    #     return super().update(self, validated_data)

class AcctStatementSerializer(serializers.ModelSerializer):
    expenses = ExpensesSerializer()

    class Meta: 
        model = AcctStatement
        fields = ['id', 'acf', 'sbc', 'balance', 'expenses']

    def create(self, validated_data): 
        # Extract expenses data
        expenses_data = validated_data.pop('expenses')
        
        # Create new Expenses object
        expenses = Expenses.objects.create(**expenses_data)
        
        # Create AcctStatement with the created Expenses
        acct_statement = AcctStatement.objects.create(expenses=expenses, **validated_data)
        return acct_statement

    def update(self, instance, validated_data):
        # Handle expenses update
        expenses_data = validated_data.pop('expenses', None)
        if expenses_data:
            expenses_serializer = ExpensesSerializer(instance.expenses, data=expenses_data)
            if expenses_serializer.is_valid():
                expenses_serializer.save()
        
        # Update AcctStatement fields
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class AcctAnnouncementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AcctAnnouncement
        fields = [
            'id', 'sbc', 'collection_1', 'collection_2'
        ]


class FinancialRecordSerializer(serializers.ModelSerializer):
    acct_statement = AcctStatementSerializer()
    acct_announcement = AcctAnnouncementSerializer()

    class Meta:
        model = FinancialRecord
        fields = ['id', 'meeting', 'acct_statement', 'acct_announcement']

    def create(self, validated_data):
        # Extract nested data
        acct_statement_data = validated_data.pop('acct_statement')
        acct_announcement_data = validated_data.pop('acct_announcement')

        # Create acct_statement
        acct_statement_serializer = AcctStatementSerializer(data=acct_statement_data)
        acct_statement_serializer.is_valid(raise_exception=True)
        acct_statement = acct_statement_serializer.save()

        # Create acct_announcement
        acct_announcement_serializer = AcctAnnouncementSerializer(data=acct_announcement_data)
        acct_announcement_serializer.is_valid(raise_exception=True)
        acct_announcement = acct_announcement_serializer.save()

        # Create FinancialRecord
        financial_record = FinancialRecord.objects.create(
            acct_statement=acct_statement, 
            acct_announcement=acct_announcement,
            **validated_data
        )
        return financial_record

    
    def update(self, instance, validated_data):
        acct_statement_data = validated_data.pop('acct_statement', None)
        acct_announcement_data = validated_data.pop('acct_announcement', None)

        if acct_statement_data:
            acct_statement_serializer = AcctStatementSerializer(
                instance.acct_statement, 
                data=acct_statement_data
            )
            if acct_statement_serializer.is_valid():
                acct_statement_serializer.save()

        if acct_announcement_data:
            acct_announcement_serializer = AcctAnnouncementSerializer(
                instance.acct_announcement, 
                data=acct_announcement_data
            )
            if acct_announcement_serializer.is_valid():
                acct_announcement_serializer.save()

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance



class FinancialSummarySerializer(serializers.ModelSerializer):
    class Meta: 
        model = FinancialSummary
        fields = [
            'id', 
            'report', 'month_year',
            'acf', 'sbc', 'balance', 'expenses', 
            'report_production', 'balance_at_hand'
        ]

    def update(self, instance, validated_data): 
        print('In financial summary serializer')
        print('validated_data', validated_data)

        # Update instance fields
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        return instance

    # def update(self, validated_data): 
    #     print('In financial summary serializer')
    #     print('validated_data', validated_data)
    #     return super().update(validated_data)