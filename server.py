import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

st.image('2.jpg', caption="",
use_container_width=True)

#NAVEGAÇÃO ENTRE ARENAS

# Inicializa o estado da página, se necessário
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

# CSS para personalizar os botões
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007bff;
        color: white;
        border: 1px solid #007bff;
    }
    div.stButton > button:first-child:hover {
        background-color: #0056b3;
        border-color: #0056b3;
    }
    </style>""", unsafe_allow_html=True)

# Função para mudar a página atual
def change_page(page_name):
    st.session_state['page'] = page_name

# Título e botões de navegação na parte principal da página
st.title('')
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('Home', key='1'):
        change_page('Home')
with col2:
    if st.button('Arena MRV', key='2'):
        change_page('Arena MRV')
with col3:
    if st.button('Mineirão', key='3'):
        change_page('Mineirão')
with col4:
    if st.button('Independência', key='4'):
        change_page('Independência')

# Conteúdo da página baseado no estado
if st.session_state['page'] == 'Home':
    st.markdown("""
# Bem-vindo ao Sistema de Gestão de Arena do CPC

Este é um sistema inovador de gestão de arenas, projetado para otimizar a eficiência e eficácia do policiamento e da gestão de eventos. Através de uma interface intuitiva e recursos avançados, o sistema permite a realização de previsões de efetivo baseadas nas características específicas de cada evento.

Principais funcionalidades incluem:

- **Previsão de Efetivo:** Capaz de calcular o número ideal de efetivos necessários para um evento, considerando fatores como tamanho do público, tipo de evento, histórico de confrontos entre torcidas, e mais.
- **Controle de Faltas:** Monitoramento e gestão de faltas de pessoal, permitindo ajustes em tempo real para garantir cobertura adequada.
- **Análise de Cobertura Policial:** Avaliação da suficiência do policiamento para eventos específicos, assegurando a segurança de todos os participantes.
- **Custo de Emprego:** Ferramentas para o cálculo e monitoramento dos custos de emprego mensais e anuais, facilitando a gestão orçamentária.
- **Relatórios para Tomada de Decisão:** Geração de relatórios detalhados para auxiliar comandantes e gestores na tomada de decisões informadas sobre a alocação de recursos e estratégias de segurança.

