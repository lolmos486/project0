from flask import Blueprint, request
from model.customer import Customer
from service.customer_account import CustomerAccount
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError

cc = Blueprint('customer_controller', __name__)

# Instantiate a CustomerAccount object
customer_account = CustomerAccount()


@cc.route('/customers')  # GET /customers  (READ)
def get_all_customers():
    return {
        "customers": customer_account.get_all_customers()  # a list of dictionaries
    }

@cc.route('/test')
def test():
    return "test"


@cc.route('/customers/<customer_id>')  # GET /customers/<customer_id>  (READ)
def get_customer_by_id(customer_id):
    try:
        return customer_account.get_customer_by_id(customer_id)  # dictionary
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


@cc.route('/customers/<customer_id>', methods=['DELETE'])  # Delete customer by id (DELETE)
def delete_customer_by_id(customer_id):
    try:
        customer_account.delete_customer_by_id(customer_id)

        return {
            "message": f"Customer with id {customer_id} deleted successfully"
        }
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


@cc.route('/customers/<customer_id>', methods=['PUT'])  # Update customer by id (UPDATE)
def update_customer_by_id(customer_id):
    try:
        json_dictionary = request.get_json()
        return customer_account.update_customer_by_id(Customer(customer_id, json_dictionary['custom_name'],
                                                               json_dictionary['active']))
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


@cc.route('/customers', methods=['POST'])  # POST /customers    (CREATE)
def add_customer():
    customer_json_dictionary = request.get_json()
    customer_object = Customer(None, customer_json_dictionary['customer_name'], None)
    try:
        return customer_account.add_customer(customer_object), 201  # Dictionary representation of the newly added
        # customer
        # 201 created
    except InvalidParameterError as e:
        return {
                   "message": str(e)
               }, 400
