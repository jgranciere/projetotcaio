class UserManager:
    def __init__(self):
        self.lista_usuario = []
        self.lista_senha = []
        self.carregar_usuarios()

    def exibir_menu(self):
        print(15 * '=-')
        print('|      -- BEM - VINDO --     |')
        print(15 * '=-')
        print()
        print('Selecione a opção:')
        print('[1] - Login')
        print('[2] - Cadastrar')
        print('[3] - Esqueci a senha')
        print()

    def realizar_login(self):
        print()
        usuario = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
        if usuario in self.lista_usuario and senha == self.lista_senha[self.lista_usuario.index(usuario)]:
            print(15 * '=-')
            print('- Login feito com sucesso -')
            print(15 * '=-')
        else:
            print('----------------')
            print('| Credenciais inválidas |')
            print('----------------')

    def cadastrar_usuario(self):
        cadastrar_usuario = input('Crie um usuário: ')
        cadastrar_senha = input('Crie uma senha: ')
        self.lista_usuario.append(cadastrar_usuario)
        self.lista_senha.append(cadastrar_senha)
        print(15 * '=-')
        print('-        Conta criada       -')
        print(15 * '=-')

        self.salvar_usuarios()

    def recuperar_senha(self):
        esqueci_senha = input('Digite seu e-mail de cadastro: ')
        print('Uma mensagem foi enviada no seu email')

    def salvar_usuarios(self):
        with open('usuarios.txt', 'w') as arquivo_usuario:
            for usuario, senha in zip(self.lista_usuario, self.lista_senha):
                arquivo_usuario.write(usuario + ';' + senha + '\n')

    def carregar_usuarios(self):
        try:
            with open('usuarios.txt', 'r') as arquivo_usuario:
                for linha in arquivo_usuario:
                    usuario, senha = linha.strip().split(';')
                    self.lista_usuario.append(usuario)
                    self.lista_senha.append(senha)
        except FileNotFoundError:
            pass


def main():
    user_manager = UserManager()
    user_manager.exibir_menu()
    opcao = int(input())

    if opcao == 1:
        user_manager.realizar_login()
    elif opcao == 2:
        user_manager.cadastrar_usuario()
    elif opcao == 3:
        user_manager.recuperar_senha()
    else:
        print('----------------')
        print('| Opção inválida |')
        print('----------------')


if __name__ == '__main__':
    main()
