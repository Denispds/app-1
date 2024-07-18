import streamlit as st

def home():
    
    # Título do Projeto
    st.header("Projeto de Implementação de Logística para Empresa de Acessórios Femininos")

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
    - definir e autorizar as compras de ensumos verniz .
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
    - Gestão produtos enviados loja 44 - cadastros e confirmaçao de preços - pedidos enviados .
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
    st.subheader("5. auxiliar de Produção")
    st.markdown("""
    **Responsabilidades:**
    - Colocar os produtos em embalagens , cartelas , preço , ganchos .
    - Preparar os produtos para serem enviados ou expostos na loja.

    **Atividades:**
    - Embalar os produtos conforme os padrões de qualidade estabelecidos.
    - Garantir que os produtos estejam prontos para serem enviados ou expostos na loja.
    - Trabalhar em conjunto com o time de reposição para garantir que os produtos estejam prontos para exposição.
    """)
    
    
    
    
    
    """)

if __name__ == "__main__":
    home()
