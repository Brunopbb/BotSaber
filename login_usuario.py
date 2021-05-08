import menuAux
from getpass import getpass

menuAux.menuLogin()


usuario = input("Digite seu usuario: ")
senha = getpass("Digite sua senha: ")



login_saber = {

    "usuario": usuario,
    "senha": senha


}