Este sistema representa um passo significativo na direção de uma gestão de arenas mais segura, eficiente e econômica, proporcionando uma experiência melhor para todos os envolvidos. Abaixo temos as principais características do evento que serão escolhidas pelo gestor:
""", unsafe_allow_html=True)

    # Adicione aqui o conteúdo para a página Home

    st.markdown("## Etapas do Campeonato:")
    st.markdown("- CLASSIFICATÓRIA/PRIMEIRO TURNO BRASILEIRO = 1")
    st.markdown("- OITAVAS/DISPUTA POR VAGA NA LIBERTADORES/SEGUNDO TURNO BRASILEIRO = 2")
    st.markdown("- QUARTAS/DISPUTA CONTRA O REBAIXAMENTO NOS JOGOS INICIAIS/LIBERTADORES = 3")
    st.markdown("- SEMIFINAIS/DISPUTA PELA LIDERANÇA = 4")
    st.markdown("- FINAIS/DISPUTA PELO TÍTULO/REBAIXAMENTO NOS JOGOS FINAIS = 5")

    st.markdown("## Público Previsto:")
    st.markdown("- ATÉ 10 MIL = 1")
    st.markdown("- 10 A 20 MIL = 2")
    st.markdown("- 20 A 30 MIL = 3")
    st.markdown("- 30 A 40 MIL = 4")
    st.markdown("- MAIS DE 40 MIL = 5")

    st.markdown("## Tipo de Clássico:")
    st.markdown("- ESTADUAL = 2")
    st.markdown("- NACIONAL = 3")
    st.markdown("- INTERNACIONAL = 4")
    st.markdown("- ATLÉTICO X CRUZEIRO = 5")

    st.markdown("## Abrangência:")
    st.markdown("- FEMININO = 1")
    st.markdown("- AMISTOSO = 2")
    st.markdown("- ESTADUAL = 3")
    st.markdown("- NACIONAL = 4")
    st.markdown("- INTERNACIONAL = 5")

    st.markdown("## Animosidade entre Torcidas:")
    st.markdown("- CONVERGENTES: Fornece suporte, possuem alianças e não possuem histórico de confrontos. (CÓDIGO = 1)")
    st.markdown("- PARCIALMENTE CONVERGENTES: Possuem alianças “secundárias”, inibem conflitos com a torcida aliadas. (CÓDIGO = 2)")
    st.markdown("- NEUTRAS: Não possuem alianças e também não possuem histórico de confrontos. (CÓDIGO = 3)")
    st.markdown("- PARCIALMENTE DIVERGENTES: Pequena possibilidade de confronto, mas é derivada da oposição da torcida aliada. (CÓDIGO = 4)")
    st.markdown("- DIVERGENTES: Elevada possibilidade de confronto, com registro histórico de danos materiais, contra a vida e de reiterados confrontos. (CÓDIGO = 5)")

elif st.session_state['page'] == 'Arena MRV':
    st.header('GESTÃO POLICIAMENTO ARENA MRV')
    # Adicione aqui o conteúdo específico para a Arena MRV
    # Exibindo uma imagem local
    st.image("Arena-MRV.jpg", caption="ARENA MRV", use_container_width=True)

    # Loading dataset
    df1 = pd.read_excel(r'excel.xlsx', sheet_name='evento')
    df2 = pd.read_excel(r'excel.xlsx', sheet_name='efetivo')

    # Merge dos dataframes
    df = pd.merge(df1, df2, how='inner', on='EVENTOS')
    df = df[['FASE', 'PUBLICO', 'TIPO DE CLÁSSICO', 'ABRANGÊNCIA', 'TORCIDAS', 'EFETIVO_TOTAL', 'RISCO']]

    def user_input_features():
        fase = st.slider('Fase do campeonato', 1, 5, 3, 1)
        publico = st.slider('Previsão de público', 1, 5, 3, 1)
        classico = st.slider('Tipo de clássico', 1, 5, 3, 1)
        abrangencia = st.slider('Abrangência', 1, 5, 3, 1)
        animosidade = st.slider('Animosidade das torcidas', 1, 5, 3, 1)
        risco = st.slider('Risco', 0, 2, 1, 1)

        soma_valores = fase + publico + classico + abrangencia + animosidade + risco

        limite_risco_alto = 19
        limite_risco_medio = 14

        if soma_valores > limite_risco_alto:
            risco_texto = 'RISCO ALTO'
        elif soma_valores > limite_risco_medio:
            risco_texto = 'RISCO MÉDIO'
        else:
            risco_texto = 'RISCO BAIXO'

        st.write(f'**<div id="blink">{risco_texto}</div>**', unsafe_allow_html=True)
        st.markdown(
            """
            <script>
            setInterval(function() {
                var element = document.getElementById("blink");
                element.style.visibility = (element.style.visibility == "hidden" ? "" : "hidden");
            }, 500);
            </script>
            """,
            unsafe_allow_html=True)

        data = {'FASE': fase,
                'PUBLICO': publico,
                'TIPO DE CLÁSSICO': classico,
                'ABRANGÊNCIA': abrangencia,
                'TORCIDAS': animosidade,
                'RISCO': risco}
        features = pd.DataFrame(data, index=[0])
        return features

    # Define os coeficientes e o intercepto
    coeficientes = [8.89362227, 6.8963978, 28.04470843, -3.26093711, 9.09572461, -13.2836195]
    intercepto = -47.76714492193065

    with st.sidebar.expander("CARACTERÍSTICAS DO JOGO", expanded=True):
        features = user_input_features()

    # Calcula a previsão fora do expander
    previsao = (
        features['FASE'] * coeficientes[0] +
        features['PUBLICO'] * coeficientes[1] +
        features['TIPO DE CLÁSSICO'] * coeficientes[2] +
        features['ABRANGÊNCIA'] * coeficientes[3] +
        features['TORCIDAS'] * coeficientes[4] +
        features['RISCO'] * coeficientes[5] +
        intercepto
    ) * 1.1

    # Exibe a previsão
    st.subheader('PREVISÃO DO TAMANHO DO EFETIVO TOTAL')
    # Exibe a previsão com destaque
    st.markdown(f"<p style='font-size: 40px; color: red; animation: blink 1s linear infinite;'>{int(previsao.iloc[0])}</p>", unsafe_allow_html=True)

    # Exibindo uma imagem local
    st.write("""
    #  EFETIVO PRECURSOR - ARENA MRV
    """)
    st.image("imagem1.png", caption="SUGESTÃO DE ALOCAÇÃO DO EFETIVO PRECURSOR", use_container_width=True)
    st.write("""
    #  EFETIVO PRINCIPAL - ARENA MRV
    """)
    st.image("imagem2.png", caption="SUGESTÃO DE ALOCAÇÃO DO EFETIVO PRINCIPAL", use_container_width=True)

elif st.session_state['page'] == 'Mineirão':
    st.header('GESTÃO DE POLICIAMENTO DO MINEIRÃO')
    # Adicione aqui o conteúdo específico para o Mineirão
    st.image("mineirao.jpg", caption="MINEIRÃO", use_container_width=True)

    # Loading dataset
    df1 = pd.read_excel(r'excel.xlsx', sheet_name='evento')
    df2 = pd.read_excel(r'excel.xlsx', sheet_name='efetivo')

    # Merge dos dataframes
    df = pd.merge(df1, df2, how='inner', on='EVENTOS')
    df = df[['FASE', 'PUBLICO', 'TIPO DE CLÁSSICO', 'ABRANGÊNCIA', 'TORCIDAS', 'EFETIVO_TOTAL', 'RISCO']]

    def user_input_features():
        fase = st.slider('Fase do campeonato', 1, 5, 3, 1)
        publico = st.slider('Previsão de público', 1, 5, 3, 1)
        classico = st.slider('Tipo de clássico', 1, 5, 3, 1)
        abrangencia = st.slider('Abrangência', 1, 5, 3, 1)
        animosidade = st.slider('Animosidade das torcidas', 1, 5, 3, 1)
        risco = st.slider('Risco', 0, 2, 1, 1)

        soma_valores = fase + publico + classico + abrangencia + animosidade + risco

        limite_risco_alto = 19
        limite_risco_medio = 14

        if soma_valores > limite_risco_alto:
            risco_texto = 'RISCO ALTO'
        elif soma_valores > limite_risco_medio:
            risco_texto = 'RISCO MÉDIO'
        else:
            risco_texto = 'RISCO BAIXO'

        st.write(f'**<div id="blink">{risco_texto}</div>**', unsafe_allow_html=True)
        st.markdown(
            """
            <script>
            setInterval(function() {
                var element = document.getElementById("blink");
                element.style.visibility = (element.style.visibility == "hidden" ? "" : "hidden");
            }, 500);
            </script>
            """,
            unsafe_allow_html=True)

        data = {'FASE': fase,
                'PUBLICO': publico,
                'TIPO DE CLÁSSICO': classico,
                'ABRANGÊNCIA': abrangencia,
                'TORCIDAS': animosidade,
                'RISCO': risco}
        features = pd.DataFrame(data, index=[0])
        return features

    # Define os coeficientes e o intercepto
    coeficientes = [8.23479431, 8.98243907, 36.49594679, -23.27225007, 2.26144646, 1.16707685]
    intercepto = 46.66649154467534

    with st.sidebar.expander("CARACTERÍSTICAS DO JOGO", expanded=True):
        features = user_input_features()

    # Calcula a previsão fora do expander
    previsao = (
        features['FASE'] * coeficientes[0] +
        features['PUBLICO'] * coeficientes[1] +
        features['TIPO DE CLÁSSICO'] * coeficientes[2] +
        features['ABRANGÊNCIA'] * coeficientes[3] +
        features['TORCIDAS'] * coeficientes[4] +
        features['RISCO'] * coeficientes[5] +
        intercepto
    ) * 1.1

    # Exibe a previsão
    st.subheader('PREVISÃO DO TAMANHO DO EFETIVO TOTAL')
    # Exibe a previsão com destaque
    st.markdown(f"<p style='font-size: 40px; color: red; animation: blink 1s linear infinite;'>{int(previsao.iloc[0])}</p>", unsafe_allow_html=True)

    # Exibindo uma imagem local
    st.write("""
    #  EFETIVO PRECURSOR - MINEIRÃO
    """)
    st.image("mineirao_efetivo.jpg", caption="SUGESTÃO DE ALOCAÇÃO DO EFETIVO PRECURSOR", use_container_width=True)
    st.write("""
    #  EFETIVO PRINCIPAL - MINEIRÃO
    """)
    st.image("mineirao_efetivo.jpg", caption="SUGESTÃO DE ALOCAÇÃO DO EFETIVO PRINCIPAL", use_container_width=True)

elif st.session_state['page'] == 'Independência':
    st.header('GESTÃO DO POLICIAMENTO INDEPENDÊNCIA')
    # Adicione aqui o conteúdo específico para o Independência

    # Adicione aqui o conteúdo específico para o Mineirão
    st.image("independencia.jpg", caption="INDEPENDÊNCIA", use_container_width=True)

    # Loading dataset
    df1 = pd.read_excel(r'excel.xlsx', sheet_name='evento')
    df2 = pd.read_excel(r'excel.xlsx', sheet_name='efetivo')

    # Merge dos dataframes
    df = pd.merge(df1, df2, how='inner', on='EVENTOS')
    df = df[['FASE', 'PUBLICO', 'TIPO DE CLÁSSICO', 'ABRANGÊNCIA', 'TORCIDAS', 'EFETIVO_TOTAL', 'RISCO']]

    def user_input_features():
        fase = st.slider('Fase do campeonato', 1, 5, 3, 1)
        publico = st.slider('Previsão de público', 1, 5, 3, 1)
        classico = st.slider('Tipo de clássico', 1, 5, 3, 1)
        abrangencia = st.slider('Abrangência', 1, 5, 3, 1)
        animosidade = st.slider('Animosidade das torcidas', 1, 5, 3, 1)
        risco = st.slider('Risco', 0, 2, 1, 1)

        soma_valores = fase + publico + classico + abrangencia + animosidade + risco

        limite_risco_alto = 19
        limite_risco_medio = 14

        if soma_valores > limite_risco_alto:
            risco_texto = 'RISCO ALTO'
        elif soma_valores > limite_risco_medio:
            risco_texto = 'RISCO MÉDIO'
        else:
            risco_texto = 'RISCO BAIXO'

        st.write(f'**<div id="blink">{risco_texto}</div>**', unsafe_allow_html=True)
        st.markdown(
            """
            <script>
            setInterval(function() {
                var element = document.getElementById("blink");
                element.style.visibility = (element.style.visibility == "hidden" ? "" : "hidden");
            }, 500);
            </script>
            """,
            unsafe_allow_html=True)

        data = {'FASE': fase,
                'PUBLICO': publico,
                'TIPO DE CLÁSSICO': classico,
                'ABRANGÊNCIA': abrangencia,
                'TORCIDAS': animosidade,
                'RISCO': risco}
        features = pd.DataFrame(data, index=[0])
        return features

    # Define os coeficientes e o intercepto
    coeficientes = [-2.58259208, 14.11460157, 10.07816947, -2.08123554, 17.77963774, 1.06541478]
    intercepto = -48.38663257759625

    with st.sidebar.expander("CARACTERÍSTICAS DO JOGO", expanded=True):
        features = user_input_features()

    # Calcula a previsão fora do expander
    previsao = (
        features['FASE'] * coeficientes[0] +
        features['PUBLICO'] * coeficientes[1] +
        features['TIPO DE CLÁSSICO'] * coeficientes[2] +
        features['ABRANGÊNCIA'] * coeficientes[3] +
        features['TORCIDAS'] * coeficientes[4] +
        features['RISCO'] * coeficientes[5] +
        intercepto
    ) 

    # Exibe a previsão
    st.subheader('PREVISÃO DO TAMANHO DO EFETIVO TOTAL')
    # Exibe a previsão com destaque
    st.markdown(f"<p style='font-size: 40px; color: red; animation: blink 1s linear infinite;'>{int(previsao.iloc[0])}</p>", unsafe_allow_html=True)

    # Exibindo uma imagem local
    st.write("""
    #  EFETIVO PRECURSOR - INDEPENDÊNCIA
    """)
    st.image("independencia.jpg", caption="SUGESTÃO DE ALOCAÇÃO DO EFETIVO PRECURSOR", use_container_width=True)
    st.write("""
    #  EFETIVO PRINCIPAL - INDEPENDÊNCIA
    """)
    st.image("independencia.jpg", caption="SUGESTÃO DE ALOCAÇÃO DO EFETIVO PRINCIPAL", use_container_width=True)
