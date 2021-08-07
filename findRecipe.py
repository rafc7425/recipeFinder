
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class SearchRecipe(unittest.TestCase):
    def setUp(self):
        #this test will run in chrome
        self.driver = webdriver.Chrome()
        #it will wait 3 secons to open the page
        self.driver.implicitly_wait(3000)
        #base url
        self.base_url = "https://www.allrecipes.com/"
       
    
    def search_for_recipe(self):
        #Navigate to all recipes.com
        driver = self.driver
        driver.get(self.base_url);
       #click on search bar and search pizza 
        driver.find_element_by_id("search-block").click()
        driver.find_element_by_id("search-block").clear()
        driver.find_element_by_id("search-block").send_keys("pizza")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search'])[3]/following::button[1]").click()
        #add chesse as ingredient
        driver.find_element_by_xpath("//div[@id='faceted-search-filters']/div/div[2]/div[2]/div[2]/div/div[2]/input").click()
        driver.find_element_by_xpath("//div[@id='faceted-search-filters']/div/div[2]/div[2]/div[2]/div/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='faceted-search-filters']/div/div[2]/div[2]/div[2]/div/div[2]/input").send_keys("cheesse")
        driver.find_element_by_css_selector("div.faceted-search-filters-available-item-body > div.faceted-search-filters-available-item-filter-choices-wrapper.include-option > div.faceted-search-filters-available-item-filter-choices-input-wrapper > span.icon.include-option.js-activate > span.icon.icon-add-circle.default-icon.color-navigation > svg > path").click()
        driver.find_element_by_xpath("//div[@id='faceted-search-filters']/div/div[2]/div[2]/div[2]/div[2]/div[2]/input").click()
        driver.find_element_by_xpath("//div[@id='faceted-search-filters']/div/div[2]/div[2]/div[2]/div[2]/div[2]/input").clear()
        #remove tomato ingredient
        driver.find_element_by_xpath("//div[@id='faceted-search-filters']/div/div[2]/div[2]/div[2]/div[2]/div[2]/input").send_keys("tomato")
        driver.find_element_by_css_selector("div.faceted-search-filters-available-item-body > div.faceted-search-filters-available-item-filter-choices-wrapper.exclude-option > div.faceted-search-filters-available-item-filter-choices-input-wrapper > span.icon.exclude-option.js-activate > span.icon.icon-remove-circle.default-icon.color-navigation > svg > path").click()
        driver.find_element_by_id("faceted-search-filters-update-results").click()
        driver.find_element_by_css_selector("label.faceted-search-filters-available-item-select-label.option.include-option.option-checked > a.filter-action.close-icon > svg > path").click()
        # and click on search button
        driver.find_element_by_id("faceted-search-filters-update-results").click()
       
