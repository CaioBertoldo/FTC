import re

def validate_cpf(cpf):
    pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    if not pattern:
        return False
    cpf_digits = []
    for i in cpf:
        if i.isdigit():
            i = int(i)
            cpf_digits.append(i)
    v1 = v2 = 0
    for i in range(0, 9):
        v1 = v1 + cpf_digits[i] * (9 - (i % 10))
        v2 = v2 + cpf_digits[i] * (9 - ((i + 1) % 10))
    v1 = (v1 % 11) % 10
    v2 = v2 + v1 * 9
    v2 = (v2 % 11) % 10
    if v1 == cpf_digits[10] and v2 == cpf_digits[9]:
        return True
    else:
        return False

def validate_cnpj(cnpj):
    pattern = re.compile(r'^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$')
    if not pattern:
        return False
    cnpj_digits = []
    for i in cnpj:
        if i.isdigit():
            i = int(i)
            cnpj_digits.append(i)
    v1 = v2 = 0
    # Calculates first check digit
    v1 = 5 * cnpj_digits[0] + 4 * cnpj_digits[1] + 3 * cnpj_digits[2] + 2 * cnpj_digits[3]
    v1 += 9 * cnpj_digits[4] + 8 * cnpj_digits[5] + 7 * cnpj_digits[6] + 6 * cnpj_digits[7]
    v1 += 5 * cnpj_digits[8] + 4 * cnpj_digits[9] + 3 * cnpj_digits[10] + 2 * cnpj_digits[11]
    v1 = 11 - v1 % 11
    if v1 >= 10:
        v1 = 0

    # Calculates the second check digit
    v2 = 6 * cnpj_digits[0] + 5 * cnpj_digits[1] + 4 * cnpj_digits[2] + 3 * cnpj_digits[3]
    v2 += 2 * cnpj_digits[4] + 9 * cnpj_digits[5] + 8 * cnpj_digits[6] + 7 * cnpj_digits[7]
    v2 += 6 * cnpj_digits[8] + 5 * cnpj_digits[9] + 4 * cnpj_digits[10] + 3 * cnpj_digits[11]
    v2 += 2 * cnpj_digits[12]
    v2 = 11 - v2 % 11
    if v2 >= 10:
        v2 = 0
    if v1 == cnpj_digits[12] and v2 == cnpj_digits[13]:
        return True
    else:
        return False

def validate_cp(cp):
    if len(cp) == 14:
        return(validate_cpf(cp))
    elif len(cp) == 18:
        return(validate_cnpj(cp))

def validate_email(email):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return bool(re.match(pattern, email))

def validate_number(number):
    pattern = re.compile(r'\+55\(\d{2}\)\d{4}\-\d{4}')
    return bool(re.match(pattern, number))

def validate_quick_key(key):
    pattern = r'^([0-9A-Fa-f][0-9A-Fa-f]\.){3}[0-9A-Fa-f][0-9A-Fa-f]$'

    if re.match(pattern, key):
        if not re.search(r'[A-Fa-f]{2}', key):
            if not re.search(r'([0-9A-Fa-f])\1', key):
                return True
    return False

def validate_datetime(date):
    pattern = re.compile(r'\d{2}/\d{2}/\d{4}')  
    if not pattern:
        return False
    
    # Se o primeiro dígito do mês for diferente de 0 e 1
    if date[3] != '0' and date[3] != '1':
        return False
    
    # Se o primeiro dígito do mês for 1, o segundo só pode ser 0, 1 ou 2
    if date[3] == '1':
        pattern = re.compile(r'\d{2}/\d[0-2]/\d{4}')
        if not pattern:
            return False
    
    # Se o primeiro dígito do mês for 0, o segundo pode ser 0-9
    if date[3] == '0':
        pattern = re.compile(r'\d{2}/\d[1-9]/\d{4}')
        if not pattern:
            return False

    # Se o primeiro dígito do dia for 0, 1 ou 2 o segundo pode ser 0-9
    if date[0] == '0' or date[0] == '1' or date[0] == '2':
        pattern = re.compile(r'0[1-9]/\d{2}/\d{4}')
        if not pattern:
            return False
    
    # Se for jan, mar, may, jul, aug, tem 31 dias
    if date[3] == '0' and date[4] == '1' or date[4] == '3' or date[4] == '5' or date[4] ==  '6' or date[4] == '8':
        pattern = re.compile(r'[0-2][0-9]/\d{2}/\d{4}')
        if date[0] == '3': # se for dia 30 ou 31, só pode ser dia 30 ou 31
            pattern = re.compile(r'3[0-1]/\d{2}/\d{4}')
            if not pattern:
                return False
    
    # Se for oct, dez, tem 31 dias
    if date[3] == '1' and date[4] == '0' or date[4] == '2':
        pattern = re.compile(r'[1-2][0-9]/\d{2}/\d{4}')
        if date[0] == '3':
            pattern = re.compile(r'3[0-1]/\d{2}/\d{4}')
            if not pattern:
                return False
    
    # Se for Apr, Jun, Sep, tem 30 dias
    if date[3] == '0' and date[4] == '4' or date[4] == '6' or date[4] == '9':
        pattern = re.compile(r'[0-2][0-9]/\d{2}/\d{4}')
        if date[0] == '3':
            pattern = re.compile(r'30/\d{2}/\d{4}')
            if not pattern:
                return False
            
    # Se for Nov, tem 30 dias
    if date[3] == '1' and date[4] == '1':
        pattern = re.compile(r'[0-2][0-9]/11/\d{4}')
        if date[0] == '3':
            pattern = re.compile(r'30/11/\d{4}')
            if not pattern:
                return False
    
    # Se for Feb, tem 28 ou 29 dias
    if date[3] == '0' and date[4] == '2':
        pattern = re.compile(r'[0-2][0-9]/02/\d{4}')
        if not pattern:
            return False
    
    return True

