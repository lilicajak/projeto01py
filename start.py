   
class Aluno:
    def __init__(este, nome, idade, matricula):
        este.nome = nome
        este.idade = idade
        este.matricula = matricula
        este.turmas = []

    def __str__(este):
        return f"Aluno: {este.nome}, Matrícula: {este.matricula}"


class Professor:
    def __init__(este, nome, area_ensino, matricula):
        este.nome = nome
        este.area_ensino = area_ensino
        este.matricula = matricula
        este.disciplinas = []

    def __str__(este):
        return f"Professor: {este.nome}, Matrícula: {este.matricula}"


class Disciplina:
    def __init__(este, nome, carga_horaria):
        este.nome = nome
        este.carga_horaria = carga_horaria
        este.professor = None

    def __str__(este):
        professor_nome = este.professor.nome if este.professor else "Não atribuído"
        return f"Disciplina: {este.nome}, Professor: {professor_nome}"


class Turma:
    def __init__(este, nome, ano):
        este.nome = nome
        este.ano = ano
        este.alunos = []
        este.disciplinas = []

    def __str__(este):
        return f"Turma: {este.nome}, Ano: {este.ano}, Alunos: {len(este.alunos)}"


class SistemaEscolar:
    def __init__(este):
        este.alunos = []
        este.professores = []
        este.disciplinas = []
        este.turmas = []

    def cadastrar_aluno(este, nome, idade, matricula):
        aluno = Aluno(nome, idade, matricula)
        # verificar se o aluno inserido tem uma  unica
        for aluno in este.aluno:
         if aluno.append(aluno):
        
            print(f"inexistente: matricula {matricula} matricula em uso ")

    def cadastrar_professor(este, nome, area_ensino, matricula):
        professor = Professor(nome, area_ensino, matricula)
        este.professores.append(professor)

    def cadastrar_disciplina(este, nome, carga_horaria):
        disciplina = Disciplina(nome, carga_horaria)
        este.disciplinas.append(disciplina)

    def cadastrar_turma(este, nome, ano):
        turma = Turma(nome, ano)
        este.turmas.append(turma)

    def listar_alunos(este):
        for aluno in este.alunos:
            print(aluno)

    def listar_professores(este):
        for professor in este.professores:
            print(professor)

    def listar_disciplinas(este):
        for disciplina in este.disciplinas:
            print(disciplina)

    def listar_turmas(este):
        for turma in este.turmas:
            print(turma)


# Exemplo de uso:
sistema = SistemaEscolar()
sistema.cadastrar_aluno("Tim Maia", "17", "B005")
sistema.cadastrar_professor("Roberto Carlos", "Literatura", "L005")
sistema.cadastrar_disciplina("Literatura", 80)
sistema.cadastrar_turma("5º Ano B", 2025)

sistema.listar_alunos()
sistema.listar_professores()
sistema.listar_disciplinas()
sistema.listar_turmas()






      