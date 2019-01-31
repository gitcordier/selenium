from selenium   import webdriver
from json       import dump

URL     = 'https://www.parisfintechforum.com/PFF2018/participants'
XPATH   = '//a[@class="resource-specific-url"]'

class Record(list):
    '''
        Container for relevant data, i.e. the URLs a given webpage enlists.
        They form a set that is identified with 'XPATH', as URL is the webpage
        address.
    '''
    
    def __init__(self, url):
        '''
            Activates a webdriver with the address 'url'.
        '''
        # You may replace 'Firefox' with your favorite browser:
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Opera()
        #self.driver = webdriver.Safari()
        #……
        
        self.driver.get(url)
    
    def fetch(self, xpath):
        '''
            Find elements by xpath then append their 'href' values.
        '''
            
        list(filter(lambda x: 
            self.append(x.get_attribute('href')), 
            self.driver.find_elements_by_xpath(xpath)))
        
        return self
    #
    def write_results(self):
        '''
            Write results into a json file. 
            Returns self.driver, so that a call of 'quit' can be chained.
        '''
        with open('output_fintech.json', 'w') as file_output:
            dump(self, file_output, ensure_ascii=False, indent=' '*4)
        return self.driver
#

Record(URL).fetch(XPATH).write_results().quit()
