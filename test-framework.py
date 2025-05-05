class TestCase:
    # Classe base para casos de teste

    def __init__(self, test_method_name):
        # Inicializa o caso de teste com o nome do método de teste
        self.test_method_name = test_method_name

    def run(self):
        # Executa o caso de teste completo
        self.set_up()    # prepara o ambiente para o teste
        test_method = getattr(self, self.test_method_name)  # obtém o método de teste pelo nome
        test_method()    # executa o método de teste 
        self.tear_down() # limpa o ambiente após o teste

    def set_up(self):
        # Método para preparar o ambiente de teste, deve ser sobrescrito se necessário
        pass

    def tear_down(self):
        # Método para limpar o ambiente após o teste, deve ser sobrescrito se necessário
        pass