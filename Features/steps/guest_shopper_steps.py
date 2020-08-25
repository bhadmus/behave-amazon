from behave import *
from Features.pages import page_objects

driver = page_objects.ShopLifeCycle()


use_step_matcher("re")


@given("I open amazon website")
def step_impl(context):

    driver.set_up()


@when("I search for an item")
def step_impl(context):

    driver.search_item()


@step("I select the item")
def step_impl(context):

    driver.pick_item()


@step("I add it to cart")
def step_impl(context):

    # driver.validate_presence_()
    driver.add_to_cart()


@step("I attempt to checkout")
def step_impl(context):

    driver.checkout()


@then("I should be redirected to the Signup or Login page")
def step_impl(context):

    driver.validate_page_redirect()
    driver.tear_down()
