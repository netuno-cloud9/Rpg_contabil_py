import random
import ipywidgets as widgets
import urllib.parse
import urllib.request
from IPython.display import display, Image, clear_output
import time



class FinancialAnalyst:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.cash = 0

    def interpret_reports(self, game):
        print(f"Bem-vindo, {self.name}! Vamos participar de um torneio par arrecadar fundos para {self.company}.")
        print("Seu objetivo é construir uma empresa unicórnio tomando decisões financeiras estratégicas.")
        print("Você responderá perguntas financeiras para ganhar dinheiro e melhorar a saúde financeira da sua empresa.")
        print("Você começa com R$ 1.000 em caixa.")
        print("Se seu saldo de caixa ficar negativo, sua empresa quebrará!\n")

        time.sleep(1)

        initial_cash = 1000
        self.cash = initial_cash

        max_questions = 15
        time_limit = 20

        for question_count in range(1, max_questions + 1):
            print(f"Pergunta {question_count}/{max_questions}")
            print(f"Saldo de Caixa Atual: R$ {self.cash:.2f}")

            if not game.has_questions_left():
                print("Fim do jogo!")
                break

            question, options, correct_index, image_url = game.load_question()
            self.display_question(question, options, image_url)

            user_choice = self.get_user_choice(options)

            if user_choice == correct_index:
                self.cash += 200
                print("Resposta correta! Você ganhou R$ 200.!!\n")
            else:
                self.cash -= 300
                print("Resposta incorreta. Você perdeu R$ 300 !!.\n")
                print(f"Saldo de Caixa Atual: R$ {self.cash:.2f}")

        if self.cash >= 1000:
            print("\nParabéns! Você construiu uma empresa unicórnio!")
        else:
            print("\nDesculpe, sua empresa faliu. Boa sorte na próxima!")

    def display_question(self, question, options, image_url):
        if image_url:
            display(Image(url=image_url))
        print(question)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        print()

    def get_user_choice(self, options):
        while True:
            try:
                choice = int(input("Escolha a opção correta: ")) - 1
                if choice in range(len(options)):
                    return choice
                else:
                    print("Opção inválida. Por favor, escolha novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira o número da opção.")

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0

    def has_questions_left(self):
        return self.current_question < len(self.questions)

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.current_question += 1
            return question_data["question"], question_data["options"], question_data["correct_index"], question_data.get("image_url", "")
        else:
            return "", [], -1, ""

def show_instructions():

    print("********************************************")
    print("            Instruções do Jogo              ")
    print("********************************************\n")
    print("Você é um ambicioso empreendedor que lidera a sua empresa,")
    print("uma startup promissora prestes a se tornar o próximo unicórnio nos negócios.")
    print("No entanto, a empresa enfrenta uma escassez de capital para suas operações e expansão.")
    print("Seu objetivo é representar a empresa em um prestigiado torneio de inteligência conhecido como 'O Torneio de Inteligência'.")
    print("Neste torneio, você responderá a uma série de desafios financeiros para ganhar investimentos valiosos para a empresa.")
    print("Você começa com um capital inicial de R$ 1.000 em caixa.")
    print("Cada resposta correta adiciona R$ 200 ao seu caixa, e cada resposta errada ou tempo esgotado deduz R$ 300.")
    print("Se você conseguir acumular R$ 1.000 ou mais até o final do torneio, a sua empresa estará segura e pronta para crescer e se tornar o próximo unicórnio dos negócios.")
    print("\n********************************************")
    input("Pressione Enter para voltar ao menu principal.")



