from dpa import *
O="out/h/"
import os; os.makedirs(O,exist_ok=True)
def st(arq,k,t,c,b):
    return (O+arq+".jpg", story(f'<div class="k" style="text-align:center">{k}</div><h1 style="text-align:center;font-size:100px">{t}</h1><p style="text-align:center;margin-top:46px">{c}</p><div style="text-align:center;margin-top:70px"><span class="btn">{b}</span></div>'),"story")
render([
 st("2027-01-11_story_segunda_edital_da_semana","Segunda-feira","Qual é o <mark>edital da semana</mark>?","Mande o link agora e a proposta fica pronta antes do prazo.","Envie pelo WhatsApp"),
 st("2027-01-18_story_segunda_um_cnpj","Começo de semana","Vários itens, <mark>um fornecedor</mark>","Informática, climatização, eletro, ferramentas e áudio e vídeo no mesmo CNPJ.","Mande a sua lista"),
 st("2027-01-25_story_segunda_dispensa","Dispensa ou pregão?","A DPA cota <mark>os dois</mark>","Envie o item, a quantidade e o local de entrega.","Envie seu edital"),
])
