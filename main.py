from services.GrabService import GrabService
from services.LoginService import LoginService
from services.WrapService import WrapService

if __name__ == '__main__':
    loginService = LoginService()
    try:
        session = loginService.doLogin()

        grabService = GrabService()
        html_content = grabService.getContent(session)

        wrapService = WrapService()
        wrapService.doWrapGames(html_content)

    except Exception as e:
        print('error: %s'%(e))
