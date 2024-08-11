import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://www.aviasales.ru/about/vacancies/3738675/resume'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = "Талип"
    lastName = "Гарифулин"
    email = 'talip.garifulin@gmail.com'
    portfolio = 'https://github.com/pilat17'
    whereMetTheVacancy = 'Здесь, на сайте Aviasales'
    cover_letter = 'Добрый день! Меня зовут Талип и с этим письмом я откликаюсь на позицию QA Engineer в Авиасейлс. Я считаю, что обладаю нужными компетенциями и квалификацией. У меня есть опыт тестирования веб-приложений ориентированных как на десктоп, так и на мобильные устройства. Также на своих проектах тестировал API и использовал различные инструменты, например Postman. Я очень внимателен к деталям: мной был найден баг в реализации логики, который принёс бы убытки компании на 20% с каждого проданного билета (проект связан с продажей билетов, не поиском). При этом не стою на месте, а продолжаю активно развиваться как в ручном тестировании, так и в автоматизации. /n /n Я давно знаком с Авиасейлс, и поэтому внимательно следил за вакансиями на сайте. Я обожаю культуру компании в отношении сотрудников и клиентов. С большим удовольствием сам использую сервис для поиска дешевых авиабилетов (например он мне помог добраться этим летом домой по самой выгодной цене). И считаю, что смогу вносить вклад в обеспечение качества продукта, для того чтобы клиенты Авиасейлс легко могли организовать поездки по своим делам, не встречая багов. В Сало мне хотелось бы привнести свой нынешний опыт и вырасти, чтобы стать ещё более крутым специалистом.'
    pathToFile = r"C:\Users\talip\QA_GarifulinT.pdf"

    input1 = browser.find_element(By.CSS_SELECTOR, '.resume_form__form>input:nth-of-type(1)')
    input1.send_keys(firstName)
    input2 = browser.find_element(By.CSS_SELECTOR, '.resume_form__form>input:nth-of-type(2)')
    input2.send_keys(lastName)
    input3 = browser.find_element(By.CSS_SELECTOR, '.resume_form__form>input:nth-of-type(3)')
    input3.send_keys(email)
    input4 = browser.find_element(By.CSS_SELECTOR, '.resume_form__form>input:nth-of-type(4)')
    input4.send_keys(portfolio)
    input4 = browser.find_element(By.CSS_SELECTOR, '.resume_form__form>input:nth-of-type(5)')
    input4.send_keys(whereMetTheVacancy)
    input5 = browser.find_element(By.CSS_SELECTOR, '.resume_form__form>textarea')
    input5.send_keys(cover_letter)

    uploadFile = browser.find_element(By.CSS_SELECTOR, '.resume_file>input[type=file]')
    uploadFile.send_keys(pathToFile)
    agreement = browser.find_element(By.CSS_SELECTOR, '.resume_rules__element')
    agreement.click()

    button = browser.find_element(By.CSS_SELECTOR, '.resume_form__button_wrapper>button')
    button.click()
    
finally:
   time.sleep(30)
   browser.quit()
