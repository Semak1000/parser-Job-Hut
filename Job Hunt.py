import json
from time import sleep
from typing import List, Union

from lxml.html import fromstring, tostring
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def save_json(data: Union[List[dict], dict], path: str):
    """
    :param data: словарь
    :param path: ссылка на место в компьютере
    :return: сохраненный джейсон
    """
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def button_clicker(xpath):
    """

    :param xpath: сслыка на нужный элемент , на который необходимо нажать
    :return: нажатый элемент
    """
    button = driver.find_element(By.XPATH, xpath)
    button.click()




if __name__ == '__main__':

    link = 'https://iirmephi.ru/tutorials/jobhunt/'
    driver = webdriver.Firefox(executable_path=r"C:\Users\мвидео\Desktop\geckodriver.exe")
    driver.get(link)
    res = {}
    for i in range(1,10):
        CV_link = driver.find_element(By.XPATH, f'//div/table/tbody/tr[{i}]/td[5]/a')
        button_clicker(f'//div/table/tbody/tr[{i}]/td[5]/a')
        Name = driver.find_element/html/body/div[1]/div/div/form/div[2]/div/div/div[1]/input
        Skills = [i.text for i in driver.find_elements(by=By.XPATH, value='//body/div[2]/span')]
        Gender = driver.find_element(By.XPATH,'//body/div[2]/p[1]/span')
        Previous_company = driver.find_element(By.XPATH,'//body/div[2]/p[3]/span')
        Desired_salary = driver.find_element(By.XPATH, '//body/div[2]/p[4]')
        res[Name.text] = {'personal_info': Name.text,
                          'Gender': Gender.text,
                          'skills': Skills,
                          'previous_company': Previous_company.text,
                          'desired_salary': Desired_salary.text,
                         }
        driver.back()
    while flag:
        try:
            button_clicker('//a[@href="?page=2"]')
        except NoSuchElementException:
            flag = False
        except Exception as err:
            print(err)
            flag = False
