from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pytest

# setup
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
driver.implicitly_wait(5)

# The Add and Remove Elements Test
def test_add_remove_elements():
    driver.find_element(by.XPATH,"//a[.='Add/Remove Elements']").click()
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((by.XPATH,"//button[.='Add Element']"))).click()
    driver.find_element(by.XPATH,"//button[@class='added-manually']").click()

# The Basic Authentication Test
def test_basic_auth():
    driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    wait = WebDriverWait(driver,3)
    Title = driver.find_element(by.CSS_SELECTOR,"p").text
    assert Title=="Congratulations! You must have the proper credentials."

# The Checkboxes Test
def test_checkboxes():
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(by.XPATH,"//a[.='Checkboxes']").click()
    # Random greatester otomesyen
    driver.find_element(by.XPATH,"//input[1]").click()
    driver.find_element(by.XPATH,"//input[2]").click()

# The Context Menu Test
def test_context_menu():
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(by.XPATH,"//a[.='Context Menu']").click()
    box = driver.find_element(by.ID,"hot-spot")
    ActionChains(driver).context_click(box).perform()
    driver.switch_to.alert.accept()

# The Drag and Drop test
def test_drag_and_drop():
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(by.XPATH,"//a[.='Drag and Drop']").click()
    source = driver.find_element(by.ID,"column-a")
    target = driver.find_element(by.ID,"column-b")
    action = ActionChains(driver)
    # Random greatester otomesyen
    action.click_and_hold(source).move_to_element(target).release().perform()

# The Dropdown List Test
def test_dropdown_list():
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(by.XPATH,"//a[.='Dropdown']").click()
    dropdown = driver.find_element(by.XPATH,"//select[@id='dropdown']")
    select = Select(dropdown)
    select.select_by_visible_text("Option 1")
    select.select_by_value("2")
    select.select_by_index(1)

# The Dynamic Control 1
def test_dynamic_control():
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(by.XPATH,"//a[.='Dynamic Controls']").click()
    chbox = driver.find_element(by.XPATH,"//div[@id='checkbox']/input[1]")
    remove = driver.find_element(by.XPATH,"//button[.='Remove']")
    chbox.click()
    remove.click()
    WebDriverWait(driver,7).until(EC.visibility_of_element_located((by.ID,"message")))
    add = driver.find_element(by.XPATH,"//button[.='Add']")
    add.click()
    # Random greatester otomesyen
    WebDriverWait(driver,7).until(EC.visibility_of_element_located((by.ID,"message")))
    driver.find_element(by.ID,"checkbox").click()
    remove.click()
    WebDriverWait(driver,7).until(EC.visibility_of_element_located((by.XPATH,"//form[@id='checkbox-example']/div[contains(.,'A checkbox')]")))

# The Dynaic Control 2
def test_dynamic_control2():
    driver.get("http://the-internet.herokuapp.com/dynamic_controls")
    enable = driver.find_element(by.XPATH,"//button[.='Enable']")
    enable.click()
    # Random greatester otomesyen
    WebDriverWait(driver,7).until(EC.visibility_of_element_located((by.XPATH,"//p[@id='message']")))
    driver.find_element(by.CSS_SELECTOR,"input").send_keys("Gatotkoco")   

# The Dynamic Loading 1
def test_dynamic_loading1():
    driver.get("http://the-internet.herokuapp.com/dynamic_loading")
    driver.find_element(by.XPATH,"//a[.='Example 1: Element on page that is hidden']").click()
    driver.find_element(by.XPATH,"//button[.='Start']").click()
    WebDriverWait(driver,7).until(EC.visibility_of_element_located((by.XPATH,"//h4[.='Hello World!']")))
    proof = driver.find_element(by.XPATH,"//h4[.='Hello World!']").text
    assert proof=="Hello World!"

