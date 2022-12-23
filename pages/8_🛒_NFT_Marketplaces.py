# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Layout
st.set_page_config(page_title='NFT Marketplaces - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🛒 NFT Marketplaces')

# Data Sources
@st.cache(ttl=10800)
def get_data(data_sector, data_type):
    if data_sector == 'NFTs':
        if data_type == 'Overview':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a9dee9b9-bfd8-4fed-b49b-a03767306d89/data/latest')
        elif data_type == 'Daily':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6ec4aca1-3d25-4233-bec2-0443b27d3e6c/data/latest')
        elif data_type == 'Heatmap':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/62fa2182-ca1b-4648-a363-8d1ce591253e/data/latest')
        elif data_type == 'Marketplaces Overview':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8f4e8520-52af-4d57-b29e-e513f62f8fa9/data/latest')
        elif data_type == 'Marketplaces Daily':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8fcca211-4bc6-444d-8696-0a583e2966a6/data/latest')
    return None

nfts_overview = get_data('NFTs', 'Overview')
nfts_daily = get_data('NFTs', 'Daily')
nfts_heatmap = get_data('NFTs', 'Heatmap')
nfts_marketplaces_overview = get_data('NFTs', 'Marketplaces Overview')
nfts_marketplaces_daily = get_data('NFTs', 'Marketplaces Daily')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=nfts_overview['Blockchain'].unique(),
    default=nfts_overview['Blockchain'].unique(),
    key='marketplaces_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    c1, c2 = st.columns([1, 2])
    with c1:
        df = nfts_marketplaces_overview.query('Blockchain == @options')

        fig = px.histogram(df, x='Marketplace', y='Volume', color='Marketplace', title='Sales Volume of Each Marketplace', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df, x='Marketplace', y='Sales', color='Marketplace', title='Sales of Each Marketplace', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df, x='Marketplace', y='Buyers', color='Marketplace', title='Buyers of Each Marketplace', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df, x='Marketplace', y='NFTs', color='Marketplace', title='Traded NFTs of Each Marketplace', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        df = nfts_marketplaces_daily.query('Blockchain == @options')

        fig = px.line(df, x='Date', y='Volume', color='Marketplace', title='Daily Sales Volume of Each Marketplace', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
        
        fig = px.line(df, x='Date', y='Sales', color='Marketplace', title='Daily Sales of Each Marketplace', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
        
        fig = px.line(df, x='Date', y='Buyers', color='Marketplace', title='Daily Buyers of Each Marketplace', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
        
        fig = px.line(df, x='Date', y='NFTs', color='Marketplace', title='Daily Traded NFTs of Each Marketplace', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Market Shares')
    c1, c2 = st.columns([1, 2])
    with c1:
        df = nfts_marketplaces_overview.query('Blockchain == @options')

        fig = px.pie(df, values='Volume', names='Marketplace', title='Share of Sales Volume of Each Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df, values='Sales', names='Marketplace', title='Share of Sales of Each Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df, values='Buyers', names='Marketplace', title='Share of Buyers of Each Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df, values='NFTs', names='Marketplace', title='Share of Traded NFTs of Each Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        df = nfts_marketplaces_daily.query('Blockchain == @options')

        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['Volume'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Sales Volume of Each Marketplace')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['Sales'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Sales of Each Marketplace')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['Buyers'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Buyers of Each Marketplace')
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        for i in df['Marketplace'].unique():
            fig.add_trace(go.Scatter(
                name=i,
                x=df.query("Marketplace == @i")['Date'],
                y=df.query("Marketplace == @i")['NFTs'],
                mode='lines',
                stackgroup='one',
                groupnorm='percent'
            ))
        fig.update_layout(title='Daily Share of Traded NFTs of Each Marketplace')
        st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    st.subheader('Overview')
    df = nfts_marketplaces_overview.query('Blockchain == @options')
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Marketplace', y='Volume', color='Blockchain', title='Sales Volume of Top marketplaces', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.histogram(df.sort_values('Sales', ascending=False).head(20), x='Marketplace', y='Sales', color='Blockchain', title='Sales of Top Marketplace', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)
    with c3:
        fig = px.histogram(df.sort_values('Buyers', ascending=False).head(20), x='Marketplace', y='Buyers', color='Blockchain', title='Buyers of Top Marketplace', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)
    with c4:
        fig = px.histogram(df.sort_values('NFTs', ascending=False).head(20), x='Marketplace', y='NFTs', color='Blockchain', title='Traded NFTs of Top Marketplace', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
        fig.update_xaxes(categoryorder='total ascending')
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Market Shares')
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        fig = px.pie(df, values='Volume', names='Marketplace', title='Share of Sales Volume of Top Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig = px.pie(df, values='Sales', names='Marketplace', title='Share of Sales of Top Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

    with c3:
        fig = px.pie(df, values='Buyers', names='Marketplace', title='Share of Buyers of Top Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)
    
    with c4:
        fig = px.pie(df, values='NFTs', names='Marketplace', title='Share of Traded NFTs of Top Marketplace')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)