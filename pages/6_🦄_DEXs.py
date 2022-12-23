# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Layout
st.set_page_config(page_title='DEXs - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🦄 DEXs')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
@st.cache(ttl=600)
def get_data(data):
    if data == 'Swaps Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b3d90320-3fcb-44f0-b0b9-3f72ee779dcb/data/latest')
    elif data == 'Swaps Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fed187af-6c8e-49fc-82d1-1975926e3951/data/latest')
    elif data == 'Swaps Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3fa50926-77bc-44f8-b190-7bd48d408c85/data/latest')
    elif data == 'Swaps DEXs Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9e0dace3-69d7-44fb-810c-e3b819b2b8de/data/latest')
    elif data == 'Swaps DEXs Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5563d79a-a937-4e04-a74e-b75f284c57cb/data/latest')
    elif data == 'Swaps Types Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/770cc6a0-bc32-49fb-942b-84c82da5a533/data/latest')
    elif data == 'Swaps Types Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3ec65249-62fe-49e6-bf85-513af7896e34/data/latest')
    return None

swaps_overview = get_data('Swaps Overview')
swaps_daily = get_data('Swaps Daily')
swaps_heatmap = get_data('Swaps Heatmap')
swaps_dexs_overview = get_data('Swaps DEXs Overview')
swaps_dexs_daily = get_data('Swaps DEXs Daily')
swaps_types_overview = get_data('Swaps Types Overview')
swaps_types_daily = get_data('Swaps Types Daily')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=swaps_overview['Blockchain'].unique(),
    default=swaps_overview['Blockchain'].unique(),
    key='dexs_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    subtab_overview, subtab_shares, subtab_amount = st.tabs(['Overview', 'Market Shares', 'Swap Amount'])
    with subtab_overview:
        c1, c2 = st.columns([1, 2])
        with c1:
            df = swaps_dexs_overview.query('Blockchain == @options')

            fig = px.histogram(df, x='DEX', y='Volume', color='DEX', title='Swaps Volume of Each DEX', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='DEX', y='Swaps', color='DEX', title='Swaps of Each DEX', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='DEX', y='Swappers', color='DEX', title='Swappers of Each DEX', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            df = swaps_dexs_daily.query('Blockchain == @options')

            fig = px.line(df, x='Date', y='Volume', color='DEX', title='Daily Swaps Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='Swaps', color='DEX', title='Daily Swaps')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='Swappers', color='DEX', title='Daily Swappers')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
    
    with subtab_shares:
        c1, c2 = st.columns([1, 2])
        with c1:
            df = swaps_dexs_overview.query('Blockchain == @options')

            fig = px.pie(df, values='Volume', names='DEX', title='Share of Swaps Volume of Each DEX')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Swaps', names='DEX', title='Share of Swaps of Each DEX')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Swappers', names='DEX', title='Share of Swappers of Each DEX')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            df = swaps_dexs_daily.query('Blockchain == @options')

            fig = go.Figure()
            for i in df['DEX'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("DEX == @i")['Date'],
                    y=df.query("DEX == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps Volume')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in df['DEX'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("DEX == @i")['Date'],
                    y=df.query("DEX == @i")['Swaps'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in df['DEX'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("DEX == @i")['Date'],
                    y=df.query("DEX == @i")['Swappers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swappers')
            st.plotly_chart(fig, use_container_width=True)
    
    with subtab_amount:
        c1, c2 = st.columns([1, 2])
        with c1:
            df = swaps_dexs_overview.query('Blockchain == @options')

            fig = px.histogram(df, x='DEX', y='AmountAverage', color='DEX', title='Average Swap Amount of Each DEX', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='DEX', y='AmountMedian', color='DEX', title='Median Swap Amount of Each DEX', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            df = swaps_dexs_daily.query('Blockchain == @options')

            fig = px.line(df, x='Date', y='AmountAverage', color='DEX', title='Daily Average Swap Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='AmountMedian', color='DEX', title='Daily Median Swap Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    st.subheader('Overview')
    df = swaps_dexs_overview.query('Blockchain == @options')
    c1, c2, c3 = st.columns(3)
    with c1:
        fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='DEX', y='Volume', color='Blockchain', title='Swaps Volume of Top DEXs', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df, values='Volume', names='DEX', title='Share of Swaps Volume of Each DEX')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.histogram(df.sort_values('Swaps', ascending=False).head(20), x='DEX', y='Swaps', color='Blockchain', title='Swaps of Top DEXs', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df, values='Swaps', names='DEX', title='Share of Swaps of Each DEX')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)
    with c3:
        fig = px.histogram(df.sort_values('Swappers', ascending=False).head(20), x='DEX', y='Swappers', color='Blockchain', title='Swappers of Top DEXs', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(df, values='Swappers', names='DEX', title='Share of Swappers of Each DEX')
        fig.update_layout(showlegend=False)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Swap Amount')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.histogram(df.sort_values('AmountAverage', ascending=False).head(20), x='DEX', y='AmountAverage', color='Blockchain', title='Average Swap Amount of Top DEXs', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.histogram(df.sort_values('AmountMedian', ascending=False).head(20), x='DEX', y='AmountMedian', color='Blockchain', title='Median Swap Amount of Top DEXs', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)