def validate_hour(hour):
    pattern = re.compile(r'\d{2}:\d{2}')
    if not pattern:
        return False
    
    # Se o primeiro dígito da hora for diferente de 0, 1 ou 2
    if hour[0] != '0' and hour[0] != '1' and hour[0] != '2':
        return False
    
    # Se o primeiro dígito dos minutos for maior do que 5
    if hour[3] != '0' and hour[3] != '1' and hour[3] != '2' and hour[3] != '3' and hour[3] != '4' and hour[3] != '5':
        return False
    
    return True

def validate_transaction_value(value):
    pattern = re.compile(r'^[R]\$ \d*,+\d{2}$')
    return bool(re.match(pattern, value))

def validate_security_code(code):
    cont_mai = 0
    cont_digits = 0
    cont_special = 0
    cont_min = 0

    pattern_mai = re.compile(r'[A-Z]')
    pattern_digits = re.compile(r'[0-9]')
    pattern_min = re.compile(r'[a-z]')

    for i in code:
        # Contar a quantidade de letras maiúsculas
        validade_code = re.match(pattern_mai, i)
        if validade_code:
            cont_mai += 1

        # Contar a quantidade de letras minúsculas
        validade_code = re.match(pattern_min, i)
        if validade_code:
            cont_min += 1
        
        # Contar a quantidade de dígitos
        validade_code = re.match(pattern_digits, i)
        if validade_code:
            cont_digits += 1

        # Contar a quantidade de símbolos especiais
        if i in '@$%(*)':
            cont_special += 1

    if cont_mai == 3 and cont_min == 3 and cont_digits == 4 and cont_special == 2:
        return True
    else:
        return False 

def validate_keys(key):
    if key[0] == '+':
        return validate_number(key)
    elif key[2] == '.':
        return validate_quick_key(key)
    elif key[0].isalpha():
        return validate_email(key)
    else:
        return False
    
def validate_origin_key(key):
    cont = 0
    for i in valid_keys:
        if i == key:
            keys_list[0] = cont
            return True
        cont += 1
    return False

def validadte_destiny_key(key):
    cont = 0
    for i in valid_keys:
        if i == key:
            for i in range(len(keys_list)):
                if cont < keys_list[i] and keys_list[0] < keys_list[i]:
                    return False
                else:
                    return True
        cont += 1
    return False

# Main

validation = True
cont = 0 # contador da posição da última chave do cliente
valid_keys = [] # Lista das chaves válidas
keys_list = [0] # Lista para guardar a posição inicial das chaves do cliente

# Loop para validadar os clientes
while True:
    client = input() # Introduzir um cliente
    data = client.split(" ") # Dados do cliente
    identifier = data[0]

    # Se chegar ao separador, acaba os clientes
    if identifier == '==========':
        break
    else:
        validation = validate_cp(identifier) # Validar o identificador (cp) do cliente
    
    # Se a validação der False
    if not validation:
        break
    valid_keys.append(identifier)
    cont += 1
    del data[0]

    # Validar as possíveis chaves
    for i in data:
        validation = validate_keys(i)

        if validation:
            valid_keys.append(i)
            cont += 1
        else:
            break

    if not validation:
        break

    keys_list.append(cont)

if not validation:
    print(False, end='')

# Loop para validar as transações
else:
    try:
        while True:
            transation = input()
            data2 = transation.split(" ")

            origin = data2[0]
            destiny = data2[1]
            value = data2[2] + ' ' + data2[3]
            datetime = data2[4]
            hour = data2[5]
            security_code = data2[6]

            validation = validate_origin_key(origin)
            if not validation:
                break

            validation = validadte_destiny_key(destiny)
            if not validation:
                break

            validation = validate_transaction_value(value)
            if not validation:
                break

            validation = validate_datetime(datetime)
            if not validation:
                break

            validation = validate_hour(hour)
            if not validation:
                break

            validation = validate_security_code(security_code)
            if not validation:
                break        

    except EOFError:
        if not validation:
            print(False, end='')
        else:
            print(True, end='')

# 04.128.563/0001-10 zxhbpg@jmurip.com +55(92)3656-8985
# 62.144.175/0001-20 L2.B3.D5.a7
# ==========
# zxhbpg@jmurip.com 62.144.175/0001-20 R$ 1.000,00 13/12/2022 23:40 s%%B9F7cB19t
# L2.B3.D5.a7 +55(92)3656-8985 R$ 57,52 29/07/2022 13:45 6O31iJa7dZ*%

# 136.775.118-79 pmlxew@veracg.com +55(92)3584-0188
# 90.400.888/0001-42 D5.D9.A9.b6
# ==========
# pmlxew@veracg.com 90.400.888/0001-42 R$ 100,00 11/12/2022 18:06 @@XHn6az31O9
# D5.D9.A9.b6 +55(92)3584-0188 R$ 25,89 13/01/2022 10:21 W1%U(7od43Li