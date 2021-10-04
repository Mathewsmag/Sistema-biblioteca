class Livro:
    def __init__(self, titulo, autor, editora, status):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.status = status


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Biblioteca:
    def __init__(self, usuario, livro, data_de_emprestismo, data_de_devolucao):
        self.usuario = usuario
        self.livro = livro
        self.data_de_emprestismo = data_de_emprestismo
        self.data_de_deevolucao = data_de_devolucao


def FazerEmprestimo(usuario, livro, data_de_emprestismo, data_de_devolucao):
    if livro.status == 0:
        print("livro esta alugado")

    try:
        Biblioteca(usuario, livro, data_de_emprestismo, data_de_devolucao)
        livro.status = 0
    except:
        print("Algo deu errado")


livro1 = Livro("Harry Potter", "J. K. Rowling", "Bloomsbury", 1)
usuario1 = Usuario("Matheus", "matheus@gmail.com", "123456")


print(livro1.status)
print("Alugando...")

FazerEmprestimo(usuario1, livro1, "10/10/2021", "15/10/2021")

print(livro1.status)
