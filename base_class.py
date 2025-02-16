import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result == get_url
        print(f"Assert url: {get_url}")

    def assert_word(self, word, result):
        value_word = word.text
        assert result == value_word
        print(f"Assert word: {value_word}")

    def get_screenshot(self):
        now_time = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        self.driver.save_screenshot(f".\\screen\\{now_time}.png")