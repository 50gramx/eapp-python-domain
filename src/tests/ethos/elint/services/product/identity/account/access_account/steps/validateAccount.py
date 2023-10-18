from behave import given, when, then
from your_project.otp import OTPService
from your_project.services import AccessAccountService

# Shared state among steps
context = {}


@given('I am using the AccessAccountService')
def step_impl(context):
    context.service = AccessAccountService()


@given('I provide a valid mobile number that exists in the system')
def step_impl(context):
    context.mobile_number = '1234567890'  # Assuming this number exists in the system
    # You might also fetch a valid number from a test database or mock service.


@given('I provide a mobile number that does not exist in the system')
def step_impl(context):
    context.mobile_number = '0987654321'  # Assuming this number doesn't exist


@given('I provide no mobile number')
def step_impl(context):
    context.mobile_number = None


@given('I provide an invalid mobile number format')
def step_impl(context):
    context.mobile_number = 'invalid-format'


@when('I call the ValidateAccount RPC')
def step_impl(context):
    # Make the call to the RPC method and store the result in the context
    context.response = context.service.validate_account(context.mobile_number)


@then('I should receive a response indicating the account exists')
def step_impl(context):
    assert context.response.status == 'exists'


@then('I should receive an OTP on the mobile number')
def step_impl(context):
    otp_service = OTPService()
    otp_sent = otp_service.is_otp_sent_to(context.mobile_number)
    assert otp_sent


@then('I should get a message saying "OTP Sent to the Mobile Number"')
def step_impl(context):
    assert context.response.message == 'OTP Sent to the Mobile Number'


@then('I should receive a response indicating the account does not exist')
def step_impl(context):
    assert context.response.status == 'does_not_exist'


@then('I should get a message saying "Account doesn\'t exists. Please Create your Account."')
def step_impl(context):
    assert context.response.message == 'Account doesn\'t exists. Please Create your Account.'


@then('I should receive an error response indicating invalid input')
def step_impl(context):
    assert context.response.error == 'invalid_input'
