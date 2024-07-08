from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from AssertsByGroups import*
from AssertDefinitions_Pipeline import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def teste_login_usuario_invalido(environment_app):
        
        #Start_test

        #login com email e senha do usuário não credenciado
        Login_user_invalido()

        #Quit_test
        quit_app()

        #End_test