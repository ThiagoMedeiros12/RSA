import random
import math
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def randomNum():
    return random.randint(0,1000001)
    
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    while True:
        num = randomNum()
        if is_prime(num):
            return num
        


def generate_n(tuple):
    p = tuple[0]
    q = tuple[1]
    
    n = p * q
    fi_n = (p-1)*(q-1)
    return n,fi_n

def genereate_e(fi_n):
    while True:
        e = random.randint(2,fi_n - 1)
        if is_prime(e) and math.gcd(e,fi_n) == 1:
            return e

def generate_d(fi_n,e):
    d = pow(e,-1,fi_n)
    return d 


def criador_chaves():
    p = generate_prime()     #gera valor p
    q = generate_prime()    # gera valor q
    pq_tuple = sorted([p,q],reverse=True)   #organiza p q na tupla em ordem crescente
    nfin_tuple = generate_n(pq_tuple) # gera n e n_fin
    e = genereate_e(nfin_tuple[1])  # gera e
    d = generate_d(fi_n=nfin_tuple[1],e=e)  #gera d 
    array = [pq_tuple[0],pq_tuple[1],nfin_tuple[0],nfin_tuple[1],e,d] # gera um array com todos os dados na ordem [p,q,n,nfin,e,d]

    return array

def input_ascii(msg_entrada):
    list_msg = msg_entrada
    asciiValue = [ord(char) for char in list_msg]
    asciiMsg = ''.join(str(num) for num in asciiValue)
    return asciiMsg 


def transform_Char_Array(asciiMsg,n): # recebe msg em string de todos os numeros juntos
    aux_list = []
    aux_str = ""

    for digit in asciiMsg:
            aux_str += digit
        
            if int(aux_str) > n:
                
                aux_list.append(int(aux_str[:-1]))
                aux_str = digit                
    
    if aux_str:
        aux_list.append(int(aux_str))
    return aux_list # retorna lista de numeros menores que n


def msg_cript(pre_cripto,eList,nList):
    cripted_msg = []
    e = int(eList)
    n = int(nList)
    
    for i in pre_cripto:
        new_value = pow(base = i,exp = e,mod = n)
        cripted_msg.append(new_value)
    return cripted_msg


def final_cripted_msg(cripted_msg):
    msg = "".join(str(num) for num in cripted_msg)
    return msg


def ascii_letter (strmsg):
    ascii_to_letter = []
    aux_part = ""
    for i in strmsg:
        if aux_part == "":
            aux_part = i
        else:
            combine = int(aux_part + i)
            if 31 > combine < 127:
                aux_part += i
            else:
                ascii_to_letter.append(combine)
                aux_part = ""
    if aux_part:
        ascii_to_letter.append(int(aux_part))

    return ascii_to_letter 


def ascii_char(ascii_list_value):
    char_from_ascii =[chr(num) for num in ascii_list_value]
    return char_from_ascii




def cript_msg(input):
    arrayKeys = criador_chaves() #[p,q,n,fi_n,e,d] gera valores para encriptar
    asciiMsg = input_ascii(input) #recebe o input de msg
    pre_cripto = transform_Char_Array(asciiMsg,arrayKeys[2]) # retorna lista de numeros ascii menores que n para serem criptografado
    final_crip = msg_cript(pre_cripto=pre_cripto,eList=arrayKeys[4],nList=arrayKeys[2]) # faz a criptografia de cada item da lista
    cripted_msg = final_cripted_msg(final_crip) # retorna string da mensagem criptografada
    return arrayKeys,cripted_msg # retorna array de valores pra criptografar e a mensagem criptografada





def decript_msg(d,n,criptedInput_msg):
    cripted_msged = transform_Char_Array(asciiMsg=criptedInput_msg,n=n)
    Listmsg = msg_cript(cripted_msged,d,n)
    strmsg = final_cripted_msg(Listmsg)
    ascii_list_value = ascii_letter(strmsg=strmsg)
    decripted_msg = ascii_char(ascii_list_value=ascii_list_value)
    msg_decripted_string = final_cripted_msg(decripted_msg)
   

    return msg_decripted_string


def criptografar_descriptografar(input):
    while True:
        list,msg = cript_msg(input=input)
        str_msg = decript_msg(d=list[5],n=list[2],criptedInput_msg=msg)
        if input == str_msg:
            return list,msg
        

            

        



#decript_msg(d,n,criptedInput_msg)
#criptografar_descriptografar(input)







    



