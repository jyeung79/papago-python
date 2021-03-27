from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()

driver.get('https://papago.naver.com/')

src_file = './subs/src.srt'
target_file = './subs/target.srt'

try:
  translate_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/section/div/div[1]/div[1]/div/div[3]/label/textarea')))
  translate_btn = driver.find_element_by_id('btnTranslate')

  line_count = len(open(src_file).readlines())
  print(line_count)
  target = open(target_file, 'w')

  with open(src_file) as f:
    lines = f.readlines()
    for index, line in enumerate(lines, start=1):
      translate_text.send_keys(line + Keys.ENTER)
      if index % 100 == 0 or index == line_count + 1:
        translate_btn.click()
        #translated_textbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/section/div/div[1]/div[2]/div/div[5]/div')))
        translated_textbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'txtTarget')))
        driver.implicitly_wait(3)
        translated_text = translated_textbox.find_elements_by_xpath(".//*")
        
        ending_tag = False
        for elem in translated_text:
          if elem.tag_name != 'br':
            #print(elem.tag_name + elem.text)
            if ending_tag == True:
              ending_tag = False
            else:
              #print(elem.tag_name + elem.text)
              target.write(elem.text+'\n')
              ending_tag = True
        
        clear_text_btn = driver.find_element_by_xpath('/html/body/div/div/div[2]/section/div/div[1]/div[1]/div/div[3]/button')
        clear_text_btn.click()

finally:
  driver.quit()
