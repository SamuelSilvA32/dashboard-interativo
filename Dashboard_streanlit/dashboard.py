import streamlit as st
import plotly.express as px
from dados import criar_dados

df = criar_dados()


# configuração
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide"

)

# Filtros na Sidebar
st.title("📊 Dashboard de Vendas")
st.markdown("---")

st.sidebar.header("Filtros")

meses_escolhidos = st.sidebar.multiselect(
    "Escolha os meses:",
    options=df['Mês'].tolist(),
    default=df['Mês'].tolist()
)

df_filtrado = df[df['Mês'].isin(meses_escolhidos)]

# Métricas Principais
col1, col2, col3 = st.columns(3)

with col1:
    total_vendas = df_filtrado['Vendas'].sum()
    st.metric(
        "💰 Vendas Totais", 
        f"R$ {total_vendas:,.0f}",
        f"+{12}%"
    )

with col2:
    total_clientes = df_filtrado['Clientes'].sum()
    st.metric(
        "👥 Clientes", 
        f"{total_clientes:,}",
        f"+{8}%"
    )

with col3:
    ticket_medio = total_vendas / total_clientes if total_clientes > 0 else 0
    st.metric(
        "🎫 Ticket Médio", 
        f"R$ {ticket_medio:.0f}",
        f"+{5}%"
    )

# Gráficos
# Duas colunas para os gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolução das Vendas")
    fig_vendas = px.line(
        df_filtrado, 
        x='Mês', 
        y='Vendas',
        markers=True,
        title="Vendas por Mês"
    )
    st.plotly_chart(fig_vendas, use_container_width=True)

with col2:
    st.subheader("Clientes por Mês")
    fig_clientes = px.bar(
        df_filtrado,
        x='Mês',
        y='Clientes',
        title="Base de Clientes",
        color='Clientes'
    )
    st.plotly_chart(fig_clientes, use_container_width=True)

#Comparação de Produtos
st.subheader("Performance por Produto")

# Reorganiza os dados para o gráfico
produtos_df = df_filtrado.melt(
    id_vars=['Mês'], 
    value_vars=['notebooks','smartphones','tvs'],
    var_name='Produto', 
    value_name='Vendas_Produto'
)

fig_produtos = px.bar(
    produtos_df,
    x='Mês',
    y='Vendas_Produto',
    color='Produto',
    barmode='group',
    title="Vendas por Produto"
)
st.plotly_chart(fig_produtos, use_container_width=True)

# Tabela de Dados
if st.checkbox("Mostrar dados detalhados"):
    st.dataframe(df_filtrado)
    
    # Botão para download
    csv = df_filtrado.to_csv(index=False)
    st.download_button(
        "📥 Baixar CSV",
        csv,
        "vendas.csv",
        "text/csv"
    )

# Widgets Interativos

st.subheader("Simulador de Receita")

col1, col2, col3 = st.columns(3)

with col1:
    preco = st.number_input("Preço unitário (R$)", 1, 1000, 50)

with col2:
    quantidade = st.number_input("Quantidade", 1, 10000, 100)

with col3:
    receita = preco * quantidade
    st.metric("Receita Total", f"R$ {receita:,.2f}")





