from django import forms
from loans.models import Loan, Message


class LoanForm(forms.ModelForm):
	

	class Meta:
		model = Loan

		fields = (
			'name',
			'personid',
			'civil_status',
			'address',
			'province',
			'phone',
			'phone_home',
			'phone_office',
			'email',
			'work_place',
			'work_time',
			'income_range',
			'other_income',
			'loan_reason',
			'loan_amount',
			'loan_time',
			)

class MessageForm(forms.ModelForm):
	
	class Meta:
		model = Message

		fields = (
			'p_name',
			'p_email',
			'p_phone',
			'p_message',
			)
