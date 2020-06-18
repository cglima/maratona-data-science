"""
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma
string no formato D de mesPorExtenso de AAAA. Opcionalmente,
valide a data e retorne NULL caso a data seja inválida.
"""
class ValidationError(Exception):
    pass

MESES = {
    "01" : "janeiro",
    "02" : "fevereiro",
    "03" : "março",
    "04" : "abril",
    "05" : "maio",
    "06" : "junho",
    "07" : "julho",
    "08" : "agosto",
    "09" : "setembro",
    "10" : "outubro",
    "11" : "novembro",
    "12" : "dezembro",
}

def validar_ano(data):
    #extrair a informação
    ano = data[6:10]

    #se fora da regra
        #lança exceção
    if not (ano.isdigit()):
        mensagem = f"Ocorreu um erro!! O ano não é um digito válido!: {data}"
        raise ValidationError(mensagem)

    if not(len(ano) == 4):
        mensagem = f"Ocorreu um erro!! O ano não tem 4 digitos: {data}"
        raise ValidationError(mensagem)

def validar_mes(data):

    mes = data[3:5]

    try:
        MESES[mes]
    except KeyError:
        raise ValidationError(f"Ocorreu um erro!! O mês {mes} da data {data} não existe!!")


def validar_dia_mes(data):

    dia = data[0:2]
    dia_numerico = int(dia)
    #SE DIA FOR MAIOR QUE 31 - DIA INVALIDO
    #SE DIA FOR MENOR QUE 1 - DIA INVALIDO
    if (dia_numerico > 31 or dia_numerico <= 0):
        raise ValidationError(f"Ocorreu um erro!! O dia {dia_numerico} da data {data} não existe")

    DIASMAX = {
        "01" : 31,
        "02" : 28,
        "03" : 31,
        "04" : 30,
        "05" : 31,
        "06" : 30,
        "07" : 31,
        "08" : 31,
        "09" : 30,
        "10" : 31,
        "11" : 30,
        "12" : 31,
    }

    mes = data[3:5]
    #se ano for bissexto
        #mês dia máximo de fevereiro igual a 29
    if is_bissexto(data):
        DIASMAX["02"] = 29

    #se dia da data for maior que o dia maximo do mÊs
        #lança erro
    if(dia_numerico > DIASMAX[mes]):
        raise ValidationError(
            f"Ocorreu um erro!! O dia {dia_numerico} da data "
            f"{data} não pode ser maior que o dia máximo do mês {mes}"
        )


def is_bissexto(data):

    ano = data[6:10]
    ano_numerico = int(ano)
    bissexto = False
    if (ano_numerico % 400 == 0):
        bissexto = True
    else:
        if(ano_numerico % 4 == 0 and ano_numerico % 100 != 0):
            bissexto = True
        else:
            bissexto = False
    return bissexto


def data_por_extenso(data):
    """Retornar a data por extenso se for válida"""
    try:
        #validar o ano
        validar_ano(data)

        #validar o mÊs
        validar_mes(data)

        #validar o dia e o mês
        validar_dia_mes(data)

        dia = data[0:2]
        mes = data[3:5]
        ano = data[6:10]

        data_por_extenso = f"{dia} de {MESES[mes]} de {ano}"

        return data_por_extenso

    except ValidationError as error:
        print("Ocorreu um erro ao validar a data:")
        print("\t", error)
        return None

if __name__ == "__main__":

    #ler uma data
    datas = [
        "16/06/2020", # DATA VÁLIDA
        "00/01", # FALTA O ANO
        "manga", # DATA INVÁLIDA FORA DO FORMATO
        "04/15/1981", # DATA INVÁLIDA PORQUE O MÊS NÃO EXISTE
        "12/06/190", # DATA INVÁLIDA PORQUE O ANO TEM 3 CARACTERES
        "30/02/2012", # DATA INVÁLIDA PORQUE O MÊS 02 NÃO TEM DIA 30
        "30/11", # FALTA O ANO
        "25/08/maga", #ANO INVALIDO
        "12/-4/1980", #MES negativo
        "31/04/1587", # MÊS 4 TEM 30 DIAS
        "-2/01/1995", # DATA INVÁLIDA PORQUE DIA NEGATIVO
        "32/10/2005", # DATA INVÁLIDA PORQUE DIA É MAIOR QUE 31
        "30/02/2006", # MÊS 02 SÓ TEM 28 OU 29 DIAS
        "31/04/2006", # MÊS 4 TEM 30 DIAS
        "31/06/2007", # MêS 06 TEM 30 DIAS
        "29/02/2001", # NÃO É ANO BISSEXTO
        "29/02/1900", # NÃO É ANO BISSEXTO
        "29/02/2000", # É ANO BISSEXTO
        "29/02/2004", # É ANO BISSEXTO
        ]

    for d in datas:
        print(f" {d} ".center(60, "*"))
        por_extenso = data_por_extenso(d)
        print(por_extenso)
