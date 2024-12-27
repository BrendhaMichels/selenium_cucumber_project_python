def before_all(context):
    print("Starting tests...")

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()

def after_all(context):
    print("All tests completed!")
