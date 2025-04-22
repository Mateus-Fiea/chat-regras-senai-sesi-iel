import streamlit as st

st.set_page_config(page_title="Chat de Regras – Auditoria, Moskit e 360", layout="centered")
st.title("🤖 Chat Inteligente – Regras, Moskit e Solução 360")

st.write("Digite sua dúvida sobre modelos de gestão, parcelamento, Moskit ou 360:")

pergunta = st.text_input("Sua dúvida:")

def responder(pergunta):
    pergunta = pergunta.lower()

    # BLOCO: REGRAS DE AUDITORIA
    if "mensal" in pergunta:
        return (
            "🔹 **Modelo Mensal**:\n"
            "- Permitido para: Combo SST, Aprendizagem, Curso Técnico (12 a 24 parcelas)\n"
            "- Ginástica Laboral e Mão de Obra Especializada: somente 12 parcelas\n"
            "- Forma de pagamento: somente Boleto Bancário\n"
            "- ❌ Não permitido para: Locação de Espaços\n"
            "- ⚠️ Exceção: Mão de Obra Especializada deve ter medição mensal."
        )
    elif "após execução" in pergunta:
        return (
            "🔹 **Modelo Após Execução**:\n"
            "- Não permite parcelamento\n"
            "- Aceita apenas Boleto Bancário\n"
            "- Não pode ser usado com Locação de Espaços"
        )
    elif "após assinatura" in pergunta:
        return (
            "🔹 **Modelo Após Assinatura**:\n"
            "- Até 10 parcelas (até 12 se for Mão de Obra Especializada com medição mensal)\n"
            "- ❌ Não aceita Depósito em Conta"
        )
    elif "após pagamento" in pergunta:
        return (
            "🔹 **Modelo Após Pagamento**:\n"
            "- Usado para: Locação de Espaços e clientes inadimplentes\n"
            "- Máximo de 2 parcelas\n"
            "- ❌ Não pode usar Depósito em Conta"
        )
    elif "aprendizagem gratuita" in pergunta:
        return (
            "🔹 **Aprendizagem Gratuita**:\n"
            "- Deve usar: Após Assinatura + Depósito em Conta\n"
            "- ❌ Não pode usar boleto, cartão ou modelos como Mensal ou Após Execução"
        )
    elif "faturamento sob demanda" in pergunta or "senai/al" in pergunta:
        return (
            "🔹 **SENAI/AL + Faturamento Sob Demanda**:\n"
            "- ❌ Não é permitido\n"
            "- ✅ Exceto para Metrologia com modelo Após Execução"
        )
    elif "sebrae" in pergunta and "modelo" in pergunta:
        return (
            "🔹 **Contratos Sebrae**:\n"
            "- Devem usar: Após Assinatura\n"
            "- ❌ Qualquer outro modelo está incorreto"
        )
    elif "sem produto" in pergunta:
        return "🔴 Erro: Proposta com 'Sem Produto' deve ser corrigida e incluir um produto válido."
    elif "fonte pagadora" in pergunta or any(x in pergunta for x in ["abdi", "sebrae al", "senai dr/df", "b+p"]):
        return (
            "🔹 **Fontes Pagadoras: Senai DR/DF, ABDI, SEBRAE-AL, B+P**\n"
            "- ✅ Devem usar: Modelo Após Execução + Depósito em Conta\n"
            "- ❌ Não pode usar boleto, cartão ou outro modelo"
        )
    elif "locação de espaços" in pergunta:
        return (
            "🔹 **Locação de Espaços**:\n"
            "- ✅ Deve usar: Após Pagamento\n"
            "- ❌ Não pode usar: Mensal, Após Execução ou Após Assinatura"
        )

    # BLOCO: MOSKIT
    elif "como cadastrar empresa" in pergunta:
        return (
            "🔹 Cadastro de empresa no Moskit:\n"
            "- Só pode ser feito após criar um negócio\n"
            "- É necessário: CNPJ válido, contato vinculado, e número de funcionários > 0\n"
            "- A empresa precisa ser ativada pelo Observatório para gerar proposta"
        )
    elif "funil do moskit" in pergunta:
        return (
            "🔹 **Funil do Moskit**:\n"
            "1. Base Geral (MQL)\n"
            "2. Cliente Potencial (SAL)\n"
            "3. Lead Qualificado (SQL)\n"
            "4. Oportunidade (OPP)\n"
            "5. Reunião\n"
            "6. Elaborar Proposta (gera link para o 360)"
        )
    elif "como abrir negócio" in pergunta:
        return (
            "🔹 Como abrir um negócio no Moskit:\n"
            "- Vá em 'Negócios' > 'Novo Negócio'\n"
            "- Preencha: Nome do negócio, Fase, Responsável, Empresa, Contato e Produto\n"
            "- Salve e avance conforme as etapas do funil"
        )
    elif "id da empresa" in pergunta:
        return (
            "🔹 Sobre o ID da empresa/contato no Moskit:\n"
            "- Para o link funcionar com o 360, o contato precisa estar vinculado corretamente à empresa\n"
            "- O ID da empresa deve aparecer igual no Moskit e na proposta"
        )

    # BLOCO: 360
    elif "360" in pergunta and "proposta" in pergunta:
        return (
            "🔹 Etapas para emitir proposta na Solução 360:\n"
            "- Preencha a aba 'Informações': Tipo de proposta, Forma de Pagamento, Template, Tabela de Preço\n"
            "- Depois preencha: Contato, Produto, Parcelas\n"
            "- Após isso, a proposta poderá ser enviada para aprovação da gerência"
        )
    elif "diagnóstico" in pergunta:
        return (
            "🔹 Etapa Diagnóstico no 360:\n"
            "- Usada quando o produto precisa de alteração (customização, precificação, carga horária)\n"
            "- O consultor deve mover o card para Diagnóstico e informar o que precisa ser ajustado\n"
            "- O setor de Negócios analisará e seguirá com a Análise de Novo Produto, se necessário"
        )
    elif "combo" in pergunta or "s+ pgr" in pergunta:
        return (
            "🔹 Regras do COMBO SST no 360:\n"
            "- Deve conter: PGR, PCMSO, E-social, S+, Laudos etc.\n"
            "- Modelo: Mensal\n"
            "- Prazo: 24 meses\n"
            "- ⚠️ Se faltar o E-social, não é mais Combo, é avulsa e segue outras regras"
        )
    elif "unidade executora" in pergunta:
        return (
            "🔹 Unidade Executora no 360:\n"
            "- Quando quem vai executar é diferente de quem criou o negócio, informe na aba 'Unidade Executora'\n"
            "- Isso evita erros e garante que o sistema direcione corretamente"
        )
    elif "não aparece a aba de produto" in pergunta:
        return (
            "🔹 Aba de produto não aparece no 360:\n"
            "- Verifique se você preencheu: Forma de Pagamento, Tipo de Proposta, Template e Tabela de Preço\n"
            "- Sem essas informações, a aba de produto fica oculta"
        )

    return "❌ Ainda não sei responder essa pergunta. Fale com o Mateus!"

# Exibe a resposta
if pergunta:
    st.success(responder(pergunta))
