
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip
import os
import googletrans
from PyQt5 import QtWidgets, uic
import sys



class Myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Myapp, self).__init__()
        # 믈래스 맹글기
        uic.loadUi("main.ui",self)
        
        
        self.x1 = "a beautiful portrait of a cute Corgi, beautiful detailed eyes, golden hour, standing on a beach, outdoors, professional award winning portrait photography, Zeiss 150mm f/ 2.8 Hasselblad"
        self.x2 = "Portrait of apex legends thanos, intricate, elegant, glowing lights, highly detailed, digital painting, artstation, glamor pose, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski, artey freytag"
        self.x3 = "Wooden shipwreck of old pirate ship on rocks at sea, dramatic lighting, sun beams, god rays illuminating wreck, dark background, gloomy green sea, fantasy art, painting, concept art, oil painting, brushstrokes"
        self.x4 = "Pirate on ship's crow nest watching for a land, hyperdetailed, hyperrealistic, photorealistic, art by trevor henderson, greg rutkowski, artstation, deviantart"
        self.x5 = "Margot robbie as jack sparrow with a parrot on the shoulder, realistic portrait, 8k resolution, hyper detailed, studio lighting, cinematic"
        self.x6 = "highly detailed creepy forest creature with antlers, stephen bliss, unreal engine, fantasy art by greg rutkowski, loish, rhads, ferdinand knab, makoto shinkai and lois van baarle, ilya kuvshinov, rossdraws, tom bagshaw, global illumination, radiant light, detailed and intricate environment "
        self.x7 ="beautiful digital matte pastel paint sunflowers poppies chillwave greg rutkowski artstation "
        self.x8 = "Liberty Leading the People"
        self.x9 = "Painting of tech priests dining at the last supper, adeptus mechanicus!, cybernetic enhancements attached to their bodies, praise the omnissaiah, zdzislaw beksinski, lewis jones, mattias adolfsson, warhammer 4 0 k!!, cold hue's, warm tone gradient background, concept art, digital painting"
        self.x10= "a korea ancient  ink painting of a tiger"
        self.x11 = "Indiana jones standing in front of an ancient temple, digital painting, extremely detailed, 4 k, intricate, artgerm, by stanley lau"
        self.x12 = "Hungarian movie poster for top gun, painted"
        self.x13 = "The Orient Express flying through interstellar space. The engine is a head of a giant monster. Psychedelic aurora borealis gleaming in the background. A man wearing 1920s clothes clinging to the tender, wearing a gas mask. The umbilical of the gas mask leads to the first car, where two other men hang onto the umbilical."
        self.x14 = "A beautiful wood engraving on paper of an old hunched fisherman, 8 k, frostbite 3 engine, cryengine, dof, trending on artstation, digital art, crepuscular ray"
        self.x15 = "A painting of ghostface in the scream by edvard munch"
        self.x16 = "Hagrid from harry potter as mona lisa, masterpiece digital painting by greg rutkowski, alex grey, artstation, 4k wallpaper"
        self.x17 = "a vase with roses growing on it "
        self.x18 = "A beautifull intricate watercolor painting of lily of the valley, reflexions, verry high details by william turner art, greg rutkowski and alphonse mucha, trending on artstation, very very detailed, masterpiece, - h 7 0 4"
        self.x19 = "Symmetry!! naruto, naruto series, glowing lights!! intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha"
        self.x20 = "Full body elegant portrait of izuku midoriya, gta art, gta cover art, anime, unreal engine 5 art"
        self.x21 = "Luffy artgerm, deviantart, digital painting, dramatic shadowing, 8 k, hd, octane render, perfect"
        self.x22 ="Light yagami, god of the new world, highly detailed, digital art, sharp focus, trending on art station, death note"
        self.x23 ="Still of kirito from sword art online in attack on titan ( 2 0 1 3 ), anime key artwork, highly detailed, trending on pixiv"
        self.x24 = "Attack on titan, masterpiece digital painting by greg rutkowski, alex grey, artstation, 4k wallpaper"
        self.x25 = "Samurai - super - saiyan fantasy art by android jones"
        self.x26 = "One punch man, garou made of stars, animecenter composition, cinematic, trending on artstation, low level, 4k uhd image, -h 960"
        self.x27 ="Genos from one punch man, collaborative painting by greg ruthowski, yoshikata amano, yoji shinkawa, highly detailed, complex, exquisite and beautiful, 4 k, 8 k, artstation"
        self.generate.released.connect(
            lambda: self.Mypredict1())
        
        self.b1.released.connect(
            lambda: self.Mypredict(self.x1,3957780999,7))
        self.b2.released.connect(
            lambda: self.Mypredict(self.x2,4281936,7))
        self.b3.released.connect(
            lambda: self.Mypredict(self.x3,7303382,7))
        self.b4.released.connect(
            lambda: self.Mypredict(self.x4,3420152,7))
        self.b5.released.connect(
            lambda: self.Mypredict(self.x5,4483745,7))
        self.b6.released.connect(
            lambda: self.Mypredict(self.x6,445116670,7))
        self.b7.released.connect(
            lambda: self.Mypredict(self.x7,1841502,7))
        self.b8.released.connect(
            lambda: self.Mypredict(self.x8,2214466,7))
        self.b9.released.connect(
            lambda: self.Mypredict(self.x9,4150418,7))
        self.b10.released.connect(
            lambda: self.Mypredict(self.x10,2359424,7))#호랑이
        self.b11.released.connect(
            lambda: self.Mypredict(self.x11,8301178,7))#인디
        self.b12.released.connect(
            lambda: self.Mypredict(self.x12,1139418,7))#탑건
        self.b13.released.connect(
            lambda: self.Mypredict(self.x13,301575,7))#은하철도
        self.b14.released.connect(
            lambda: self.Mypredict(self.x14,9431335,7))#노인과바다
        self.b15.released.connect(
            lambda: self.Mypredict(self.x15,1814754,7))#절규
        self.b16.released.connect(
            lambda: self.Mypredict(self.x16,6765496,7))#모나리자
        self.b17.released.connect(
            lambda: self.Mypredict(self.x17,5385902,7))#장미
        self.b18.released.connect(
            lambda: self.Mypredict(self.x18,9749793,7))#은방울꽃
        self.b19.released.connect(
            lambda :self.Mypredict2(self.x19,9852741,15,100))
        self.b20.released.connect(
            lambda :self.Mypredict2(self.x20,8378295,15,200))
        self.b21.released.connect(
            lambda :self.Mypredict2(self.x21,5143436,15,100))
        self.b22.released.connect(
            lambda :self.Mypredict2(self.x22,8941920,15,100))
        self.b23.released.connect(
            lambda :self.Mypredict2(self.x23,3859189,15,100))
        self.b24.released.connect(
            lambda :self.Mypredict2(self.x24,1546973,15,100))
        self.b25.released.connect(
            lambda :self.Mypredict2(self.x25,9424403,15,100))
        self.b26.released.connect(
            lambda :self.Mypredict2(self.x26,7568973,15,100))
        self.b27.released.connect(
            lambda :self.Mypredict2(self.x27,7713854,15,100))

        url = "http://wolsv.kro.kr:9000"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        
        
        
        
    def Mypredict1(self):
        textEdit = self.textEdit.toPlainText()
        print(textEdit)
        self.textEdit.setText("")
        translator = googletrans.Translator()

        result1 = translator.translate(textEdit, dest="en", src="auto")


        tag_prompt = self.driver.find_element(By.ID,'prompt')
        tag_coll = self.driver.find_element(By.CSS_SELECTOR ,'#editor-settings > h4')
        tag_prompt.clear()
        tag_prompt.click()
        pyperclip.copy(result1.text)
        tag_prompt.send_keys(Keys.CONTROL, 'v')
        if tag_coll.text == "➕ Image Settings":
            tag_coll.click()
            
        tag_random = self.driver.find_element(By.CSS_SELECTOR,"#random_seed")
        if self.driver.find_element(By.CSS_SELECTOR,"#seed").is_enabled() is True:
            tag_random.click()
            
        tag_plus = self.driver.find_element(By.CSS_SELECTOR,"#use_upscale")
        if self.driver.find_element(By.CSS_SELECTOR,"#upscale_model").is_enabled() is False:
            tag_plus.click()

        if self.radioButton_2.isChecked() is True:
            tag_quality = self.driver.find_element(By.CSS_SELECTOR,"#num_inference_steps")
            tag_quality.clear()
            tag_quality.click()
            pyperclip.copy(30)
            tag_quality.send_keys(Keys.CONTROL, 'v')
        else:
            tag_quality = self.driver.find_element(By.CSS_SELECTOR,"#num_inference_steps")
            tag_quality.clear()
            tag_quality.click()
            pyperclip.copy(500)
            tag_quality.send_keys(Keys.CONTROL, 'v')
            

        login_btn = self.driver.find_element(By.ID,'makeImage')
        login_btn.click()

        
    def Mypredict(self,qtext,seed,scale):
        print(qtext)
        self.textEdit.setText("")

        tag_prompt = self.driver.find_element(By.ID,'prompt')
        tag_coll = self.driver.find_element(By.CSS_SELECTOR ,'#editor-settings > h4')
        tag_prompt.clear()
        print(tag_coll)

        tag_prompt.click()
        pyperclip.copy(qtext)
        tag_prompt.send_keys(Keys.CONTROL, 'v')
        if tag_coll.text == "➕ Image Settings":
            tag_coll.click()

        tag_random = self.driver.find_element(By.CSS_SELECTOR,"#random_seed")
        if self.driver.find_element(By.CSS_SELECTOR,"#seed").is_enabled() is False:
            tag_random.click()
 
        tag_seed = self.driver.find_element(By.ID ,'seed')
        tag_seed.clear()
        tag_seed.click()
        pyperclip.copy(seed)
        tag_seed.send_keys(Keys.CONTROL, 'v')


        tag_seed = self.driver.find_element(By.CSS_SELECTOR ,'#guidance_scale')
        tag_seed.clear()
        tag_seed.click()
        pyperclip.copy(scale)
        tag_seed.send_keys(Keys.CONTROL, 'v')

        tag_plus = self.driver.find_element(By.CSS_SELECTOR,"#use_upscale")
        tag_plus.click()
        tag_plus.click()

        if self.driver.find_element(By.CSS_SELECTOR,"#upscale_model").is_enabled() is False:
            tag_plus.click()

        if self.radioButton_2.isChecked() is True:
            tag_quality = self.driver.find_element(By.CSS_SELECTOR,"#num_inference_steps")
            tag_quality.clear()
            tag_quality.click()
            pyperclip.copy(30)
            tag_quality.send_keys(Keys.CONTROL, 'v')
        else:
            tag_quality = self.driver.find_element(By.CSS_SELECTOR,"#num_inference_steps")
            tag_quality.clear()
            tag_quality.click()
            pyperclip.copy(500)
            tag_quality.send_keys(Keys.CONTROL, 'v')
        

        login_btn = self.driver.find_element(By.ID,'makeImage')
        login_btn.click()

    def Mypredict2(self, qtext, seed, scale,steps):
            print(qtext)
            self.textEdit.setText("")

            tag_prompt = self.driver.find_element(By.ID, 'prompt')
            tag_coll = self.driver.find_element(By.CSS_SELECTOR, '#editor-settings > h4')
            tag_prompt.clear()
            print(tag_coll)

            tag_prompt.click()
            pyperclip.copy(qtext)
            tag_prompt.send_keys(Keys.CONTROL, 'v')
            if tag_coll.text == "➕ Image Settings":
                tag_coll.click()

            tag_random = self.driver.find_element(By.CSS_SELECTOR, "#random_seed")
            if self.driver.find_element(By.CSS_SELECTOR, "#seed").is_enabled() is False:
                tag_random.click()

            tag_seed = self.driver.find_element(By.ID, 'seed')
            tag_seed.clear()
            tag_seed.click()
            pyperclip.copy(seed)
            tag_seed.send_keys(Keys.CONTROL, 'v')

            tag_quality = self.driver.find_element(By.CSS_SELECTOR, "#num_inference_steps")
            tag_quality.clear()
            tag_quality.click()
            pyperclip.copy(steps)
            tag_quality.send_keys(Keys.CONTROL, 'v')

            tag_seed = self.driver.find_element(By.CSS_SELECTOR, '#guidance_scale')
            tag_seed.clear()
            tag_seed.click()
            pyperclip.copy(scale)
            tag_seed.send_keys(Keys.CONTROL, 'v')

            tag_plus = self.driver.find_element(By.CSS_SELECTOR, "#use_upscale")
            tag_plus.click()
            tag_plus.click()

            if self.driver.find_element(By.CSS_SELECTOR, "#upscale_model").is_enabled() is False:
                tag_plus.click()

            login_btn = self.driver.find_element(By.ID, 'makeImage')
            login_btn.click()




    
        
def main():
    print("start main")
    app = QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    
    sys.exit(app.exec_())
    
main()

