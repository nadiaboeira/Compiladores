from sly import Lexer

class analisadorLexico(Lexer):

    tokens = {ID, NUM, IF, ELSE, INT, VOID, RETURN, WHILE, SOMA, SUBTRACAO, MULTIPLICACAO, DIVISAO, MENOR, MENOR_IGUAL, MAIOR, MAIOR_IGUAL, IGUAL, DIFERENTE, ATRIBUICAO}
    literals = {'(', ')', '[', ']', '{', '}', ';', ',', '/*', '*/'}

    ignore = ' \t'
    ignore_coment = '[/][*][^*]*[*]+([^*/][^*]*[*]+)*[/]'

    # Expressões Regulares para os tokens
    ID = r'[a-zA-Z][a-zA-Z]*'
    NUM = r'\d+'
    SOMA = r'\+'
    SUBTRACAO = r'-'
    MULTIPLICACAO = r'\*'
    DIVISAO = r'/'
    MENOR = r'<'
    MENOR_IGUAL = r'<='
    MAIOR = r'>'
    MAIOR_IGUAL = r'>='
    IGUAL = r'=='
    DIFERENTE = r'!='
    ATRIBUICAO = r'='

    # Identificadores e Palavras-Chave
    ID['if'] = IF
    ID['else'] = ELSE
    ID['void'] = VOID
    ID['int'] = INT
    ID['return'] = RETURN
    ID['while'] = WHILE

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

    ignore_espace = '\n'


if __name__ == "__main__":

    arquivo = open('1_PC.txt', 'r')
    linha = arquivo.read()
    lista = list()
    lexer = analisadorLexico()

    for token in lexer.tokenize(linha):
        if((token.type == 'NUM') or (token.type == 'ID')):
            lista.append(token.type)
        else:
            lista.append(token.value)

    print(lista)