# The Dynamic Loading 2
def test_dynamic_loading2():
    driver.get("http://the-internet.herokuapp.com/dynamic_loading")
    # Random greatester otomesyen
    driver.find_element(by.XPATH,"//a[.='Example 2: Element rendered after the fact']").click()
    driver.find_element(by.XPATH,"//button[.='Start']").click()
    WebDriverWait(driver,7).until(EC.visibility_of_element_located((by.XPATH,"//h4[.='Hello World!']")))
    proof = driver.find_element(by.XPATH,"//h4[.='Hello World!']").text
    assert proof=="Hello World!"

# The Entry Ad
def test_entry_ad():
    try:
        driver.get("http://the-internet.herokuapp.com/entry_ad")
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((by.XPATH,"//p[.='Close']"))).click()
        # Random greatester otomesyen
    except TimeoutException:
        driver.find_element(by.ID,"restart-ad").click()
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((by.XPATH,"//p[.='Close']"))).click()

# The Forgot Password
def test_forgot_password():
    driver.get("http://the-internet.herokuapp.com/forgot_password")
    driver.find_element(by.ID,"email").send_keys("Gatotkoco@gmail.com")
    driver.find_element(by.XPATH,"//i[@class='icon-2x icon-signin']").click()
    text = driver.find_element(by.XPATH,"//h1[.='Internal Server Error']").text
    assert text=="Internal Server Error"

# The Login
def test_invalid_login():
    driver.get("http://the-internet.herokuapp.com/login")
    driver.find_element(by.ID,"username").send_keys("tomsmith")
    driver.find_element(by.ID,"password").send_keys("SuperIncorrectPassword!")
    driver.find_element(by.XPATH,"//i[@class='fa fa-2x fa-sign-in']").click()
    invalid = WebDriverWait(driver,5).until(EC.visibility_of_element_located((by.XPATH,"//div[@id='flash']"))).text
    # Random greatester otomesyen
    assert invalid=="Your password is invalid!\n×"

def test_valid_login():
    driver.get("http://the-internet.herokuapp.com/login")
    driver.find_element(by.ID,"username").send_keys("tomsmith")
    driver.find_element(by.ID,"password").send_keys("SuperSecretPassword!")
    driver.find_element(by.XPATH,"//i[@class='fa fa-2x fa-sign-in']").click()
    success = driver.find_element(by.XPATH,"//div[@id='flash']").text
    assert success=="You logged into a secure area!\n×"
    driver.find_element(by.XPATH,"//i[@class='icon-2x icon-signout']").click()

    logout = driver.find_element(by.XPATH,"//div[@id='flash']").text
    assert logout=="You logged out of the secure area!\n×"

# The Hover
def test_hover1():
    driver.get("http://the-internet.herokuapp.com/hovers")
    action = ActionChains(driver)
    pro1 = driver.find_element(by.XPATH,"//div[@class='example']/div[1]/img[@alt='User Avatar']")
    action.move_to_element(pro1).perform()
    driver.find_element(by.XPATH,"//a[@href='/users/1']").click()
    text1 = driver.find_element(by.CSS_SELECTOR,"h1").text
    assert text1=="Not Found"

def test_hover2():   
    driver.get("http://the-internet.herokuapp.com/hovers")
    action = ActionChains(driver)
    pro2 = driver.find_element(by.XPATH,"//div[@class='example']/div[2]/img[@alt='User Avatar']")
    # Random greatester otomesyen
    action.move_to_element(pro2).perform()
    driver.find_element(by.XPATH,"//a[@href='/users/2']").click()
    text2 = driver.find_element(by.CSS_SELECTOR,"h1").text
    assert text2=="Not Found"
    
def test_hover3():
    driver.get("http://the-internet.herokuapp.com/hovers")
    action = ActionChains(driver)
    pro3 = driver.find_element(by.XPATH,"//div[@class='example']/div[3]/img[@alt='User Avatar']")
    action.move_to_element(pro3).perform()
    # Random greatester otomesyen
    driver.find_element(by.XPATH,"//a[@href='/users/3']").click()
    text3 = driver.find_element(by.CSS_SELECTOR,"h1").text
    assert text3=="Not Found"
