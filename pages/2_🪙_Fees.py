# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Layout
st.set_page_config(page_title='Fees - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🪙 Transaction Fess')

# Data Sources
@st.cache(ttl=10800)
def get_data(data_sector, data_type):
    if data_sector == 'Transactions':
        if data_type == 'Overview':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/579714e6-986e-421a-85dd-c32a8b41b25c/data/latest')
        elif data_type == 'Daily':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4e0c69ff-9395-43c1-af49-f590f864d339/data/latest')
        elif data_type == 'Heatmap':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9d8d54d4-b700-4d85-af17-8c29aa29d334/data/latest')
        elif data_type == 'Fee Payers':
            return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7eae69ea-2387-420d-b4b9-6eceeb5ef22d/data/latest')
    return None

transactions_overview = get_data('Transactions', 'Overview')
transactions_daily = get_data('Transactions', 'Daily')
transactions_heatmap = get_data('Transactions', 'Heatmap')
transactions_fee_payers = get_data('Transactions', 'Fee Payers')

# Filter the blockchains
options = st.multiselect(
    '**Select your desired blockchains:**',
    options=transactions_overview['Blockchain'].unique(),
    default=transactions_overview['Blockchain'].unique(),
    key='fees_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = transactions_overview.query("Blockchain == @options")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label='Total Fees', value=df['Fees'].round(), help='USD')
    with c2:
        st.metric(label='Fees/Block', value=df['Fees/Block'].round(6), help='USD')
    with c3:
        st.metric(label='Average Fee', value=df['FeeAverage'].round(6), help='USD')
    with c4:
        st.metric(label='Median Fee', value=df['FeeMedian'].round(6), help='USD')
    
    st.subheader('Activity Over Time')
    df = transactions_daily.query("Blockchain == @options")
    c1, c2 = st.columns(2)
    with c1:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Fees'], name='Total Fees'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Fees/Block'], name='Fees/Block'), secondary_y=True)
        fig.update_layout(title_text='Daily Total Fees and Average Fees/Block')
        fig.update_yaxes(title_text='Total Fees', secondary_y=False)
        fig.update_yaxes(title_text='Fees/Block', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['FeeAverage'], name='Average'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['FeeMedian'], name='Median'), secondary_y=True)
        fig.update_layout(title_text='Daily Average, and Median Fees')
        fig.update_yaxes(title_text='Average', secondary_y=False)
        fig.update_yaxes(title_text='Median', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Activity Heatmap')
    df = transactions_heatmap.query("Blockchain == @options")
    fig = px.scatter(df, x='Hour', y='Day', size='Fees', color='Fees', title='Heatmap of Fees')
    fig.update_layout(xaxis_title=None, yaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Top Fee Payers')
    df = transactions_fee_payers.query("Blockchain == @options")
    fig = px.bar(df, x='User', y='Fees', color='User', title='Total Fees Paid By Top Fee Payers')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
    fig.update_xaxes(type='category')
    st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    st.subheader('Overview')
    c1, c2 = st.columns([1, 2])
    with c1:
        df = transactions_overview.query("Blockchain == @options")

        fig = px.bar(df, x='Blockchain', y='Fees', color='Blockchain', title='Total Fees', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.bar(df, x='Blockchain', y='FeeAverage', color='Blockchain', title='Average Fee Amount', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.bar(df, x='Blockchain', y='FeeMedian', color='Blockchain', title='Median Fee Amount', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        df = transactions_daily.query("Blockchain == @options")

        fig = px.line(df, x='Date', y='Fees', color='Blockchain', title='Daily Total Fees', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.line(df, x='Date', y='FeeAverage', color='Blockchain', title='Daily Average Fee Amount', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.line(df, x='Date', y='FeeMedian', color='Blockchain', title='Daily Median Fee Amount', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader('Activity Heatmap')
    c1, c2 = st.columns(2)
    with c1:
        df = transactions_heatmap.query("Blockchain == @options").round()

        fig = px.scatter(df, x='Fees', y='Day', color='Blockchain', title='Daily Heatmap of Fees', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.scatter(df, x='Fees', y='Hour', color='Blockchain', title='Hourly Heatmap of Fees', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)