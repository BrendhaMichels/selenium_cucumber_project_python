from features.pages.google_page import GooglePage
from selenium import webdriver
from features.pages.google_page import GooglePage


@given('I am on the Google homepage')
def step_open_google(context):
    context.driver = webdriver.Chrome()
    context.google_page = GooglePage(context.driver)
    context.google_page.open()

@when('I search for "{term}"')
def step_search_google(context, term):
    context.google_page.search(term)

@then('I should see results related to "{term}"')
def step_verify_google_results(context, term):
    assert term in context.google_page.get_results_title(), f"Expected '{term}' in the page title"
    context.driver.quit()
