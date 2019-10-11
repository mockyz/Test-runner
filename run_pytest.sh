
TESTS=$1
pytest $TESTS --alluredir=my_allure_results
allure serve my_allure_results