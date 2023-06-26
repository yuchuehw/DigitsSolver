from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from solver import DigitSolver
from collections import defaultdict    
    
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.nytimes.com/games/digits')
WebDriverWait(driver, 10).until(
  EC.element_to_be_clickable((By.ID, 'play-button'))
).click()

WebDriverWait(driver, 10).until(
  EC.element_to_be_clickable((By.ID, 'close-help'))
).click()

for question in range(5):
    buttons = defaultdict(lambda:list())
    solution = []
    skip = []
    
    for x in range(5):
        if x in skip:
            continue
        button = driver.find_element(By.ID, f'number-pos-{x}')
        buttons[button.get_attribute('innerHTML')].append(x)  


      
    target = driver.find_element(
                                  By.ID,
                                  'target'
                                ).get_attribute('innerHTML')
    
    solver = DigitSolver([int(x) for x in
                          list(buttons)],int(target))
    solver.printer_setter(lambda x:solution.append(x))
    solver.solve(True)
    

    for step in solution[0]:
        
        print(step)
        step_list = step.split(' ')
        # for component in step_list[:3]:
        i1,i2 = buttons[step_list[0]].pop(), buttons[step_list[2]].pop()

        print(i1,i2)
        try:
            WebDriverWait(driver, 10).until(
              EC.text_to_be_present_in_element((By.ID, f'number-pos-{i1}'),step_list[0])
            )
        except:
            input("i am stuck")

        try:
            WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.ID, f'number-pos-{i1}'))
            ).click()
        except:
            input("i am stuck")
      

        try:
            WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.ID, step_list[1]))
            ).click()
        except:
            input("i am stuck")
          
        try:
            WebDriverWait(driver, 10).until(
              EC.text_to_be_present_in_element((By.ID, f'number-pos-{i2}'),step_list[2])
            )
        except:
            input("i am stuck")
          
        try:
            WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.ID, f'number-pos-{i2}'))
            ).click()
        except:
            input("i am stuck")
          
        
        buttons[step_list[4]].append(i2)

    if question == 4:
        continue
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "next-puzzle-button"))
    ).click()

input("press enter to close session")
