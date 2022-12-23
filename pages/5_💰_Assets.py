# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Layout
st.set_page_config(page_title='Swapped Assets - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('💰 Swapped Assets')

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
    elif data == 'Swaps Assets Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/060d6f19-6e02-4be3-b262-05a91e694986/data/latest')
    elif data == 'Swaps Assets Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0139649d-6c38-4ee6-9e20-fff34e452fe6/data/latest')
    return None

swaps_overview = get_data('Swaps Overview')
swaps_daily = get_data('Swaps Daily')
swaps_heatmap = get_data('Swaps Heatmap')
swaps_dexs_overview = get_data('Swaps DEXs Overview')
swaps_dexs_daily = get_data('Swaps DEXs Daily')
swaps_types_overview = get_data('Swaps Types Overview')
swaps_types_daily = get_data('Swaps Types Daily')
swaps_assets_overview = get_data('Swaps Assets Overview')
swaps_assets_daily = get_data('Swaps Assets Daily')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=swaps_overview['Blockchain'].unique(),
    default=swaps_overview['Blockchain'].unique(),
    key='assets_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    subtab_types, subtab_assets = st.tabs(['Asset Types', 'Swapping To Assets'])
    with subtab_types:
        st.subheader('Overview')
        df = swaps_types_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.histogram(df, x='Type', y='Volume', color='Type', title='Total Volume of Each Asset Type')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Volume', names='Type', title='Share of Swaps Volume of Each Asset Type')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Type', y='Volume/Day', color='Type', title='Average Volume/Day of Each Asset Type')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.histogram(df, x='Type', y='Swaps', color='Type', title='Total Swaps of Each Asset Type')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Swaps', names='Type', title='Share of Swaps of Each Asset Type')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Type', y='Swaps/Day', color='Type', title='Average Swaps/Day of Each Asset Type')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c3:
            fig = px.histogram(df, x='Type', y='Swappers', color='Type', title='Total Swappers of Each Asset Type')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Swappers', names='Type', title='Share of Swappers of Each Asset Type')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Type', y='Swappers/Day', color='Type', title='Average Swappers/Day of Each Asset Type')
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        st.subheader('Swaps Over Time')
        c1, c2 = st.columns(2)
        df = swaps_types_daily.query('Blockchain == @options')
        with c1:
            fig = px.line(df, x='Date', y='Volume', color='Type', title='Daily Average Swaps Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='Swaps', color='Type', title='Daily Average Swaps')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='Swappers', color='Type', title='Daily Swappers')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = go.Figure()
            for i in df['Type'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Type == @i")['Date'],
                    y=df.query("Type == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps Volume')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in df['Type'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Type == @i")['Date'],
                    y=df.query("Type == @i")['Swaps'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps')
            st.plotly_chart(fig, use_container_width=True)

            fig = go.Figure()
            for i in df['Type'].unique():
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Type == @i")['Date'],
                    y=df.query("Type == @i")['Swappers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swappers')
            st.plotly_chart(fig, use_container_width=True)

        st.subheader('Swap Amount')
        c1, c2 = st.columns([1, 2])
        with c1:
            fig = px.histogram(df, x='Type', y='AmountAverage', color='Type', title='Average Swap Amount of Each Asset Type', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Type', y='AmountMedian', color='Type', title='Median Swap Amount of Each Asset Type', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            df = swaps_types_daily.query('Blockchain == @options')
            fig = px.line(df, x='Date', y='AmountAverage', color='Type', title='Daily Average Swap Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
            
            fig = px.line(df, x='Date', y='AmountMedian', color='Type', title='Daily Median Swap Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
    
    with subtab_assets:
        st.subheader('Overview')
        df = swaps_assets_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Asset', y='Volume', color='Asset', title='Swaps Volume of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Volume', names='Asset', title='Share of Total Swaps Volume of Top Assets')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.histogram(df.sort_values('Swaps', ascending=False).head(20), x='Asset', y='Swaps', color='Asset', title='Swaps of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df.sort_values('Swaps', ascending=False).head(20), values='Swaps', names='Asset', title='Share of Total Swaps of Top Assets')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        with c3:
            fig = px.histogram(df.sort_values('Swappers', ascending=False).head(20), x='Asset', y='Swappers', color='Asset', title='Swappers of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df.sort_values('Swappers', ascending=False).head(20), values='Swappers', names='Asset', title='Share of Total Swappers of Top Assets')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader('Swap Amount')
        df = swaps_assets_overview.query('Blockchain == @options').sort_values('Swaps', ascending=False).head(20)
        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df, x='Asset', y='AmountAverage', color='Asset', title='Average Swap Amount of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.bar(df, x='Asset', y='AmountMedian', color='Asset', title='Median Swap Amount of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    subtab_types, subtab_assets = st.tabs(['Asset Types', 'Swapping To Assets'])
    with subtab_types:
        st.subheader('Overview')
        df = swaps_types_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.pie(df, values='Volume', names='Type', title='Share of Total Swaps Volume of Each Asset Type')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.pie(df, values='Swaps', names='Type', title='Share of Total Swaps of Each Asset Type')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        with c3:
            fig = px.pie(df, values='Swappers', names='Type', title='Share of Total Swappers of Each Asset Type')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

        st.subheader('Blockchains')
        c1, c2 = st.columns([2, 1])
        with c1:
            fig = px.histogram(df, x='Blockchain', y='Volume', color='Type', title='Swaps Volume of Each Asset Type', log_y=True, barmode='group')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Blockchain', y='Swaps', color='Type', title='Swaps of Each Asset Type', log_y=True, barmode='group')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Blockchain', y='Swappers', color='Type', title='Swappers of Each Asset Type', log_y=True, barmode='group')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            fig = px.histogram(df, x='Blockchain', y='Volume', color='Type', title='Share of Swaps Volume of Each Asset Type', log_y=True, barnorm='percent')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Blockchain', y='Swaps', color='Type', title='Share of Swaps of Each Asset Type', log_y=True, barnorm='percent')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.histogram(df, x='Blockchain', y='Swappers', color='Type', title='Share of Swappers of Each Asset Type', log_y=True, barnorm='percent')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

    with subtab_assets:
        st.subheader('Overview')
        df = swaps_assets_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.histogram(df.sort_values('Volume', ascending=False).head(20), x='Asset', y='Volume', color='Blockchain', title='Swaps Volume of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df.sort_values('Volume', ascending=False).head(20), values='Volume', names='Asset', title='Share of Total Swaps Volume of Top Assets')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.histogram(df.sort_values('Swaps', ascending=False).head(20), x='Asset', y='Swaps', color='Blockchain', title='Swaps of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df.sort_values('Swaps', ascending=False).head(20), values='Swaps', names='Asset', title='Share of Total Swaps of Top Assets')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        with c3:
            fig = px.histogram(df.sort_values('Swappers', ascending=False).head(20), x='Asset', y='Swappers', color='Blockchain', title='Swappers of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df.sort_values('Swappers', ascending=False).head(20), values='Swappers', names='Asset', title='Share of Total Swappers of Top Assets')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader('Swap Amount')
        df = swaps_assets_overview.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df.sort_values('Swaps', ascending=False).head(20), x='Asset', y='AmountAverage', color='Blockchain', title='Average Swap Amount of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.bar(df.sort_values('Swaps', ascending=False).head(20), x='Asset', y='AmountMedian', color='Blockchain', title='Median Swap Amount of Top Assets', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)