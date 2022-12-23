# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Layout
st.set_page_config(page_title='Swaps - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🔄 Swaps')

# Data Sources
@st.cache(ttl=10800)
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
    default=swaps_overview['Blockchain'].unique()
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = swaps_overview.query('Blockchain == @options')
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.metric(label='Swaps Volume', value=df['Volume'].round(), help='USD')
        st.metric(label='Volume/Day', value=df['Volume/Day'].round(), help='USD')
    with c2:
        st.metric(label='Swaps', value=df['Swaps'])
        st.metric(label='Swaps/Day', value=df['Swaps/Day'].round())
    with c3:
        st.metric(label='Swappers', value=df['Swappers'])
        st.metric(label='Swappers/Day', value=df['Swappers/Day'].round())
    with c4:
        st.metric(label='Volume/Swapper', value=df['Volume/Swapper'].round(), help='USD')
        st.metric(label='Swaps/Swapper', value=df['Swaps/Swapper'].round(2))
    with c5:
        st.metric(label='Average Swap Amount', value=df['AmountAverage'].round(2), help='USD')
        st.metric(label='Median Swap Amount', value=df['AmountMedian'].round(2), help='USD')
    
    st.subheader('Swaps Over Time')
    df = swaps_daily.query('Blockchain == @options')

    fig = px.area(df, x='Date', y='Volume', title='Daily Volume of Swaps')
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Swaps'], name='Swaps'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Swappers'], name='Swappers'), secondary_y=True)
        fig.update_layout(title_text='Daily Swaps and Swappers')
        fig.update_yaxes(title_text='Swaps', secondary_y=False)
        fig.update_yaxes(title_text='Swappers', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['AmountAverage'], name='Average'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['AmountMedian'], name='Median'), secondary_y=True)
        fig.update_layout(title_text='Daily Average and Median Swap Amount')
        fig.update_yaxes(title_text='Average', secondary_y=False)
        fig.update_yaxes(title_text='Median', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Heatmap')
    df = swaps_heatmap.query('Blockchain == @options')
    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(df, x='Hour', y='Day', size='Volume', color='Volume', title='Heatmap of Swaps Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='AmountAverage', color='AmountAverage', title='Heatmap of Average Swap Amount')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.scatter(df, x='Hour', y='Day', size='Swaps', color='Swaps', title='Heatmap of Swaps')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Hour', y='Day', size='Swappers', color='Swappers', title='Heatmap of Swappers')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    subtab_overview, subtab_heatmap = st.tabs(['Overview', 'Heatmap'])
    with subtab_overview:
        st.subheader('Overview of Swaps')
        df = swaps_overview.query('Blockchain == @options')
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Volume', color='Blockchain', title='Total Swaps Volume', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Volume', names='Blockchain', title='Share of Total Swaps Volume')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Volume/Day', color='Blockchain', title='Average Swaps Volume/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            fig = px.bar(df, x='Blockchain', y='Swaps', color='Blockchain', title='Total Swaps', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Swaps', names='Blockchain', title='Share of Total Swaps')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Swaps/Day', color='Blockchain', title='Average Swaps/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c3:
            fig = px.bar(df, x='Blockchain', y='Swappers', color='Blockchain', title='Total Swappers', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(df, values='Swappers', names='Blockchain', title='Share of Total Swappers')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='Swappers/Day', color='Blockchain', title='Average Swappers/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df, x='Blockchain', y='Volume/Swapper', color='Blockchain', title='Average Volume/Swapper', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)
            
        with c2:
            fig = px.bar(df, x='Blockchain', y='Swaps/Swapper', color='Blockchain', title='Average Swaps/Swapper', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        st.subheader('Swap Amount')
        
        c1, c2 = st.columns([1, 2])
        with c1:
            fig = px.bar(df, x='Blockchain', y='AmountAverage', color='Blockchain', title='Average Swap Amount', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(df, x='Blockchain', y='AmountMedian', color='Blockchain', title='Median Swap Amount', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            df = swaps_daily.query('Blockchain == @options')

            fig = px.line(df, x='Date', y='AmountAverage', color='Blockchain', title='Daily Average Swap Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(df, x='Date', y='AmountMedian', color='Blockchain', title='Daily Median Swap Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader('Swaps Over Time')
        df = swaps_daily.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(df, x='Date', y='Volume', color='Blockchain', title='Daily Swaps Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(df, x='Date', y='Swaps', color='Blockchain', title='Daily Swaps')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(df, x='Date', y='Swappers', color='Blockchain', title='Daily Swappers')
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
            fig.update_layout(title='Daily Share of Swaps Volume')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Swaps'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swaps')
            st.plotly_chart(fig, use_container_width=True)

            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=df.query("Blockchain == @i")['Date'],
                    y=df.query("Blockchain == @i")['Swappers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Swappers')
            st.plotly_chart(fig, use_container_width=True)

    with subtab_heatmap:
        st.subheader('Heatmap of Swaps')
        df = swaps_heatmap.query('Blockchain == @options')
        c1, c2 = st.columns(2)
        with c1:
            fig = px.scatter(df, x='Volume', y='Day', color='Blockchain', title='Daily Heatmap of Swaps Volume', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Swaps', y='Day', color='Blockchain', title='Daily Heatmap of Swaps', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Swappers', y='Day', color='Blockchain', title='Daily Heatmap of Swappers', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='AmountAverage', y='Day', color='Blockchain', title='Daily Heatmap of Average Swap Amount', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.scatter(df, x='Volume', y='Hour', color='Blockchain', title='Hourly Heatmap of Swaps Volume', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Swaps', y='Hour', color='Blockchain', title='Hourly Heatmap of Swaps', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='Swappers', y='Hour', color='Blockchain', title='Hourly Heatmap of Swappers', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(df, x='AmountAverage', y='Hour', color='Blockchain', title='Hourly Heatmap of Average Swap Amount', log_x=True)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)