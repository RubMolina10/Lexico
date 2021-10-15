import ply.lex as lex
import re
import codecs
#declaran los tokens

tokens = ['PR01','PR02','PR03','PR04','PR05','PR06','PR07','PR08','PR09','PR10','PR11','PR12','PR13','PR14','PR15','PR16',
         'PR17','PR18','PR19','PR20','PR21','PR22','PR23','PR24','PR25','PR26','PR27','PR28','PR29','PR30','PR31','PR32','PR33','PR34','PR35',
         'PR36','PR37','PR38','PR39','PR40','PR41','PR42','PR43','PR44','PR45','PR46','PR47','PR48','PR49','PR50','PR51','PR52','PR53','PR54',
         'PR55','PR56','PR57','PR58','PR59','PR60','PR61','PR62','PR63','PR64','PR65','PR66','PR67','PR68','PR69','PR70',
         'ASIGN','OA','OL','OR','PI','PF','VAR','CNE','CC']

#declarar las expresiones regulares simples.
t_ignore = ' \t\r'
t_PR01 = r'INSERT'
t_PR02 = r'Insert'
t_PR03 = r'insert'
t_PR04 = r'INTO'
t_PR05 = r'Into'
t_PR06 = r'into'
t_PR07 = r'VALUES'
t_PR08 = r'Values'
t_PR09 = r'values'
t_PR10=r'DELETE'
t_PR11=r'Delete'
t_PR12=r'delete'
t_PR13=r'INNER'
t_PR14=r'Inner'
t_PR15=r'inner'
t_PR16=r'JOIN'
t_PR17=r'Join'
t_PR18=r'join'
t_PR19=r'ON'
t_PR20=r'On'
t_PR21=r'UPDATE'
t_PR22=r'Update'
t_PR23=r'update'
t_PR24=r'SET'
t_PR25=r'Set'
t_PR26=r'set'
t_PR27=r'NULL'
t_PR28=r'Null'
t_PR29=r'null'
t_PR30=r'TOP'
t_PR31=r'Top'
t_PR32=r'top'
t_PR33=r'PERCENT'
t_PR34=r'Percent'
t_PR35=r'percent'
t_PR36 = r'SELECT'
t_PR37 = r'Select'
t_PR38 = r'SELECT'
t_PR39 = r'select'
t_PR40 = r'DISTINCT'
t_PR41 = r'Distinct'
t_PR42 = r'distinct'
t_PR43 = r'FROM'
t_PR44 = r'From'
t_PR45 = r'from'
t_PR46 = r'WHERE'
t_PR47 = r'Where'
t_PR48 = r'where'
t_PR49 = r'GROUP'
t_PR50 = r'Group'
t_PR51 = r'group'
t_PR52 = r'BY'
t_PR53 = r'By'
t_PR54 = r'HAVING'
t_PR55 = r'Having'
t_PR56 = r'having'
t_PR57 = r'ORDER'
t_PR58 = r'Order'
t_PR59 = r'order'
t_PR60 = r'BETWEEN'
t_PR61 = r'Between'
t_PR62 = r'betweem'
t_PR63 = r'AND'
t_PR64 = r'And'
t_PR65 = r'and'
t_PR66 = r'LIKE'
t_PR67 = r'Like'
t_PR68 = r'like'
t_PR69 = r'IN'
t_PR70 = r'In'



t_OA = r'\+ | - | \* | \/ '
t_OL = r' && | \|\|'
t_OR = r'< | > '
t_PI = r'\('
t_PF = r'\)'


#declarar las expresiones regulares compuestas.
def t_CNE (t):
    r'/d | [0-9]+'
    t.value = int (t.value)
    return t

def t_CC (t):
    r'\"[a-zA-Z0-9 ]+\" | \'[a-zA-Z0-9 ]+\''
    t.value = t.value
    return t
def t_VAR (t):
     r'[a-z][a-zA-Z0-9_]+'
     return t
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_error (t):
    print ("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1) 
#C:\Users\leoba\source\repos\PythonApplication2\PythonApplication2
carpeta = "C:\\Users\\regem\\source\\repos\\analizadorLexico\\"
archivo = "texto.txt"
abrir = codecs.open(carpeta+archivo,"r","utf-8")
cadena = abrir.read()
abrir.close()
analizador = lex.lex()
analizador.input(cadena)
while True:
    tok = analizador.token()
    if not tok: 
        break
    print(tok)


ListaDeTokesns =['rINSERT',r'Insert',r'insert',r'INTO',r'Into',r'into',r'VALUES',r'Values',r'values',r'DELETE',r'Delete',r'delete',r'INNER',r'Inner',r'inner'
,r'JOIN',r'Join',r'join',r'ON',r'On',r'UPDATE',r'Update',r'update',r'SET',r'Set',r'set',r'NULL',r'Null',r'null',r'TOP',r'Top',r'top'
,r'PERCENT',r'Percent',r'percent',r'SELECT',r'Select',r'SELECT',r'select',r'DISTINCT',r'Distinct',r'distinct',r'FROM',r'From',r'from',r'WHERE',r'Where'
,r'where',r'GROUP',r'Group',r'group',r'BY',r'By',r'HAVING',r'Having',r'having',r'ORDER',r'Order',r'order',r'BETWEEN',r'Between',r'betweem',r'AND', r'And',r'and',r'LIKE',r'Like',r'like',r'IN',r'In']

#print(ListaDeTokens)
for x in tokens:
    print (x)
    print(len(tokens))

    


