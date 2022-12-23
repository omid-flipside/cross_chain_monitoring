# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Layout
st.set_page_config(page_title='Maro - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')
st.title('🌍 Macro KPIs')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
@st.cache(ttl=600)
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
    key='macro_options'
)

# Selected Blockchain
if len(options) == 0:
    st.warning('Please select at least one blockchain to see the metrics.')

# Single chain Analysis
elif len(options) == 1:
    st.subheader('Overview')
    df = transactions_overview.query("Blockchain == @options")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label='Transactions', value=df['Transactions'])
        st.metric(label='TPS', value=df['TPS'].round(2))
    with c2:
        st.metric(label='Blocks', value=df['Blocks'])
        st.metric(label='Transactions/Block', value=df['Transactions/Block'].round(2))
    with c3:
        st.metric(label='Users', value=df['Users'])
        st.metric(label='Users/Day', value=df['Users/Day'].round())
    # with c4:
    #     st.metric(label='Fees', value=df['Fees'].round(), help='USD')
    #     st.metric(label='Fees/Block', value=df['Fees/Block'].round(6), help='USD')
    # with c5:
    #     st.metric(label='Average Fee', value=df['FeeAverage'].round(6), help='USD')
    #     st.metric(label='Median Fee', value=df['FeeMedian'].round(6), help='USD')
    
    st.subheader('Activity Over Time')
    df = transactions_daily.query("Blockchain == @options")
    c1, c2 = st.columns(2)
    with c1:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Transactions'], name='Transactions'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Blocks'], name='Blocks'), secondary_y=True)
        fig.update_layout(title_text='Daily Total Transactions and Blocks')
        fig.update_yaxes(title_text='Transactions', secondary_y=False)
        fig.update_yaxes(title_text='Blocks', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)

        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['TPS'], name='TPS'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Transactions/Block'], name='Transactions/Block'), secondary_y=True)
        fig.update_layout(title_text='Daily TPS and Transactions/Block')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        fig.update_yaxes(title_text='Transactions/Block', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.area(df, x='Date', y='Users', title='Daily Active Addresses')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Fees'], name='Total'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['FeeAverage'], name='Average'), secondary_y=True)
        fig.add_trace(go.Line(x=df['Date'], y=df['FeeMedian'], name='Median'), secondary_y=True)
        fig.update_layout(title_text='Daily Total, Average, and Median Fees')
        fig.update_yaxes(title_text='Total', secondary_y=False)
        fig.update_yaxes(title_text='Average and Median', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Activity Heatmap')
    df = transactions_heatmap.query("Blockchain == @options")
    fig = px.scatter(df, x='Hour', y='Day', size='Transactions', color='Transactions', title='Heatmap of Transactions')
    fig.update_layout(xaxis_title=None, yaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)
    fig = px.scatter(df, x='Hour', y='Day', size='Blocks', color='Blocks', title='Heatmap of Blocks')
    fig.update_layout(xaxis_title=None, yaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)
    fig = px.scatter(df, x='Hour', y='Day', size='Users', color='Users', title='Heatmap of Users')
    fig.update_layout(xaxis_title=None, yaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)

# Cross Chain Comparison
else:
    st.subheader('Overview')
    c1, c2 = st.columns([1, 2])
    with c1:
        df = transactions_overview.query("Blockchain == @options")

        fig = px.bar(df, x='Blockchain', y='Transactions', color='Blockchain', title='Total Transactions', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.bar(df, x='Blockchain', y='TPS', color='Blockchain', title='Average TPS', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.bar(df, x='Blockchain', y='Blocks', color='Blockchain', title='Blocks', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        fig = px.bar(df, x='Blockchain', y='Users', color='Blockchain', title='Total Active Addresses', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        df = transactions_daily.query("Blockchain == @options")

        fig = px.line(df, x='Date', y='Transactions', color='Blockchain', title='Daily Total Transactions', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.line(df, x='Date', y='TPS', color='Blockchain', title='Daily Average TPS', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.line(df, x='Date', y='Blocks', color='Blockchain', title='Daily Blocks', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.line(df, x='Date', y='Users', color='Blockchain', title='Daily Active Addresses', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader('Activity Heatmap')
    c1, c2 = st.columns(2)
    with c1:
        df = transactions_heatmap.query("Blockchain == @options")

        fig = px.scatter(df, x='Transactions', y='Day', color='Blockchain', title='Daily Heatmap of Transactions', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Blocks', y='Day', color='Blockchain', title='Daily Heatmap of Blocks', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Users', y='Day', color='Blockchain', title='Daily Heatmap of Users', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.scatter(df, x='Transactions', y='Hour', color='Blockchain', title='Hourly Heatmap of Transactions', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Blocks', y='Hour', color='Blockchain', title='Hourly Heatmap of Blocks', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df, x='Users', y='Hour', color='Blockchain', title='Hourly Heatmap of Users', log_x=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)