from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

@given(u'que acesso a loja virtual Nox Joias')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://vhsys.net/noxjoias")


@when(u'selecionado o produto "{nome_produto}"')
def step_impl(context,nome_produto):
    element = context.driver.find_element(By.NAME, 's')
    element.send_keys(nome_produto)
    element.send_keys(Keys.ENTER)
    time.sleep(2)
    context.driver.find_element(By.PARTIAL_LINK_TEXT, nome_produto).click()


@when(u'selecionado o genero "{categoria}"')
def step_impl(context, categoria):
    element = context.driver.find_element(By.ID, 'grade_9569')
    element.send_keys(categoria)


@when(u'clicar no botão "Comprar"')
def step_impl(context):
    context.driver.find_element(By.ID, 'btn-comprar').click()


@then(u'o valor total do carrinho de compras deve ser R$ "{valor}",00')
def step_impl(context, valor):
    time.sleep(3)
    element = context.driver.find_element(By.ID, 'valor_produtos').get_attribute('value')
    assert element == valor