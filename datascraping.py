

            


def get_html_table_as_df(table_xpath,df_to_save):
   '''This saves a html table as a df.
   Rmb to create an empty df to save the data to before executing this function.
   If the df to save the data to is not empty, this function appends cases'''
   table_html = driver.find_element_by_xpath(table_xpath).get_attribute('outerHTML')
   data_table = pd.read_html(table_html)

   if df_to_save.empty:
         df_to_save = pd.DataFrame(data_table)
   else: df_to_save = df_to_save.append(data_table)
   return df_to_save


def data_gov_table_scrapper(url, table_xpath, number_of_pages_to_scrap,next_button_xpath,df_to_save):
   '''This  scraps a table from data.gov.sg and returns a df.
   Rmb to create an empty df to save the data to before executing this function'''
   driver.get(url)
   time.sleep(2) ###to ensure entire page has been loaded
   for page in range(number_of_pages_to_scrap):
       
        if page == 0:
            df_to_save = get_html_table_as_df(table_xpath,df_to_save)
          

           
        if page == number_of_pages_to_scrap-1:
            df_to_save = get_html_table_as_df(table_xpath,df_to_save)
            
            df_to_save1 =df_to_save[2:] 
         
             
            df_to_save1.to_csv("data.csv")
      
     
            return df_to_save1
            break
        else:
            df_to_save = get_html_table_as_df(table_xpath,df_to_save)
            next_button_xpath += 1 
            next_button_xpath1=str(next_button_xpath)
            next_page = driver.find_element_by_link_text(next_button_xpath1)
           
            
    
            next_page.click()
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv



driver = webdriver.Chrome('/home/victor/sgp19_ds1/chromedriver_linux64/chromedriver')


url ="https://data.gov.sg/dataset/resale-flat-prices/resource/42ff9cfe-abe5-4b54-beda-c88f9bb438ee/view/8481923a-3673-4b4c-b443-5a5bf5127215"
table_xpath = '//*[@id="table-view"]'



next_button_xpath = 1


number_of_pages_to_scrap = 134
df_to_save = pd.DataFrame()

data_gov_table_scrapper(url, table_xpath, number_of_pages_to_scrap,next_button_xpath,df_to_save)          
           
