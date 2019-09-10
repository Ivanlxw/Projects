from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import os
import shutil

class App():
    def __init__(self,username,password, target_username,
                 path="C:/Users/ivanl/Desktop/Ivan/Education/Python/Python Exercises (non-Github)/webscraping/insta_photos"):
        self.username=username
        self.password = password
        self.target_username = target_username
        self.path = path
        self.error = False
        self.driver=webdriver.Chrome("C:/Users/ivanl/Desktop/Ivan/Education/Python/Python Courses/Python for webscraping/chromedriver")
        self.main_url = 'https://www.instagram.com/?hl=en'
        self.driver.get(self.main_url)        
        
        self.log_in()
        sleep(3)
        self.user_page()
        self.scroll_down()
        
        if not os.path.exists(path):
            os.mkdir(path)
        
        self.download_image()
        self.driver.close()
        
    #Write login function
    def log_in(self,):
        login = self.driver.find_element_by_xpath("//span[@id='react-root']//p[@class='izU2O']/a")
        login.click()
        sleep(3)
        username_input = self.driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(self.username)
        pw_input = self.driver.find_element_by_xpath("//input[@name='password']")
        pw_input.send_keys(self.password)
        pw_input.submit()       #key-in enter. Html must b in form tag

    def user_page(self,):
        try:
            not_now = self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
            not_now.click()
        except Exception:
            self.error = True
            print("can't find the username link...")
        sleep(1)
        searchbar = self.driver.find_element_by_xpath("//input[@class='XTCLo x3qfX ']")
        searchbar.send_keys(self.target_username)
        target_url = 'https://www.instagram.com/' + self.target_username +'/' + '?hl=en'
        self.driver.get(target_url)
        sleep(2)


    def scroll_down(self):
        no_posts = self.driver.find_element_by_xpath("//span[@class='g47SY ']")
        no_posts = str(no_posts.text).replace(',','')
        print(no_posts)
        # self.no_posts = int(no_posts)
        # if self.no_posts > 12:
        #     no_scrolls = int(self.no_posts/12) + 3

        for i in range(3):
            print(i)
            self.driver.execute_script('window.scrollTo(0, 500);')

    def download_image(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')
        self.download_captions(all_images)
        print("Length of all images:", len(all_images))
        for index,image in enumerate(all_images):
            filename = 'image_' + str(index) + '.jpg'
            image_path = self.path + '/'+ filename
            # image.path = os.path.join(self.path, filename)
            link = image['src']
            print("Downloading image ", index)
            response = requests.get(link, stream=True)

            try:
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)     #source, destination
            except Exception as e:
                print(e)
                print("Could not download image number", index)
                print("Image link --->", link)
            print('\n')
    def download_captions(self, images):
        captions_folder_path = os.path.join(self.path, 'captions')
        if not os.path.exists(captions_folder_path):
            os.mkdir(captions_folder_path)
        for index,image in enumerate(images):
            try:
                caption = image['alt']
            except KeyError:
                caption =  "No caption exists"
            file_name = 'caption_' + str(index) + '.txt'
            file_path = os.path.join(captions_folder_path, )
            link = image['src']
            with open(file_path, 'wb') as file:
                file.write('link: '+ str(link) + '\n' + "caption:" + caption.encode())
            
        

if __name__ == "__main__":
    app = App()     #Key in own username, password and target's username
