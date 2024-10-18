cont_s = 0
cont_n = 0
cont_m_s = 0
cont_h_n = 0
cont_m = 0
cont_h = 0
for i in range(200):
    pessoas = int(input("DIGITE 1 PARA SE VOCE DISSE SIM E PERTENCE AO SEXO FEMININO\n"
                        "DIGITE 2 PARA SE VOCE DISSE SIM E PERTENCE AO SEXO MASCULINO\n"
                        "DIGITE 3 PARA SE VOCE DISSE NÃO E PERTENCE AO SEXO FEMININO\n"
                        "DIGITE 4 PARA SE VOCE DISSE NÃO E PERTENCE AO SEXO MASCULINO\n"
                        "DIGITE AQUI: "))
    
    if(pessoas == 1) or (pessoas == 2):
        cont_s += 1
    elif(pessoas == 3) or (pessoas == 4):
        cont_n += 1

    if(pessoas == 1):
        cont_m_s += 1
    elif(pessoas == 2):
        cont_h_n += 1
    elif(pessoas == 3):
        cont_m += 1
    elif(pessoas == 4):
        cont_h += 1

porcetagem_m = (cont_m_s/(cont_m_s+cont_m))*100
porcetagem_h = (cont_h_n/(cont_h+cont_h_n))*100

print(f"\nQUATIDADE DE PESSOAS QUE VOTARAM SIM: {cont_s}\nQUATIDADE DE PESSOAS QUE VOTARAM NÃO: {cont_n}\nPORCETAGENS DE MULHERES QUE DISSERAM SIM: {porcetagem_m:.2f} %\nPORCETAGENS DE HOMENS QUE DISSERAM NÃO: {porcetagem_h:.2f} %")