import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def discriminative_tests(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'discriminative_tests'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ##################################
    ############ discriminative_tests #############
    ##################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text', 'Text', "Text", "Text", "Text", "Text", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["TriangleTest", "minimum_number_of_assessors", "alpha", "beta", "minimum_of_correct_responses", "score_sheet", "protocol_sheet"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["TesteTriangular", "numero_minimo_de_avaliadores", "alfa", "beta", "minimo_de_respostas_corretas", "planilha_score", "planilha_protocolo"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [['Text', "Text", ], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Panelist", "Sample", "Product"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Provador", "Amostra", "Produto"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [['Text', "Text", "Text", "Text", "Text", "Text", "Text", "Text", "Text", "Text", "Text", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Date", "Test code", "Triangle test - Order and Serving Protocol",
        "Post this sheet in the area where trays are prepared. \nCode scoresheets and serving containers ahead of time.", "PRODUCT NAME", "SAMPLE A INFORMATION", "SAMPLE B INFORMATION", "Code serving containers as follows:",
        "RECOMMENDATIONS", "1. Label plates with the unique 3 digit random numbers and arrange in serving order by panelist.", "2. To serve, place samples and a coded scoresheet on a serving tray.", "3. Decode whether reply was correct or incorrect by referring back to the worksheet."
        ], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Data", "Código do teste", "Teste Triangular - Protocolo de serviço e ordenação",
        "Coloque esta folha na área onde as bandejas são preparadas. \nCodifique as planilhas e os contêineres com antecedência.", "NOME DO PRODUTO", "INFORMAÇÃO DA AMOSTRA A", "INFORMAÇÃO DA AMOSTRA B", "Codifique os recipientes da seguinte forma:", "RECOMENDAÇÕES", "1. Rotule as placas com os números aleatórios exclusivos de 3 dígitos e organize-os em ordem de servir pelo provador", "2. Para servir, coloque as amostras e uma planilha codificada em uma bandeja de servir.", "3. Decodifique se a resposta foi correta ou incorreta consultando a planilha."
        ], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: data not found"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: resultados não encontrados"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [['Text', "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["To generate the protocol it is necessary to generate the combinations previously.", "Use the method 'make_combinations' to get the combinations"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Para gerar o protocolo é necessário gerar as combinações préviamente.", "Utilize o método 'make_combinations' para obter as combinações"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################


    ###########################
    position = position + 1 # 6

    params = [
        [['Text', "Text", "Text", "Text", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Triangle Test", "Name", "Instructions", 'Evaluate samples from left to rigth. Two are alike. Mark an "X" in the box from the sample which differs from the others. If no difference is apparent, you must guess.', "Remarks"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Teste Triangular", "Nome", "Instruções", 'Avalie as amostras da esquerda para a direita. Duas são iguais. Marque um "X" na caixa da amostra que difere das demais. Se nenhuma diferença for aparente, você deve adivinhar.', "Comentários"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    #################################################################
    ####################   FECHANDO A DATABASE   ####################
    #################################################################

    cursor.close()
    connection.close()



if __name__ == '__main__':
    discriminative_tests()
