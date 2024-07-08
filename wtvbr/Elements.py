
class  Elements_variable ():

    #capabilities
    desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "avd": "testetvsmart",
    "appPackage": "br.tv.watch.watchbrasil.androidtv",
    "appActivity": "tv.accedo.xdk.viki.app.MainActivity",
    "automationName": "UIAutomator2"
    }

    #Login usuário válido
    botao_entrar = '//android.widget.Button[@text="Entrar"]'
    botao_para_acessar_login_e_senha = '//android.widget.Button[@text="Login por email e senha"]'
    login_email = '//android.view.View[@resource-id="App"]/android.view.View/android.view.View[2]/android.widget.EditText[1]'
    login_email_valido = "ramon_leles@hotmail.com"
    login_password = '//android.view.View[@resource-id="App"]/android.view.View/android.view.View[2]/android.widget.EditText[2]'
    login_password_valido = "Leles1990"
    Botao_login = '//android.widget.Button[@text="Entrar"]'
    
    #Login usuário com email inválido
    login_email_valor_invalido = "ramon@hotmail.com"
    
    #selecionando perfil de usuário
    Selecionar_perfil = '(//android.widget.Image[@text="Ícone de perfil"])[1]'
    
    #Selecionando minha lista
    Selecionar_botao_minha_lista = '//android.widget.Button[@text="Ícone do menu Minha lista"]'