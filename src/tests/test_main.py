from src.all_imports import *

# Loading properties and start logging
prop = utils.load_yaml(f"{utils.ROOT_DIR}/data/config.yaml")

# variables
HOST = prop['host']
USER = prop['user']
PASSWORD = prop['password']


# @pytest.mark.skip   # this can be use to skip the test
@pytest.mark.smoke
@pytest.mark.shopping1
def test_shopping(driver):
    """
    Steps:
    Log into the site
    Sort the items (Lowest Price sort)
    Add two or more items to the shopping cart
    Visit the shopping cart
    Assert that the items that you added are in the cart
    Remove an item and then continue shopping
    Add another item
    Checkout
    Assert you are purchasing the correct items
    Assert the total price
    Finish checkout
    """

    # variables
    product1 = "Sauce Labs Backpack"
    product2 = "Sauce Labs Bike Light"
    product3 = "Sauce Labs Bolt T-Shirt"
    firstname = "John"
    lastname = "Doe"
    zipcode = "10010"
    total_amount = 28.06

    # Loading Page Factories
    prod_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Steps
    # Log into the site
    login_to_web(driver, HOST, USER, PASSWORD)
    time.sleep(5)
    prod_page.take_screenshot("AfterLogin")

    # Sort the items (Lowest Price sort)
    prod_page.sort_products_by("Price (low to high)")
    # Add two or more items to the shopping cart
    prod_page.add_to_cart_by_prod_name(product1)
    prod_page.add_to_cart_by_prod_name(product2)
    prod_page.take_screenshot("ItemsAddedToCart")
    time.sleep(2)

    # Visit the shopping cart
    prod_page.open_shopping_cart()
    cart_page.take_screenshot("ShoppingCart")

    # Assert that the items that you added are in the cart
    product_list = cart_page.get_product_name_list()
    assert product1 in product_list
    assert product2 in product_list
    utils.LOG.info(f"Both products are in the cart.")

    # Remove an item and then continue shopping
    cart_page.remove_by_prod_name(product1)
    cart_page.take_screenshot("ItemRemoved")
    time.sleep(2)
    cart_page.click_continue_shopping()
    time.sleep(2)

    # Add another item
    prod_page.take_screenshot("BackToProducts")
    prod_page.add_to_cart_by_prod_name(product3)

    # Checkout
    prod_page.open_shopping_cart()
    cart_page.take_screenshot("UpdatedCart")
    cart_page.click_checkout()

    checkout_page.enter_first_name(firstname)
    checkout_page.enter_last_name(lastname)
    checkout_page.enter_zip_code(zipcode)
    checkout_page.take_screenshot("CheckoutStepOne")
    checkout_page.click_continue()
    time.sleep(2)

    # Assert you are purchasing the correct items
    checkout_page.take_screenshot("CheckoutStepTwo")
    product_list = checkout_page.get_product_name_list()
    assert product2 in product_list
    assert product3 in product_list
    utils.LOG.info(f"Both products are in the cart.")

    # Assert the total price
    utils.LOG.info(f"Asserting the total amount: ")
    # price1 = checkout_page.get_price_by_prod_name(product1)
    # price3 = checkout_page.get_price_by_prod_name(product3)
    # assert price1 + price3 == checkout_page.get_subtotal_amount()
    assert checkout_page.get_total_amount() == total_amount

    # Finish checkout
    driver.execute_script("window.scrollBy(0, 400);")
    checkout_page.click_finish()
    checkout_page.take_screenshot("CheckoutComplete")
    utils.LOG.info(f"********* Shopping test is completed! *********")
