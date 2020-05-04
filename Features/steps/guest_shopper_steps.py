from behave import *
from Features.pages import page_objects

driver = page_objects.ShopLifeCycle()


use_step_matcher("re")


@given("I open amazon website")
def step_impl(context):
    """
    :type context: behave.runner.Context

    """
    driver.set_up()



@when("I search for an item")
def step_impl(context):
    """
    :type context: behave.runner.Context

    """
    driver.search_item()



@step("I select the item")
def step_impl(context):
    """
    :type context: behave.runner.Context

    """
    driver.pick_item()
    # raise NotImplementedError(u'STEP: And I select the item')


@step("I add it to cart")
def step_impl(context):
    """
    :type context: behave.runner.Context

    """
    driver.validate_presence_()
    driver.add_to_cart()
    # raise NotImplementedError(u'STEP: And I add it to cart')


@step("I attempt to checkout")
def step_impl(context):
    """
    :type context: behave.runner.Context

    """
    driver.checkout()
    # raise NotImplementedError(u'STEP: And I attempt to checkout')


@then("I should be redirected to the Signup or Login page")
def step_impl(context):
    """
    :type context: behave.runner.Context

    """
    driver.validate_page_redirect()
    # raise NotImplementedError(u'STEP: Then I should be redirected to the Signup or Login page')