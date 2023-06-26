from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from solver import DigitSolver
from collections import defaultdict    
from datetime import datetime

# a = new Date('2023-06-23T00:00:00.000Z').getTime()

inject = ""

with open("TimeShift.js","r") as f:
    inject = f.read()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': inject})

LEVEL_0_TIME = 1681084800000
start_level = 0
time_ = LEVEL_0_TIME + start_level * 86400000
level = start_level
while True:
    puzzle_date = datetime.fromtimestamp(time_//1000).strftime("%B %d, %Y")
    print(f"now solving puzzle #{level}({puzzle_date})")
    driver.get('https://www.nytimes.com/games/digits')
    driver.execute_script(f"Date = TimeShift.Date;TimeShift.setTime({time_});")
    try:
      WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'play-button'))
      ).click()
    except:
      input("i got stuck. play button doesn't work!")
    
    for question in range(5):
        buttons = defaultdict(lambda:list())
        solution = []
        
        for x in range(6):
            button = WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.ID, f'number-pos-{x}'))
            )
            buttons[button.get_attribute('innerHTML')].append(x)  
          
        target = driver.find_element(
                                      By.ID,
                                      'target'
                                    ).get_attribute('innerHTML')
        
        solver = DigitSolver([int(x) for x in
                              list(buttons)],int(target))
        solver.printer_setter(lambda x:solution.append(x))
        solver.solve(True)
        print(list(buttons),target)

        for step in solution[0]:
            print(step)
            step_list = step.split(' ')
            i1,i2 = buttons[step_list[0]].pop(), buttons[step_list[2]].pop()
    
            try:
                WebDriverWait(driver, 10).until(
                  EC.element_to_be_clickable((By.ID, f'number-pos-{i1}'))
                ).click()
            except:
                input("i am stuck, i can't click first number")
          
    
            try:
                WebDriverWait(driver, 10).until(
                  EC.element_to_be_clickable((By.ID, step_list[1]))
                ).click()
            except:
                input("i am stuck, i can't click the operator")
              
              
            try:
                WebDriverWait(driver, 10).until(
                  EC.element_to_be_clickable((By.ID, f'number-pos-{i2}'))
                ).click()
            except:
                input("i am stuck, i can't click second number")
              
            
            buttons[step_list[4]].append(i2)
            
            try:
                WebDriverWait(driver, 10).until(
                  EC.text_to_be_present_in_element((By.ID, f'number-pos-{i2}'),step_list[4])
                )
            except:
                input("i am stuck, the number doesn't seems to combine!")
    
        if question == 4:
            try:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "back-to-puzzles-button"))
                ).click()
            except:
                input("i am stuck, the number doesn't combine properly")
            time_ += 86400000
            level += 1
            continue
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "next-puzzle-button"))
            ).click()
        except:
            input("i am stuck, there' no next puzzle button")
