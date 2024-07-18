import streamlit as st

def home():
    st.title("Projeto de Implementação de Logística para Empresa de Acessórios Femininos")

    # Estrutura do Projeto
    st.header("Estrutura do Projeto")

    # Objetivos
    st.subheader("Objetivos")
    st.markdown("""
    - Melhorar a precisão e eficiência no gerenciamento de estoque.
    - Reduzir o tempo de processamento e distribuição dos produtos.
    - Assegurar que os produtos estejam corretamente precificados e organizados.
    - Melhorar a comunicação e coordenação entre os membros da equipe.
    """)

    # Fluxo de Processo
    st.header("Fluxo de Processo")
    st.markdown("""
    1. **Recebimento**: As mercadorias chegam e são conferidas pelo Assistente de Estoque.
    2. **Conferência**: O Assistente de Estoque verifica a quantidade e qualidade dos produtos recebidos.
    3. **Precificação**: Os produtos são precificados pelo Assistente de Estoque.
    4. **Lançamento no Sistema**: O Assistente de Estoque registra as entradas de produtos no sistema.
    5. **Distribuição**: O Responsável pela Saída de Produtos processa os pedidos dos clientes.
    6. **Organização no Estoque**: Produtos são mantidos organizados pelo Assistente de Estoque.
    7. **Saída de Produtos**: O Responsável pela Saída de Produtos embala e envia os produtos.
    8. **Solicitação de Compras**: O Gestor de Compras solicita a aquisição de novos produtos conforme necessário.
    """)

    # Cargos e Funções
    st.header("Cargos e Funções")

    # Gestor de Compras
    st.subheader("1. Gestor de Compras - LÍDER DO DEPARTAMENTO")
    st.markdown("""
    **Responsabilidades:**
    - Planejar e executar a compra de produtos, garantindo que o estoque seja suficiente para atender à demanda.
    - Negociar com fornecedores para obter as melhores condições de compra, preço e prazo de pagamento.
    - Monitorar o desempenho dos fornecedores e a qualidade dos produtos recebidos.
    - Orientação e suporte à equipe de logística.

    **Atividades:**
    - Analisar relatórios de vendas e previsões de demanda para planejar compras futuras.
    - Realizar pedidos de compra e acompanhar a entrega dos produtos.
    - Avaliar e selecionar novos fornecedores, mantendo um cadastro atualizado.
    - Trabalhar em conjunto com o Assistente de Estoque para garantir que os produtos recebidos estejam corretos.
    """)

    # Assistente de Estoque - Interno
    st.subheader("2. Assistente de Estoque - INTERNO")
    st.markdown("""
    **Responsabilidades:**
    - Receber, conferir e armazenar produtos no estoque.
    - Garantir que o estoque esteja organizado e que os produtos sejam facilmente acessíveis.
    - Manter registros precisos de entradas e saídas de produtos.
    - Emissão de etiquetas de preço.
    - Garantir que o estoque esteja sempre em rotatividade.
    - Registro dos produtos enviados para a loja ou ponto de vendas.
    - Gestão dos produtos com defeito de fábrica.
    - Definir os produtos a serem produzidos e enviados para a loja.
    - Gestão da produtividade de encartelamento.
    - Apresentar os indicadores.

    **Atividades:**
    - Receber e conferir as mercadorias com base nos pedidos de compra.
    - Precificar os produtos conforme necessário.
    - Organizar os produtos no estoque de maneira lógica e eficiente.
    - Realizar inventários periódicos para garantir a precisão do estoque.
    - Auxiliar na preparação de relatórios de estoque para o Gestor de Compras.
    - Comunicar a chegada de novos produtos com o time de vendas e marketing.
    - Alimentar e enviar relatórios de produtividade do departamento.
    - Comunicar fatos e acontecimentos relevantes do departamento.
    """)

    # Assistente de Estoque - Externo
    st.subheader("3. Assistente de Estoque - EXTERNO")
    st.markdown("""
    **Responsabilidades:**
    - Processar pedidos de produtos enviados do CD.
    - Garantir que o estoque de produtos na frente de loja e o sistema estejam alinhados.
    - Acompanhar as vendas dos produtos e solicitar ao CD a reposição.
    - Avaliar como estão as seções da loja.
    - Verificar produtos solicitados pela equipe de vendas.
    - Saída dos produtos para o catálogo - fotos.
    - Coordenar as demandas da produção.
    - Ajudar na organização.

    **Atividades:**
    - Verificar os pedidos de clientes e separar os produtos necessários.
    - Embalar os produtos de maneira segura e eficiente.
    - Organizar a logística de envio, escolhendo as melhores opções de transporte.
    - Atualizar o sistema com informações de envio e entrega.
    - Monitorar o status das entregas e resolver eventuais problemas de distribuição.
    """)

    # Assistente de Reposição
    st.subheader("4. Assistente de Reposição")
    st.markdown("""
    **Responsabilidades:**
    - Verificar os produtos que precisam ser enviados para a frente de loja.
    - Manter as seções e vitrines da loja organizadas e atrativas.
    - Garantir que a loja mantenha um visual merchandising adequado.

    **Atividades:**
    - Realizar verificações diárias para identificar produtos que precisam ser repostos na frente de loja.
    - Reorganizar e repor produtos nas seções e vitrines da loja.
    - Trabalhar em conjunto com o time de produção para garantir que os produtos estejam prontos para exposição.
    - Manter a loja organizada e visualmente atraente para os clientes.
    """)

    # Time de Produção
    st.subheader("5. Time de Produção")
    st.markdown("""
    **Responsabilidades:**
    - Colocar os produtos em embalagens adequadas.
    - Preparar os produtos para serem enviados ou expostos na loja.

    **Atividades:**
    - Embalar os produtos conforme os padrões de qualidade estabelecidos.
    - Garantir que os produtos estejam prontos para serem enviados ou expostos na loja.
    - Trabalhar em conjunto com o time de reposição para garantir que os produtos estejam prontos para exposição.
    """)

    # Implementação do Projeto
    st.header("Implementação do Projeto")

    st.subheader("Fase 1: Planejamento")
    st.markdown("""
    - Reunião inicial com todos os membros da equipe para discutir o projeto.
    - Definição de KPIs (Key Performance Indicators) para monitorar o desempenho do projeto.
    """)

    st.subheader("Fase 2: Treinamento")
    st.markdown("""
    - Treinamento do Gestor de Compras em análise de mercado e negociação com fornecedores.
    - Treinamento do Assistente de Estoque em técnicas de organização e controle de inventário.
    - Treinamento do Responsável pela Saída de Produtos em logística e atendimento ao cliente.
    """)

    st.subheader("Fase 3: Execução")
    st.markdown("""
    - Implementação do fluxo de processos conforme definido.
    - Acompanhamento diário das atividades e ajustes conforme necessário.
    """)

    st.subheader("Fase 4: Avaliação")
    st.markdown("""
    - Revisão semanal do desempenho do projeto com base nos KPIs.
    - Feedback contínuo entre os membros da equipe para melhoria contínua.
    """)

    st.subheader("Conclusão")
    st.markdown("""
    A implementação deste projeto visa não apenas melhorar a eficiência logística, 
    mas também proporcionar uma melhor experiência para os clientes internos, garantindo que os produtos estejam sempre disponíveis e sejam entregues pontualmente. A colaboração e a comunicação eficiente entre os membros da equipe serão fundamentais para o sucesso deste projeto.
    """)

    # Sistema de Metas e Bônus
    st.header("Sistema de Metas e Bônus")

    st.subheader("Gestor de Compras")
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

    st.subheader("Assistente de Estoque - Interno")
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

    st.subheader("Assistente de Estoque - Externo")
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

    st.subheader("Time de Reposição")
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

    st.subheader("Time de Produção")
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

    if st.button('Salvar Página em HTML'):
        # Conteúdo HTML
        html_content = """
        <html>
        <head>
        <title>Implementação do Projeto</title>
        </head>
        <body>
        <h1>Implementação do Projeto</h1>

        <h2>Fase 1: Planejamento</h2>
        <ul>
        <li>Reunião inicial com todos os membros da equipe para discutir o projeto.</li>
        <li>Definição de KPIs (Key Performance Indicators) para monitorar o desempenho do projeto.</li>
        </ul>

        <h2>Fase 2: Treinamento</h2>
        <ul>
        <li>Treinamento do Gestor de Compras em análise de mercado e negociação com fornecedores.</li>
        <li>Treinamento do Assistente de Estoque em técnicas de organização e controle de inventário.</li>
        <li>Treinamento do Responsável pela Saída de Produtos em logística e atendimento ao cliente.</li>
        </ul>

        <h2>Fase 3: Execução</h2>
        <ul>
        <li>Implementação do fluxo de processos conforme definido.</li>
        <li>Acompanhamento diário das atividades e ajustes conforme necessário.</li>
        </ul>

        <h2>Fase 4: Avaliação</h2>
        <ul>
        <li>Revisão semanal do desempenho do projeto com base nos KPIs.</li>
        <li>Feedback contínuo entre os membros da equipe para melhoria contínua.</li>
        </ul>

        <h2>Conclusão</h2>
        <p>A implementação deste projeto visa não apenas melhorar a eficiência logística, 
        mas também proporcionar uma melhor experiência para os clientes internos, garantindo que os produtos estejam sempre disponíveis e sejam entregues pontualmente. A colaboração e a comunicação eficiente entre os membros da equipe serão fundamentais para o sucesso deste projeto.</p>

        <h1>Sistema de Metas e Bônus</h1>

        <h2>Gestor de Compras</h2>
        <h3>KPIs:</h3>
        <ul>
        <li>Precisão nas Previsões de Compras</li>
        <li>Custo por Unidade Comprada</li>
        <li>Tempo de Ciclo de Compras</li>
        <li>Índice de Qualidade de Fornecedores</li>
        </ul>
        <h3>Metas e Bônus:</h3>
        <ul>
        <li>Manter a diferença de previsão abaixo de <b>5%</b> (<i>10% do salário</i>)</li>
        <li>Reduzir o custo médio em <b>5%</b> (<i>5% do salário</i>)</li>
        <li>Reduzir o tempo de ciclo em <b>10%</b> (<i>5% do salário</i>)</li>
        <li>Manter a qualidade acima de <b>95%</b> (<i>5% do salário</i>)</li>
        </ul>

        <h2>Assistente de Estoque - Interno</h2>
        <h3>KPIs:</h3>
        <ul>
        <li>Precisão do Inventário</li>
        <li>Tempo de Processamento de Recebimento</li>
        <li>Nível de Organização do Estoque</li>
        <li>Rotatividade de Estoque</li>
        </ul>
        <h3>Metas e Bônus:</h3>
        <ul>
        <li>Manter a precisão acima de <b>98%</b> (<i>10% do salário</i>)</li>
        <li>Reduzir o tempo em <b>15%</b> (<i>5% do salário</i>)</li>
        <li>Receber avaliações positivas acima de <b>90%</b> (<i>5% do salário</i>)</li>
        <li>Aumentar a rotatividade em <b>10%</b> (<i>5% do salário</i>)</li>
        </ul>

        <h2>Assistente de Estoque - Externo</h2>
        <h3>KPIs:</h3>
        <ul>
        <li>Precisão no Atendimento de Pedidos</li>
        <li>Tempo de Processamento de Pedidos</li>
        <li>Satisfação do Cliente</li>
        <li>Índice de Devoluções</li>
        </ul>
        <h3>Metas e Bônus:</h3>
        <ul>
        <li>Manter a precisão acima de <b>99%</b> (<i>10% do salário</i>)</li>
        <li>Reduzir o tempo em <b>20%</b> (<i>5% do salário</i>)</li>
        <li>Manter a satisfação acima de <b>95%</b> (<i>5% do salário</i>)</li>
        <li>Manter o índice abaixo de <b>2%</b> (<i>5% do salário</i>)</li>
        </ul>

        <h2>Time de Reposição</h2>
        <h3>KPIs:</h3>
        <ul>
        <li>Tempo de Reposição</li>
        <li>Organização Visual</li>
        <li>Disponibilidade de Produtos na Loja</li>
        </ul>
        <h3>Metas e Bônus:</h3>
        <ul>
        <li>Reduzir o tempo em <b>15%</b> (<i>5% do salário</i>)</li>
        <li>Receber avaliações positivas acima de <b>90%</b> (<i>5% do salário</i>)</li>
        <li>Manter a disponibilidade acima de <b>98%</b> (<i>10% do salário</i>)</li>
        </ul>

        <h2>Time de Produção</h2>
        <h3>KPIs:</h3>
        <ul>
        <li>Qualidade da Embalagem</li>
        <li>Tempo de Embalagem</li>
        <li>Satisfação Interna</li>
        </ul>
        <h3>Metas e Bônus:</h3>
        <ul>
        <li>Manter a qualidade acima de <b>98%</b> (<i>10% do salário</i>)</li>
        <li>Reduzir o tempo em <b>20%</b> (<i>5% do salário</i>)</li>
        <li>Manter a satisfação interna acima de <b>95%</b> (<i>5% do salário</i>)</li>
        </ul>

        </body>
        </html>
        """

        # Salvar o conteúdo HTML em um arquivo
        with open("/Implementacao_do_Projeto.html", "w") as file:
            file.write(html_content)
        
        st.success('Página salva em HTML com sucesso!')
        st.markdown("[Baixar HTML](sandbox:/Implementacao_do_Projeto.html)")

if __name__ == "__main__":
    home()
