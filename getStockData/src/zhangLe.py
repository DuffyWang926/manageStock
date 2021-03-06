import os
from time import sleep
import unittest
from appium import webdriver
from src.getPwdData import getPwd
from utils.verify import isExist
from setting import getSetting
# driver.find_element_by_id('android:id/content')
# driver.find_element_by_class_name('android.view.View')
# driver.find_element_by_xpath('//android.view.View[contains(@text, "去认购")]')
# driver.find_element_by_android_uiautomator('new UiSelector().text("(01490.HK)")')
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("4000")')
def buyZhangLe(param):
    code = param['code']
    isCash = param['isCash']
    stockNumVal = param['numVal']
    isFinancingAll = param['isFinancingAll']
    isCashAll = param['isCashAll']
    settingIndex = param['setIndex']
    settingData = getSetting(settingIndex)
    settingData['appPackage'] = 'com.lphtsccft.zlqqt2'
    settingData['appActivity'] = 'com.lphtsccft.zhangle.startup.SplashScreenActivity'
    desired_caps = settingData
    # desired_caps = {
    #     'platformName':'Android',
    #     'platformVersion':'10',
    #     'deviceName':'2214c691',
    #     'appPackage':'com.lphtsccft.zlqqt2',
    #     'noReset':True,
    #     'appActivity':'com.lphtsccft.zhangle.startup.SplashScreenActivity',
    # }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.close_app();            
    sleep(3)
    driver.launch_app(); 
    sleep(6)
    loginZhangeLe(driver)
    driver.find_element_by_id('com.lphtsccft.zlqqt2:id/main_account').click()
    sleep(1)
    path = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]'
    driver.find_element_by_xpath(path).click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().text("打新股")').click()
    sleep(1)

    
    # driver.find_element_by_android_uiautomator('new UiSelector().text("交易")').click()
    # sleep(2)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("新股认购")').click()
    # sleep(1)
    # driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "认购中")]').click()
    # sleep(1)
    # if isExist(driver,'com.tigerbrokers.stock:id/btn_cancel') :
    #     driver.find_element_by_id('com.tigerbrokers.stock:id/btn_cancel').click()
    #     sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("IPO")').click()
    # sleep(1)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("港股")').click()
    # sleep(1)

    # buyPath='//android.widget.TextView[contains(@text,"(' + code + '.HK)")]/parent::*/following-sibling::android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView'
    # driver.find_element_by_xpath(buyPath).click()
    # sleep(1)
    # if not isCash:
    #     driver.find_element_by_id('com.juniorchina.jcstock:id/iv_margin').click()

    # numPath = 'new UiSelector().textContains("%d")'%(stockNum)
    # driver.find_element_by_android_uiautomator(numPath).click()
    # sleep(1)
    driver.quit()
    

def getZhangeLeProperty(param):
   settingIndex = param['setIndex']
   settingData = getSetting(settingIndex)
   settingData['appPackage'] = 'com.lphtsccft.zlqqt2'
   settingData['appActivity'] = 'com.lphtsccft.zhangle.startup.SplashScreenActivity'
   desired_caps = settingData
   driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
   driver.close_app();            
   sleep(3)
   driver.launch_app(); 
   sleep(6)
   loginZhangeLe(driver)
   driver.find_element_by_id('com.lphtsccft.zlqqt2:id/main_account').click()
   sleep(2)
   propertyPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ScrollView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]'
   driver.find_element_by_xpath(propertyPath).click()
   sleep(1)
   pwd = getPwd('zhangLe')['tradePwd']
   pwdId = 'com.lphtsccft.zlqqt2:id/login_et_password'
   driver.find_element_by_id(pwdId).send_keys(pwd)
   driver.find_element_by_id('com.lphtsccft.zlqqt2:id/login_btn_login_account').click()
   sleep(10)
   print(driver.page_source)
   print(driver.contexts)

   
    

def loginZhangeLe(driver):
   closePath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView'
   if isExist(driver, 2,closePath):
      driver.find_element_by_xpath(closePath).click()
      sleep(1)
   
   if isExist(driver, 4,'com.lphtsccft.zlqqt2:id/pending_open'):
       driver.find_element_by_id('com.lphtsccft.zlqqt2:id/pending_open').click()
       sleep(1)