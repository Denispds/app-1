import streamlit as st

# Página da Implementação
def implementacao():
    st.title("Implementação do Projeto")

    st.header("Fase 1: Planejamento")
    st.markdown("""
    - Reunião inicial com todos os membros da equipe para discutir o projeto.
    - Definição de KPIs (Key Performance Indicators) para monitorar o desempenho do projeto.
    """)

    st.header("Fase 2: Treinamento")
    st.markdown("""
    - Treinamento do Gestor de Compras em análise de mercado e negociação com fornecedores.
    - Treinamento do Assistente de Estoque em técnicas de organização e controle de inventário.
    - Treinamento do Responsável pela Saída de Produtos em logística e atendimento ao cliente.
    """)

    st.header("Fase 3: Execução")
    st.markdown("""
    - Implementação do fluxo de processos conforme definido.
    - Acompanhamento diário das atividades e ajustes conforme necessário.
    """)

    st.header("Fase 4: Avaliação")
    st.markdown("""
    - Revisão semanal do desempenho do projeto com base nos KPIs.
    - Feedback contínuo entre os membros da equipe para melhoria contínua.
    """)

    st.header("Conclusão")
    st.markdown("""
    A implementação deste projeto visa não apenas melhorar a eficiência logística, 
    mas também proporcionar uma melhor experiência para os clientes internos, garantindo que os produtos estejam sempre disponíveis e sejam entregues pontualmente. A colaboração e a comunicação eficiente entre os membros da equipe serão fundamentais para o sucesso deste projeto.
    """)

# Chamada para a função no Streamlit
implementacao()
