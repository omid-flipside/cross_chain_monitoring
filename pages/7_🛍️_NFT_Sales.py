# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Layout
st.set_page_config(page_title='NFTs - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🛍️ NFT Sales')

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
    default=nfts_overview['Blockchain'].unique()
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = nfts_overview.query('Blockchain == @options')
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1:
        st.metric(label='Volume', value=df['Volume'].round(), help='USD')
        st.metric(label='Volume/Day', value=df['Volume/Day'].round(), help='USD')
        st.metric(label='Volume/Buyer', value=df['Volume/Buyer'].round(), help='USD')
    with c2:
        st.metric(label='Sales', value=df['Sales'])
        st.metric(label='Sales/Day', value=df['Sales/Day'].round())
        st.metric(label='Sales/Buyer', value=df['Sales/Buyer'].round())
    with c3:
        st.metric(label='Buyers', value=df['Buyers'])
        st.metric(label='Buyers/Day', value=df['Buyers/Day'].round())
        st.metric(label='Volume/Collection', value=df['Volume/Collection'].round(), help='USD')
    with c4:
        st.metric(label='NFTs', value=df['NFTs'])
        st.metric(label='NFTs/Day', value=df['NFTs/Day'].round())
        st.metric(label='NFTs/Buyer', value=df['NFTs/Buyer'].round(2))
    with c5:
        st.metric(label='Collections', value=df['Collections'])
        st.metric(label='Collections/Day', value=df['Collections/Day'].round())
        st.metric(label='Collections/Buyer', value=df['Collections/Buyer'].round(2))
    with c6:
        st.metric(label='Marketplaces', value=df['Marketplaces'])
        st.metric(label='NFTs/Sale', value=df['NFTs/Sale'].round(2))
        st.metric(label='NFTs/Collection', value=df['NFTs/Collection'].round())

    st.subheader('Sales Over Time')
    df = nfts_daily.query('Blockchain == @options')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.area(df, x='Date', y='Volume', title='Daily Sales Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['PriceAverage'], name='Average'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['PriceMedian'], name='Median'), secondary_y=True)
        fig.update_layout(title_text='Daily Average and Median NFT Prices')
        fig.update_yaxes(title_text='Average', secondary_y=False)
        fig.update_yaxes(title_text='Median', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Sales'], name='Sales'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Buyers'], name='Buyers'), secondary_y=True)
        fig.update_layout(title_text='Daily Sales and Buyers')
        fig.update_yaxes(title_text='Sales', secondary_y=False)
        fig.update_yaxes(title_text='Buyers', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)

        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['NFTs'], name='NFTs'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Collections'], name='Collections'), secondary_y=True)
        fig.update_layout(title_text='Daily Traded NFTs and Collections')
        fig.update_yaxes(title_text='NFTs', secondary_y=False)
        fig.update_yaxes(title_text='Collections', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)
        
    st.subheader('Activity Heatmap')
    df = nfts_heatmap.query('Blockchain == @options')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(df, x='Hour', y='Day', size='Volume', color='Volume', title='Heatmap of Sales Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='PriceAverage', color='PriceAverage', title='Heatmap of Average NFT Price')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='PriceMedian', color='PriceMedian', title='Heatmap of Median NFT Price')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='PriceMax', color='PriceMax', title='Heatmap of Maximum NFT Price')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.scatter(df, x='Hour', y='Day', size='Sales', color='Sales', title='Heatmap of Sales')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='Buyers', color='Buyers', title='Heatmap of Buyers')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='NFTs', color='Buyers', title='Heatmap of Traded NFTs')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='Collections', color='Buyers', title='Heatmap of Traded Collections')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    subtab_overview, subtab_prices, subtab_heatmap = st.tabs(['Overview', 'Prices', 'Heatmap'])
    with subtab_overview:
        st.subheader('Overview of Sales')
        df = nfts_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Volume', color='Blockchain', title='Total Sales Volume', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Sales', color='Blockchain', title='Total Sales', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Buyers', color='Blockchain', title='Total Buyers', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='NFTs', color='Blockchain', title='Total Traded NFTs', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Collections', color='Blockchain', title='Total Traded Collections', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            fig = px.pie(df, values='Volume', names='Blockchain', title='Share of Total Sales Volume')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Sales', names='Blockchain', title='Share of Total Sales')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Buyers', names='Blockchain', title='Share of Total Buyers')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='NFTs', names='Blockchain', title='Share of Total Traded NFTs')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Collections', names='Blockchain', title='Share of Total Traded Collections')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

        with c3:
            fig = px.bar(df, x='Blockchain', y='Volume/Day', color='Blockchain', title='Average Volume/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Sales/Day', color='Blockchain', title='Average Sales/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Buyers/Day', color='Blockchain', title='Average Buyers/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='NFTs/Day', color='Blockchain', title='Average NFTs/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Collections/Day', color='Blockchain', title='Average Collections/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader('Sales Over Time')
        df = nfts_daily.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(df, x='Date', y='Volume', color='Blockchain', title='Daily Sales Volume', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(df, x='Date', y='Sales', color='Blockchain', title='Daily Sales', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='Buyers', color='Blockchain', title='Daily Buyers', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='NFTs', color='Blockchain', title='Daily Traded NFTs', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='Collections', color='Blockchain', title='Daily Traded Collections', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Sales Volume')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Sales'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Sales')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Buyers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Buyers')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['NFTs'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Traded NFTs')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Collections'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Traded Collections')
            st.plotly_chart(fig, use_container_width=True)

    with subtab_prices:
        st.subheader('NFT Prices')
        c1, c2 = st.columns([1, 2])
        with c1:
            df = nfts_overview.query('Blockchain == @options')

            fig = px.bar(df, x='Blockchain', y='PriceAverage', color='Blockchain', title='Average NFT Price', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='PriceMedian', color='Blockchain', title='Median NFT Price', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='PriceMax', color='Blockchain', title='Maximum NFT Price', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            df = nfts_daily.query('Blockchain == @options')

            fig = px.line(df, x='Date', y='PriceAverage', color='Blockchain', title='Daily Average NFT Price', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(df, x='Date', y='PriceMedian', color='Blockchain', title='Daily Median NFT Price', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(df, x='Date', y='PriceMax', color='Blockchain', title='Daily Maximum NFT Price', log_y=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
    
    with subtab_heatmap:
        st.subheader('Heatmap of Sales')
        df = nfts_heatmap.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.scatter(df, x='Volume', y='Day', color='Blockchain', title='Daily Heatmap of Sales Volume', log_x=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Sales', y='Day', color='Blockchain', title='Daily Heatmap of Sales', log_x=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Buyers', y='Day', color='Blockchain', title='Daily Heatmap of Buyers', log_x=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='PriceAverage', y='Day', color='Blockchain', title='Daily Heatmap of Average NFT Price', log_x=True)
            fig.update_layout(xaxis_title='Average Price')
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.scatter(df, x='Volume', y='Hour', color='Blockchain', title='Hourly Heatmap of Sales Volume', log_x=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Sales', y='Hour', color='Blockchain', title='Hourly Heatmap of Sales', log_x=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Buyers', y='Hour', color='Blockchain', title='Hourly Heatmap of Buyers', log_x=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='PriceAverage', y='Hour', color='Blockchain', title='Hourly Heatmap of Average NFT Price', log_x=True)
            fig.update_layout(xaxis_title='Average Price')
            st.plotly_chart(fig, use_container_width=True)