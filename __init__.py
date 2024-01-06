import os 
import time 

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




def save_images(folder_name: str, image_name: str, image_content: bytes) -> None:
    """
    Saves the image content to a specified folder with a given name.

    Args:
        folder_name (str): The name of the folder to save the image in.
        image_name (str): The name of the image file.
        image_content (bytes): The content of the image file.

    Returns:
        None: This function does not return anything.
    """
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the image
    with open(os.path.join(folder_name, image_name+'.jpg'), 'wb') as f:
        f.write(image_content)

if __name__ == '__main__':
    options = Options()
    options.headless = False # Set this to False if you want to see the browser window.

    # Create a new Chrome WebDriver instance
    driver = webdriver.Chrome(options=options)
    url = "https://epapervijayavani.in/"

    class_name = "img-section"
    # Navigate to the URL
    driver.get(url)

    elements = driver.find_elements(by = By.CLASS_NAME, value= class_name)

    for element in elements:
        paper_name = element.find_element(By.CLASS_NAME, 'ediname').text
        element.click()
        time.sleep(10)
        driver.window_handles
        driver.switch_to.window(driver.window_handles[1])
        elements_page  = driver.find_elements(By.CLASS_NAME, 'page-image')
        
        for page in elements_page:

            img_l = page.get_attribute('src')
            image_name =page.get_attribute('id')
            img_content = requests.get(img_l).content
            save_images(paper_name, image_name, img_content)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    