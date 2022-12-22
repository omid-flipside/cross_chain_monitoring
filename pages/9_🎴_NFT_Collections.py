# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Layout
st.set_page_config(page_title='NFT Collections - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🎴 NFT Collections')

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
        elif data_type == 'Collections Overview':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eaa5902c-0206-4fd7-8eb4-b15ecf9a71b4/data/latest')
        elif data_type == 'Collections Daily':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3cb9e6f6-849b-47e6-8c7e-b454e1394d6b/data/latest')
    return None

nfts_overview = get_data('NFTs', 'Overview')
nfts_daily = get_data('NFTs', 'Daily')
nfts_heatmap = get_data('NFTs', 'Heatmap')
nfts_marketplaces_overview = get_data('NFTs', 'Marketplaces Overview')
nfts_marketplaces_daily = get_data('NFTs', 'Marketplaces Daily')
nfts_collections_overview = get_data('NFTs', 'Collections Overview')
nfts_collections_daily = get_data('NFTs', 'Collections Daily')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=nfts_overview['Blockchain'].unique(),
    default=nfts_overview['Blockchain'].unique()
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    c1, c2 = st.columns(2)
    df = nfts_collections_overview.query('Blockchain == @options')
    with c1:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='Volume', color='Collection', title='Sales Volume of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='Sales', color='Collection', title='Sales of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='Buyers', color='Collection', title='Buyers of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='NFTs', color='Collection', title='Traded NFTs of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Volume', names='Collection', title='Share of Sales Volume of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Sales', names='Collection', title='Share of Sales of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Buyers', names='Collection', title='Share of Buyers of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='NFTs', names='Collection', title='Share of Traded NFTs of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader('Price')
    c1, c2 = st.columns(2)
    df = nfts_collections_overview.query('Blockchain == @options')
    with c1:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceAverage', color='Collection', title='Average Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceMax', color='Collection', title='Highest Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceMedian', color='Collection', title='Median Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceFloor', color='Collection', title='Floor Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    st.subheader('Overview')
    c1, c2 = st.columns(2)
    df = nfts_collections_overview.query('Blockchain == @options')
    with c1:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='Volume', color='Blockchain', title='Sales Volume of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='Sales', color='Blockchain', title='Sales of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='Buyers', color='Blockchain', title='Buyers of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='NFTs', color='Blockchain', title='Traded NFTs of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Volume', names='Collection', title='Share of Sales Volume of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Sales', names='Collection', title='Share of Sales of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Buyers', names='Collection', title='Share of Buyers of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='NFTs', names='Collection', title='Share of Traded NFTs of Each Collection')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader('Price')
    c1, c2 = st.columns(2)
    df = nfts_collections_overview.query('Blockchain == @options')
    with c1:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceAverage', color='Blockchain', title='Average Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceMax', color='Blockchain', title='Highest Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceMedian', color='Blockchain', title='Median Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Collection', y='PriceFloor', color='Blockchain', title='Floor Price of Top Collections', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)