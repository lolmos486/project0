from flask import Blueprint

from exception.customer_not_found import CustomerNotFoundError
from service.account_service import AccountService

ac = Blueprint('account_controller', __name__)

# GET /users/<user_id>/accounts: Get all accounts for a particular customer
# GET /users/<user_id/accounts/<account_id>: Get a particular account that belongs to a particular customer
# POST /users/<user_id/accounts: Add an account for a particular customer
# PUT /users/<user_id>/accounts/<account_id>: Edit a particular account that belongs to a particular customer
# DELETE /users/<user_id>/accounts/<account_id>: Delete a particular to-do that belongs to a particular customer

account_service = AccountService()


@ac.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
        }
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


@ac.route('/customers/<customer_id>/accounts/<account_id>')
def get_account_by_customer_id_and_account_id(customer_id, account_id):
    pass


@ac.route('/customers/<customer_id>/accounts', methods=['POST'])
def add_account_for_customer_by_customer_id(customer_id):
    pass


@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def edit_account_by_customer_id_and_account_id(customer_id, account_id):
    pass


@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_account_by_customer_id_and_account_id(customer_id, account_id):
    pass
