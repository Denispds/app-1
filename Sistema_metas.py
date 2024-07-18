import streamlit as st

# Página do Sistema de Metas e Bônus
def sistema_de_metas():
    st.title("Sistema de Metas e Bônus")

    st.header("Gestor de Compras")
    st.subheader("KPIs:")
    st.markdown("""
    - **Precisão nas Previsões de Compras**
    - **Custo por Unidade Comprada**
    - **Tempo de Ciclo de Compras**
    - **Índice de Qualidade de Fornecedores**
    """)
    st.subheader("Metas e Bônus:")
    st.markdown("""
    - Manter a diferença de previsão abaixo de **5%** (_10% do salário_)
    - Reduzir o custo médio em **5%** (_5% do salário_)
    - Reduzir o tempo de ciclo em **10%** (_5% do salário_)
    - Manter a qualidade acima de **95%** (_5% do salário_)
    """)

    st.header("Assistente de Estoque - Interno")
    st.subheader("KPIs:")
    st.markdown("""
    - **Precisão do Inventário**
    - **Tempo de Processamento de Recebimento**
    - **Nível de Organização do Estoque**
    - **Rotatividade de Estoque**
    """)
    st.subheader("Metas e Bônus:")
    st.markdown("""
    - Manter a precisão acima de **98%** (_10% do salário_)
    - Reduzir o tempo em **15%** (_5% do salário_)
    - Receber avaliações positivas acima de **90%** (_5% do salário_)
    - Aumentar a rotatividade em **10%** (_5% do salário_)
    """)

    st.header("Assistente de Estoque - Externo")
    st.subheader("KPIs:")
    st.markdown("""
    - **Precisão no Atendimento de Pedidos**
    - **Tempo de Processamento de Pedidos**
    - **Satisfação do Cliente**
    - **Índice de Devoluções**
    """)
    st.subheader("Metas e Bônus:")
    st.markdown("""
    - Manter a precisão acima de **99%** (_10% do salário_)
    - Reduzir o tempo em **20%** (_5% do salário_)
    - Manter a satisfação acima de **95%** (_5% do salário_)
    - Manter o índice abaixo de **2%** (_5% do salário_)
    """)

    st.header("Time de Reposição")
    st.subheader("KPIs:")
    st.markdown("""
    - **Tempo de Reposição**
    - **Organização Visual**
    - **Disponibilidade de Produtos na Loja**
    """)
    st.subheader("Metas e Bônus:")
    st.markdown("""
    - Reduzir o tempo em **15%** (_5% do salário_)
    - Receber avaliações positivas acima de **90%** (_5% do salário_)
    - Manter a disponibilidade acima de **98%** (_10% do salário_)
    """)

    st.header("Time de Produção")
    st.subheader("KPIs:")
    st.markdown("""
    - **Qualidade da Embalagem**
    - **Tempo de Embalagem**
    - **Satisfação Interna**
    """)
    st.subheader("Metas e Bônus:")
    st.markdown("""
    - Manter a qualidade acima de **98%** (_10% do salário_)
    - Reduzir o tempo em **20%** (_5% do salário_)
    - Manter a satisfação interna acima de **95%** (_5% do salário_)
    """)

# Chamada para a função no Streamlit
sistema_de_metas()
