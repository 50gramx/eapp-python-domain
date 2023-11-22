from behave import given, when, then
from ethos.elint.services.product.identity.account.access_account_pb2 import ValidateAccountRequest
from gramx.fifty.zero.ethos.identity.multiverse.core.entity.account.capabilities.access.service import \
    AccessAccountService

# Shared state among steps
context = {}


@given('I am using the AccessAccountService')
def step_impl(context):
    context.service = AccessAccountService()


@given('I provide a valid mobile number that exists in the system')
def step_impl(context):
    context.account_mobile_number = '1234567890'  # Assuming this number exists in the system
    # You might also fetch a valid number from a test database or mock service.


@given('I provide a mobile number that does not exist in the system')
def step_impl(context):
    context.account_mobile_number = '0987654321'  # Assuming this number doesn't exist


@given('I provide no mobile number')
def step_impl(context):
    context.account_mobile_number = None


@given('I provide an invalid mobile number format')
def step_impl(context):
    context.account_mobile_number = 'invalid-format'


@when('I call the ValidateAccount RPC')
def step_impl(context):
    # Make the call to the RPC method and store the result in the context
    request = ValidateAccountRequest(
        account_mobile_number=context.account_mobile_number
    )
    context.response = context.service.validate_account(request)


@then('I should receive a response indicating the account exists')
def step_impl(context):
    assert context.response.account_exists is True


@then('I should receive an OTP on the mobile number')
def step_impl(context):
    assert context.response.code_sent_at is not None


@then('I should get a message saying "OTP Sent to the Mobile Number"')
def step_impl(context):
    assert context.response.validate_account_message == 'OTP Sent to the Mobile Number'


@then('I should receive a response indicating the account does not exist')
def step_impl(context):
    assert context.response.account_exists is False


@then('I should get a message saying "Account doesn\'t exists. Please Create your Account."')
def step_impl(context):
    assert context.response.validate_account_message == "Account doesn't exists. Please Create your Account."


@then('I should receive an error response indicating invalid input')
def step_impl(context):
    assert context.response.validate_account_message == 'Invalid mobile number. Please provide a valid mobile number.'