def main_menu():
    while True:
        # ASCII art title
        title_ascii = r"""


  ____  ____   ____    ____            _    __  _     _ _
  |  _ \|  _ \ / ___|  / ___|___  _ __ | |_ /_/_| |__ (_) |
  | |_) | |_) | |  _  | |   / _ \| '_ \| __/ _` | '_ \| | |
  |  _ <|  __/| |_| | | |__| (_) | | | | || (_| | |_) | | |
  |_| \_\_|    \____|  \____\___/|_| |_|\__\__,_|_.__/|_|_|


        """
        print(title_ascii)
        print("***************************************")
        print("*    Bem-vindo ao torneio de análise  *")
        print("*              Financeira             *")
        print("***************************************")
        print()
        print("1. Iniciar Jogo")
        print("2. Instruções")
        print("3. Sair")
        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            name = input("Digite seu nome: ")
            company = input("Digite o nome da empresa: ")
            analyst = FinancialAnalyst(name, company)
            game = QuizGame(quiz_questions)
            analyst.interpret_reports(game)
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            print("Obrigado por jogar. Adeus!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Rest of your code remains the same



# Exemplo de perguntas (perguntas adicionadas)
quiz_questions = [
    {
        "question": "As principais funções da Contabilidade são:",
        "options": [
            "A) Registrar, organizar, demonstrar, analisar e acompanhar as modificações do patrimônio em virtude da atividade econômica ou social que a empresa exerce no contexto econômico.",
            "B) Registrar, organizar, demonstrar, analisar e acompanhar as modificações do patrimônio em virtude da atividade econômica e não social da empresa que exerce no contexto econômico.",
            "C) Organizar faz parte da contabilidade pois tendo uma boa organização tudo flui dentro da empresa.",
            "D) Na contabilidade não existe funções."
        ],
        "correct_index": 0
    },
    {
        "question": "O que é balanço patrimonial?",
        "options": [
            "A) O balanço patrimonial é um relatório financeiro porém, não são todas as empresas que usam, apenas as multinacionais.",
            "B) O balanço patrimonial tem que ser feito a cada dois (02) anos.",
            "C) O balanço patrimonial é uma ferramenta dispensável por todas as empresas.",
            "D) O balanço patrimonial é um relatório financeiro que mostra a situação financeira de uma empresa em um determinado momento, apresentando seus ativos, passivos e patrimônio líquido."
        ],
        "correct_index": 3
    },
    {
        "question": "Qual é o princípio contábil que estabelece que as informações contábeis devem ser registradas separadamente das informações pessoais dos proprietários?",
        "options": [
            "A) Princípio da entidade",
            "B) Princípio da competência",
            "C) Princípio da materialidade",
            "D) Princípio da continuidade"
        ],
        "correct_index": 0
    },
    {
        "question": "Verdadeiro ou Falso: O balanço patrimonial é um relatório financeiro que mostra a situação financeira de uma empresa em um determinado momento, apresentando seus ativos, passivos e patrimônio líquido.",
        "options": ["Verdadeiro", "Falso"],
        "correct_index": 0
    },
    {
        "question": "Verdadeiro ou Falso: O princípio contábil da competência estabelece que as receitas e os gastos devem ser registrados no momento em que são realizados, independentemente do momento em que o dinheiro é recebido ou pago.",
        "options": ["Verdadeiro", "Falso"],
        "correct_index": 0
    },
    {
        "question": "Qual é o registro contábil utilizado para registrar a venda de produtos ou serviços?",
        "options": [
            "A) Débito em Contas a Pagar, Crédito em Contas a Receber.",
            "B) Débito em Contas de Receitas, Crédito em Contas de Despesas.",
            "C) Débito em Contas de Receitas, Crédito em Contas de Ativos.",
            "D) Débito em Contas de Ativos, Crédito em Contas de Passivos."
        ],
        "correct_index": 2
    },
    {
        "question": "Qual é a fórmula para calcular o lucro líquido?",
        "options": [
            "A) Ativos – Passivos.",
            "B) Receitas – Despesas",
            "C) Ativo + Despesas",
            "D) Receitas – Passivos"
        ],
        "correct_index": 1
    },
    {
        "question": "Qual é o princípio contábil que estabelece que as receitas e os gastos devem ser registrados no momento em que são realizados, independentemente do momento em que o dinheiro é recebido ou pago.",
        "options": [
            "A) Princípio da Entidade",
            "B) Princípio da competência",
            "C) Princípio da materialidade",
            "D) Princípio da continuidade"
        ],
        "correct_index": 1
    },
    {
        "question": "Qual é o registro contábil utilizado para registrar o pagamento de despesas operacionais?",
        "options": [
            "A) Débito em Contas de Receitas, Crédito em Contas de Ativos",
            "B) Débito em Contas de Despesas, Crédito em Contas de Ativos",
            "C) Débito em Contas de Despesas, Crédito em Contas de Receitas",
            "D) Débito em Contas de Despesas, Crédito em Contas de Passivos"
        ],
        "correct_index": 1
    },
    {
        "question": "Qual é o princípio contábil que estabelece que as informações contábeis devem ser consistentes ao longo do tempo, permitindo comparações entre diferentes períodos contábeis?",
        "options": [
            "A) Princípio da Entidade",
            "B) Princípio da Competência",
            "C) Princípio da Consistência",
            "D) Princípio da Materialidade"
        ],
        "correct_index": 2
    },
    {
        "question": "O que significa qualificação dos ativos em um balanço patrimonial?",
        "options": [
            "A) Refere-se à quantidade de ativos que a empresa possui.",
            "B) Refere-se à avaliação dos ativos em termos de sua qualidade e utilidade.",
            "C) Refere-se à classificação dos ativos como concorrentes e não concorrentes.",
            "D) Refere-se ao valor monetário."
        ],
        "correct_index": 1
    }
]
random.shuffle(quiz_questions)

# Inicie o jogo
main_menu()
