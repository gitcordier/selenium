from selenium                       import webdriver
from json                           import dump

URL     = 'https://www.parisfintechforum.com/PFF2018/participants'
XPATH   = '//a[@class="resource-specific-url"]'

class Record(list):
    def __init__(self, url):
        '''
            Activates a webdriver with the address 'url'.
        '''
        # You may replace 'Firefox' with your favorite browser.
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Opera()
        #self.driver = webdriver.Safari()
        #……
        self.driver.get(url)
    
    def fetch(self, xpath):
        '''
            Find elements by xpath then append their 'href' values.
        '''
        def append_new_url(x): 
            self.append(x.get_attribute('href'))
        
        list(map(append_new_url, self.driver.find_elements_by_xpath(xpath)))
        
        return self
    #
    def write_results(self):
        '''
            Basically a wrapper for the 'open' method.
        '''
        with open('output_fintech.json', 'w') as file_output:
            dump(self, file_output, ensure_ascii=False, indent=' '*4)
        return self.driver
#

Record(URL).fetch(XPATH).write_results().quit()
