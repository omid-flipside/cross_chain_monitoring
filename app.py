# -------------------------------------------------- Libraries --------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

# -------------------------------------------------- Data Sources --------------------------------------------------

# Transactions
transactions_overview = pd.read_csv('Data/transactions_overview.csv')
transactions_daily = pd.read_csv('Data/transactions_daily.csv')
transactions_heatmap = pd.read_csv('Data/transactions_heatmap.csv')

# Transfers
transfers_overview = pd.read_csv('Data/transfers_overview.csv')
transfers_daily = pd.read_csv('Data/transfers_daily.csv')

# Swaps
swaps_overview = pd.read_csv('Data/swaps_overview.csv')
swaps_daily = pd.read_csv('Data/swaps_daily.csv')

# NFTs
nfts_overview = pd.read_csv('Data/nfts_overview.csv')
nfts_daily = pd.read_csv('Data/nfts_daily.csv')

# st.cache(ttl=3600)
# def get_date(data):
#     if data == 'swaps':
#         return pd.read_csv('data/Swaps.csv')
        # return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/14dc8c9f-9d45-439d-ac4e-46505d1a8298/data/latest')
# raw_swaps = get_date('swaps')

# raw_swaps = pd.read_csv('Data/Swaps.csv')
# swaps_dexs_overview = raw_swaps.groupby(['Blockchain', 'DEX'], as_index=False).aggregate(
#     {'Date': 'nunique', 'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).round()
# swaps_dexs_overview['Swaps/Day'] = (swaps_dexs_overview['Swaps'] / swaps_dexs_overview['Date']).round()
# swaps_dexs_overview['Swappers/Day'] = (swaps_dexs_overview['Swappers'] / swaps_dexs_overview['Date']).round()
# swaps_dexs_overview['Volume/Day'] = (swaps_dexs_overview['Volume'] / swaps_dexs_overview['Date']).round()
# swaps_dexs_overview['Swaps/Swapper'] = (swaps_dexs_overview['Swaps'] / swaps_dexs_overview['Swappers']).round()
# swaps_dexs_overview['Volume/Swapper'] = (swaps_dexs_overview['Volume'] / swaps_dexs_overview['Swappers']).round()

# swaps_dexs_daily = raw_swaps.groupby(['Date', 'Blockchain', 'DEX'], as_index=False).aggregate(
#     {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'})

# swaps_assets_overview = raw_swaps.groupby(['Blockchain', 'Type'], as_index=False).aggregate(
#     {'Date': 'nunique', 'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'}).round()
# swaps_assets_overview['Swaps/Day'] = (swaps_assets_overview['Swaps'] / swaps_assets_overview['Date']).round()
# swaps_assets_overview['Swappers/Day'] = (swaps_assets_overview['Swappers'] / swaps_assets_overview['Date']).round()
# swaps_assets_overview['Volume/Day'] = (swaps_assets_overview['Volume'] / swaps_assets_overview['Date']).round()
# swaps_assets_overview['Swaps/Swapper'] = (swaps_assets_overview['Swaps'] / swaps_assets_overview['Swappers']).round()
# swaps_assets_overview['Volume/Swapper'] = (swaps_assets_overview['Volume'] / swaps_assets_overview['Swappers']).round()

# swaps_assets_daily = raw_swaps.groupby(['Date', 'Blockchain', 'Asset', 'Type'], as_index=False).aggregate(
#     {'Swaps': 'sum', 'Swappers': 'sum', 'Volume': 'sum', 'AmountAverage': 'mean', 'AmountMedian': 'mean'})

# -------------------------------------------------- Layout --------------------------------------------------

st.set_page_config(page_title='Cross Chain Monitoring Tool', page_icon=':bar_chart:', layout='wide')
st.title('Cross Chain Monitoring Tool')

tab_overview, tab_transactions, tab_transfers, tab_swaps, tab_nfts = st.tabs([
    '**Overview**', '**Transactions**', '**Transfers**', '**Swaps**', '**NFTs**'])

# -------------------------------------------------- Overview --------------------------------------------------

with tab_overview:

    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15 = st.columns(15)
    c1.image(Image.open('Images/ethereum-logo.png'))
    c2.image(Image.open('Images/bsc-logo.png'))
    c3.image(Image.open('Images/polygon-logo.png'))
    c4.image(Image.open('Images/solana-logo.png'))
    c5.image(Image.open('Images/avalanche-logo.png'))
    c6.image(Image.open('Images/cosmos-logo.png'))
    c7.image(Image.open('Images/algorand-logo.png'))
    c8.image(Image.open('Images/near-logo.png'))
    c9.image(Image.open('Images/flow-logo.png'))
    c10.image(Image.open('Images/thorchain-logo.png'))
    c11.image(Image.open('Images/osmosis-logo.png'))
    c12.image(Image.open('Images/gnosis-logo.png'))
    c13.image(Image.open('Images/optimism-logo.png'))
    c14.image(Image.open('Images/arbitrum-logo.png'))
    c15.image(Image.open('Images/axelar-logo.png'))

    st.write(
        """
        The crypto industry continues to progress regardless of the market condition and contributors of each
        blockchain keep developing different segments of the industry and the whole crypto ecosystem.
        This tool is designed to allow viewers to journey into the world of crypto ecosystems of some of the
        major blockchains, and compare their performance.

        This tool is designed and structured in multiple **Tabs**, which address a different segment of the crypto
        industry. Within each segment (Transactions, Transfers, Swaps, and NFTs) you are able to filter your desired
        blockchains to narrow/expand the comparison. By selecting a single blockchain, you are able to observe a
        deep dive into that particular network.
        """
    )

    st.subheader('Methodology')
    st.write(
        """
        The data for this cross-chain comparison were selected from the [Flipside Crypto](https://flipsidecrypto.xyz/)
        data platform and queried using the [Flipside ShroomDK](https://sdk.flipsidecrypto.xyz/shroomdk).
        The results of these queries were saved into multiple CSV files in a
        [GitHub Repository](https://github.com/alitslm/cross_chain_monitoring). The scripts are currently manually run
        to both cover the recent data, as well as backfilling the previous ones.

        While all the codes and queries are accessible through the GitHub repository mentioned above, the following
        dashboards created using Flipside Crypto were used as the core references in developing the current tool.

        - [Flipside World Cup: Gas Guzzlers](https://app.flipsidecrypto.com/dashboard/flipsides-world-cup-gas-guzzlers-iTcitG)
        - [Flipside World Cup: USDC Transfers](https://app.flipsidecrypto.com/dashboard/flipside-world-cup-usdc-transfers-l-dWsf)
        - [Flipside World Cup: NFT Sales](https://app.flipsidecrypto.com/dashboard/flipside-world-cup-nft-sales-lDvMLG)
        - [Flipside World Cup: Cross Chain DeFi Monitoring](https://app.flipsidecrypto.com/dashboard/flipside-world-cup-cross-chain-de-fi-monitoring-bOY5ox)
        """
    )

    st.subheader('Future Works')
    st.write(
        """
        This tool is a work in progress and other blockchains/metrics are constantly being added to further facilitate
        the comparison of different networks and segments with one another. Feel free to @ me on Twitter
        ([@AliTslm](https://twitter.com/AliTslm)) to share your feedback, suggestions, and even critics with me.
        """
    )

# -------------------------------------------------- Transactions --------------------------------------------------
with tab_transactions:
    st.write(
        """
        Generally, Gas refers to the unit that measures the amount of computational power required to execute specific operations on a particular blockchain.
        Each transaction requires computational resources to execute which is paid as a fee, to also enhance the security of the network by preventing bad actors from spamming transactions.
        In order to avoid infinite loops or other computational wastage in the code, each transaction must set a limit to its steps of execution.
        The fundamental unit for this fee is gas. In other words, gas is the fuel that allows a particular network to operate, the same way gasoline plays a critical role in the operation of a car.
        """
    )

    # Filter the blockchains
    options = st.multiselect(
        'Select your desired blockchains:',
        options=transactions_overview['Blockchain'].unique(),
        default=transactions_overview['Blockchain'].unique()
    )
    filtered_transactions_overview = transactions_overview.query("Blockchain == @options")
    filtered_transactions_daily = transactions_daily.query("Blockchain == @options")
    filtered_transactions_heatmap = transactions_heatmap.query("Blockchain == @options")

    # Selected Blockchain
    if len(options) == 0:
        st.warning('Please select at least one blockchain to see the metrics.')

    elif len(options) == 1:
        st.subheader('Overview')

        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            st.metric(label='Blocks', value=filtered_transactions_overview['Blocks'])
            st.metric(label='Transactions/Block', value=filtered_transactions_overview['Transactions/Block'].round(2))
        with c2:
            st.metric(label='Transactions', value=filtered_transactions_overview['Transactions'])
            st.metric(label='TPS', value=filtered_transactions_overview['TPS'].round(2))
        with c3:
            st.metric(label='Users', value=filtered_transactions_overview['Users'])
            st.metric(label='Users/Day', value=filtered_transactions_overview['Users/Day'].round())
        with c4:
            st.metric(label='Fees', value=filtered_transactions_overview['Fees'].round(), help='USD')
            st.metric(label='Fees/Block', value=filtered_transactions_overview['Fees/Block'].round(2), help='USD')
        with c5:
            st.metric(label='FeeAverage', value=filtered_transactions_overview['FeeAverage'].round(2), help='USD')
            st.metric(label='FeeMedian', value=filtered_transactions_overview['FeeMedian'].round(2), help='USD')

        st.subheader('Activity')

        c1, c2 = st.columns(2)
        with c1:
            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Transactions'], name='Transactions'), secondary_y=False)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Blocks'], name='Blocks'), secondary_y=True)
            fig.update_layout(title_text='Daily Total Transactions and Blocks')
            fig.update_yaxes(title_text='Transactions', secondary_y=False)
            fig.update_yaxes(title_text='Blocks', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['TPS'], name='TPS'), secondary_y=False)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Transactions/Block'], name='Transactions/Block'), secondary_y=True)
            fig.update_layout(title_text='Daily TPS and Transactions/Block')
            fig.update_yaxes(title_text='TPS', secondary_y=False)
            fig.update_yaxes(title_text='Transactions/Block', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.area(filtered_transactions_daily, x='Date', y='Users', title='Daily Users')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Fees'], name='Total'), secondary_y=False)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['FeeAverage'], name='Average'), secondary_y=True)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['FeeMedian'], name='Median'), secondary_y=True)
            fig.update_layout(title_text='Daily Total, Average, and Median Fees')
            fig.update_yaxes(title_text='Total', secondary_y=False)
            fig.update_yaxes(title_text='Average and Median', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)

        st.subheader('Heatmap')

        c1, c2 = st.columns(2)
        with c1:
            fig = px.scatter(filtered_transactions_heatmap, x='Hour', y='Day', size='Transactions', color='Transactions', title='Daily Heatmap of Transactions')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(filtered_transactions_heatmap, x='Hour', y='Day', size='Blocks', color='Blocks', title='Daily Heatmap of Blocks')
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.scatter(filtered_transactions_heatmap, x='Hour', y='Day', size='Users', color='Users', title='Daily Heatmap of Users')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.scatter(filtered_transactions_heatmap, x='Hour', y='Day', size='Fees', color='Fees', title='Daily Heatmap of Fees')
            st.plotly_chart(fig, use_container_width=True)

    # Cross Chain Comparison
    else:
        subtab_overview, subtab_fees, subtab_heatmap = st.tabs(['Overview', 'Fees', 'Heatmap'])

        with subtab_overview:
            st.subheader("Transactions, Blocks, and Users")
            c1, c2, c3 = st.columns([1, 1, 2])
            with c1:
                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='Transactions', color='Blockchain', title='Total Transactions', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='Blocks', color='Blockchain', title='Total Blocks', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='Fees', color='Blockchain', title='Total Transaction Fees', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                fig = px.pie(filtered_transactions_overview, values='Transactions', names='Blockchain', title='Share of Total Transaction')
                fig.update_layout(showlegend=False)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True)

                fig = px.pie(filtered_transactions_overview, values='Blocks', names='Blockchain', title='Share of Total Blocks')
                fig.update_layout(showlegend=False)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True)

                fig = px.pie(filtered_transactions_overview, values='Fees', names='Blockchain', title='Share of Total Transaction Fees')
                fig.update_layout(showlegend=False)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True)
            with c3:
                fig = px.line(filtered_transactions_daily, x='Date', y='Transactions', color='Blockchain', title='Daily Transactions', log_y=True)
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.line(filtered_transactions_daily, x='Date', y='Blocks', color='Blockchain', title='Daily Blocks', log_y=True)
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.line(filtered_transactions_daily, x='Date', y='Fees', color='Blockchain', title='Daily Transaction Fees', log_y=True)
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

            c1, c2, c3 = st.columns(3)
            with c1:
                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='TPS', color='Blockchain', title='Average TPS', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='Transactions/Block', color='Blockchain', title='Average Transactions/Block', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)
            with c3:
                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='Users/Day', color='Blockchain', title='Average Users/Day', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

        with subtab_fees:
            st.subheader("Total Transaction Fees")
            c1, c2, c3 = st.columns([1, 1, 2])
            with c1:
                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='Fees', color='Blockchain', title='Total Transaction Fees', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                fig = px.pie(filtered_transactions_overview, values='Fees', names='Blockchain', title='Share of Total Transaction Fees')
                fig.update_layout(showlegend=False)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True)
            with c3:
                fig = px.line(filtered_transactions_daily, x='Date', y='Fees', color='Blockchain', title='Daily Transaction Fees', log_y=True)
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

            st.subheader("Fee Amounts")
            c1, c2 = st.columns([1, 2])
            with c1:
                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='FeeAverage', color='Blockchain', title='Average Transaction Fees', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='FeeMedian', color='Blockchain', title='Median Transaction Fees', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)
                
                fig = px.bar(filtered_transactions_overview, x='Blockchain', y='Fees/Block', color='Blockchain', title='Median Transaction Fees/Block', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                fig = px.line(filtered_transactions_daily, x='Date', y='FeeAverage', color='Blockchain', title='Daily Average Fee Amount', log_y=True)
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.line(filtered_transactions_daily, x='Date', y='FeeMedian', color='Blockchain', title='Daily Median Fee Amount', log_y=True)
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.line(filtered_transactions_daily, x='Date', y='Fees/Block', color='Blockchain', title='Daily Average Fees/Block', log_y=True)
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

        with subtab_heatmap:
            c1, c2 = st.columns(2)
            with c1:
                fig = px.scatter(filtered_transactions_heatmap, x='Transactions', y='Day', color='Blockchain', title='Daily Heatmap of Transactions', log_x=True)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.scatter(filtered_transactions_heatmap, x='Blocks', y='Day', color='Blockchain', title='Daily Heatmap of Blocks', log_x=True)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.scatter(filtered_transactions_heatmap, x='Users', y='Day', color='Blockchain', title='Daily Heatmap of Users', log_x=True)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.scatter(filtered_transactions_heatmap, x='Fees', y='Day', color='Blockchain', title='Daily Heatmap of Fees', log_x=True)
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                fig = px.scatter(filtered_transactions_heatmap, x='Transactions', y='Hour', color='Blockchain', title='Hourly Heatmap of Transactions', log_x=True)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.scatter(filtered_transactions_heatmap, x='Blocks', y='Hour', color='Blockchain', title='Hourly Heatmap of Blocks', log_x=True)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.scatter(filtered_transactions_heatmap, x='Users', y='Hour', color='Blockchain', title='Hourly Heatmap of Users', log_x=True)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.scatter(filtered_transactions_heatmap, x='Fees', y='Hour', color='Blockchain', title='Hourly Heatmap of Fees', log_x=True)
                st.plotly_chart(fig, use_container_width=True)
   
# -------------------------------------------------- Transfers --------------------------------------------------
with tab_transfers:
    st.write("""
        Developed by Circle, USD Coin (USDC) is a faster, safer, and more efficient way to send, spend, and exchange money around the world. USDC supports apps that provide anytime access to payments and financial services.
        USDC, also known as a stablecoin, is a digital dollar that is available 24/7 and travels at the speed of the internet.
        USDC lives natively on the internet and runs on many of the world's most advanced blockchains.
        Billions of USDC change hands every day, and every digital dollar of USDC can always be exchanged 1:1 for cash.
        USDC is beyond border and bank business hours.
        As a worldwide digital dollar, USDC is available whenever and wherever you need it.
        It is easy to send USDC anywhere in the world, pay for goods and services, or save for the future.
        Anyone with an internet connection can send, receive and store USDC.
        Merchants can avoid associated credit card payment fees, benefit from immediate cash flow, and pass the savings on to their customers.
        USDC unlocks opportunities in the virtual capital markets for trading, lending, borrowing, and financing.
        Known as a fully reserved stablecoin, all USDC digital dollars on the web are always redeemable as they are backed by 100 percent cash and short-term U.S. treasuries, so it is always redeemable 1:1 for U.S. dollars.
        The USDC Reserve is owned and managed by major US financial institutions such as BlackRock and BNY Mellon.
        Each month, Grant Thornton LLP, one of the largest US accounting, tax, and advisory firms, provides independent verification of the size of USDC reserves.
        Circle is regulated as a licensed money transfer provider under US federal law and its financial statements are audited annually and are subject to review by the SEC.
        """)

    # Filter the blockchains
    options = st.multiselect(
        'Select your desired blockchains:',
        options=transfers_overview['Blockchain'].unique(),
        default=transfers_overview['Blockchain'].unique()
    )
    filtered_transfers_overview = transfers_overview.query("Blockchain == @options")
    filtered_transfers_daily = transfers_daily.query("Blockchain == @options")

    # Selected Blockchain
    if len(options) == 1:
        st.subheader(f"Overview")

        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            st.metric(label='Blocks', value=filtered_transactions_overview['Blocks'])
            st.metric(label='Transactions/Block', value=filtered_transactions_overview['Transactions/Block'].round(2))
        with c2:
            st.metric(label='Transactions', value=filtered_transactions_overview['Transactions'])
            st.metric(label='TPS', value=filtered_transactions_overview['TPS'].round(2))
        with c3:
            st.metric(label='Users', value=filtered_transactions_overview['Users'])
            st.metric(label='Users/Day', value=filtered_transactions_overview['Users/Day'].round())
        with c4:
            st.metric(label='Fees', value=filtered_transactions_overview['Fees'].round(), help='USD')
            st.metric(label='Fees/Block', value=filtered_transactions_overview['Fees/Block'].round(2), help='USD')
        with c5:
            st.metric(label='FeeAverage', value=filtered_transactions_overview['FeeAverage'].round(2), help='USD')
            st.metric(label='FeeMedian', value=filtered_transactions_overview['FeeMedian'].round(2), help='USD')

        st.subheader(f"Activity")

        c1, c2 = st.columns(2)
        with c1:
            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Transactions'], name='Transactions'), secondary_y=False)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Blocks'], name='Blocks'), secondary_y=True)
            fig.update_layout(title_text='Daily Total Transactions and Blocks')
            fig.update_yaxes(title_text='Transactions', secondary_y=False)
            fig.update_yaxes(title_text='Blocks', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)

            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['TPS'], name='TPS'), secondary_y=False)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Transactions/Block'], name='Transactions/Block'), secondary_y=True)
            fig.update_layout(title_text='Daily TPS and Transactions/Block')
            fig.update_yaxes(title_text='TPS', secondary_y=False)
            fig.update_yaxes(title_text='Transactions/Block', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.area(filtered_transactions_daily, x='Date', y='Users', title='Daily Users')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
            fig.add_trace(go.Bar(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['Fees'], name='Total'), secondary_y=False)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['FeeAverage'], name='Average'), secondary_y=True)
            fig.add_trace(go.Line(x=filtered_transactions_daily['Date'], y=filtered_transactions_daily['FeeMedian'], name='Median'), secondary_y=True)
            fig.update_layout(title_text='Daily Total, Average, and Median Fees')
            fig.update_yaxes(title_text='Total', secondary_y=False)
            fig.update_yaxes(title_text='Average and Median', secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)

    # Cross Chain Comparison
    else:
        st.subheader("Overview")

        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='Volume', color='Blockchain', title='Total USDC Transferred Volume', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(filtered_transfers_overview, values='Volume', names='Blockchain', title='Share of Total USDC Transferred Volume')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='Volume/Day', color='Blockchain', title='Average USDC Transferred Volume/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='Transfers', color='Blockchain', title='Total USDC Transfers', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(filtered_transfers_overview, values='Transfers', names='Blockchain', title='Share of Total USDC Transfers')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='Transfers/Day', color='Blockchain', title='Average USDC Transfers/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c3:
            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='Users', color='Blockchain', title='Total USDC Transferring Users', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(filtered_transfers_overview, values='Users', names='Blockchain', title='Share of Total USDC Transferring Users')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='Users/Day', color='Blockchain', title='Average USDC Transferring Users/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Transferred Amount")

        c1, c2 = st.columns([1, 2])
        with c1:
            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='AmountAverage', color='Blockchain', title='Average Transferred Amount', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_transfers_overview, x='Blockchain', y='AmountMedian', color='Blockchain', title='Median Transferred Amount', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            fig = px.line(filtered_transfers_daily, x='Date', y='AmountAverage', color='Blockchain', title='Daily Average Transferred Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(filtered_transfers_daily, x='Date', y='AmountMedian', color='Blockchain', title='Daily Median Transferred Amount')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Transfers Over Time")

        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(filtered_transfers_daily, x='Date', y='Volume', color='Blockchain', title='Daily Transferred Volume')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(filtered_transfers_daily, x='Date', y='Transfers', color='Blockchain', title='Daily Transfers')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(filtered_transfers_daily, x='Date', y='Users', color='Blockchain', title='Daily Transferring Users')
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=filtered_transfers_daily.query("Blockchain == @i")['Date'],
                    y=filtered_transfers_daily.query("Blockchain == @i")['Volume'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Transferred Volume')
            st.plotly_chart(fig, use_container_width=True)
            
            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=filtered_transfers_daily.query("Blockchain == @i")['Date'],
                    y=filtered_transfers_daily.query("Blockchain == @i")['Transfers'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Transfers')
            st.plotly_chart(fig, use_container_width=True)

            fig = go.Figure()
            for i in options:
                fig.add_trace(go.Scatter(
                    name=i,
                    x=filtered_transfers_daily.query("Blockchain == @i")['Date'],
                    y=filtered_transfers_daily.query("Blockchain == @i")['Users'],
                    mode='lines',
                    stackgroup='one',
                    groupnorm='percent'
                ))
            fig.update_layout(title='Daily Share of Transferring Users')
            st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------- Swaps --------------------------------------------------
with tab_swaps:
    st.write(
        """
        Traditionally, trading cryptocurrencies requires the use of a centralized exchange (CEX) which is operated by a private company.
        This implies that there is a third party overseeing every transaction who also gathers and maintains information on all of their clients.
        Another crucial factor is that CEX transactions are custodial, meaning the platform owns the assets that are being traded.
        Decentralized exchanges (DEX) provide non-custodial transactions and, ideally, total anonymity.
        This indicates that the assets being exchanged never passes through the hands of an intermediary.
        """
    )

    # Filter the blockchains
    options = st.multiselect(
        'Select your desired blockchains:',
        options=swaps_overview['Blockchain'].unique(),
        default=swaps_overview['Blockchain'].unique(),
        key='Blockchain'
    )

    filtered_swaps_overview = swaps_overview.query("Blockchain == @options")
    filtered_swaps_daily = swaps_daily.query("Blockchain == @options")
    # filtered_swaps_dexs_overview = swaps_dexs_overview.query("Blockchain == @options")
    # filtered_swaps_dexs_daily = swaps_dexs_daily.query("Blockchain == @options")
    # filtered_swaps_assets_overview = swaps_assets_overview.query("Blockchain == @options")
    # filtered_swaps_assets_daily = swaps_assets_daily.query("Blockchain == @options")

    # Swaps Data Layout
    subtab_overview, subtab_heatmap, subtab_dexs, subtap_assets = st.tabs(['Overview', 'Heatmap', 'DEXs', 'Assets'])

    with subtab_overview:

        # Selected Blockchain
        if len(options) == 1:

            st.subheader(f"{options[0]}'s Overview")

            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                st.metric(label='Volume', value=filtered_swaps_overview['Volume'], help='USD')
                st.metric(label='Volume/Day', value=filtered_swaps_overview['Volume/Day'], help='USD')
            with c2:
                st.metric(label='Swaps', value=filtered_swaps_overview['Swaps'], help='Number')
                st.metric(label='Swaps/Day', value=filtered_swaps_overview['Swaps/Day'], help='Number')
            with c3:
                st.metric(label='Swappers', value=filtered_swaps_overview['Swappers'], help='Number')
                st.metric(label='Swappers/Day', value=filtered_swaps_overview['Swappers/Day'], help='Number')
            with c4:
                st.metric(label='Average Swap Amount', value=filtered_swaps_overview['AmountAverage'], help='USD')
                st.metric(label='Median Swap Amount', value=filtered_swaps_overview['AmountMedian'], help='USD')
            with c5:
                st.metric(label='Volume/Swapper', value=filtered_swaps_overview['Volume/Swapper'], help='USD')
                st.metric(label='Swaps/Swapper', value=filtered_swaps_overview['Swaps/Swapper'], help='Number')

            st.subheader("Swaps Over Time")

            c1, c2, c3 = st.columns(3)
            with c1:
                fig = px.line(filtered_swaps_daily, x='Date', y='Volume', title='Daily Volume of Swaps')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                fig = px.line(filtered_swaps_daily, x='Date', y=['Swaps', 'Swappers'], title='Daily Number of Swaps and Swappers')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)
            with c3:
                fig = px.line(filtered_swaps_daily, x='Date', y=['AmountAverage', 'AmountMedian'], title='Daily Average and Median Swap Amount')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)
            
        # Cross Chain Comparison
        else:

            st.subheader("Overview of Swaps")

            c1, c2, c3 = st.columns(3)

            with c1:
                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Volume', color='Blockchain', title='Total Swaps Volume', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

                fig = px.pie(filtered_swaps_overview, values='Volume', names='Blockchain', title='Share of Total Swaps Volume')
                fig.update_layout(showlegend=False)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True)

                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Volume/Day', color='Blockchain', title='Average Swaps Volume/Day', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

            with c2:
                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Swaps', color='Blockchain', title='Total Swaps', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

                fig = px.pie(filtered_swaps_overview, values='Swaps', names='Blockchain', title='Share of Total Swaps')
                fig.update_layout(showlegend=False)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True)

                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Swaps/Day', color='Blockchain', title='Average Swaps/Day', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

            with c3:
                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Swappers', color='Blockchain', title='Total Swappers', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

                fig = px.pie(filtered_swaps_overview, values='Swappers', names='Blockchain', title='Share of Total Swappers')
                fig.update_layout(showlegend=False)
                fig.update_traces(textinfo='percent+label', textposition='inside')
                st.plotly_chart(fig, use_container_width=True)

                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Swappers/Day', color='Blockchain', title='Average Swappers/Day', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

            c1, c2 = st.columns(2)
            with c1:
                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Volume/Swapper', color='Blockchain', title='Average Volume/Swapper', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)
                
            with c2:
                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='Swaps/Swapper', color='Blockchain', title='Average Swaps/Swapper', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

            st.subheader("Swap Amount")

            c1, c2 = st.columns([1, 2])
            with c1:
                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='AmountAverage', color='Blockchain', title='Average Swap Amount', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

                fig = px.bar(filtered_swaps_overview, x='Blockchain', y='AmountMedian', color='Blockchain', title='Median Swap Amount', log_y=True)
                fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
                st.plotly_chart(fig, use_container_width=True)

            with c2:
                fig = px.line(filtered_swaps_daily, x='Date', y='AmountAverage', color='Blockchain', title='Daily Average Swap Amount')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.line(filtered_swaps_daily, x='Date', y='AmountMedian', color='Blockchain', title='Daily Median Swap Amount')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)
           
            st.subheader("Swaps Over Time")

            c1, c2 = st.columns(2)
            with c1:
                fig = px.line(filtered_swaps_daily, x='Date', y='Volume', color='Blockchain', title='Daily Swaps Volume')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.line(filtered_swaps_daily, x='Date', y='Swaps', color='Blockchain', title='Daily Swaps')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

                fig = px.line(filtered_swaps_daily, x='Date', y='Swappers', color='Blockchain', title='Daily Swappers')
                fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None)
                st.plotly_chart(fig, use_container_width=True)

            with c2:
                fig = go.Figure()
                for i in options:
                    fig.add_trace(go.Scatter(
                        name=i,
                        x=filtered_swaps_daily.query("Blockchain == @i")['Date'],
                        y=filtered_swaps_daily.query("Blockchain == @i")['Volume'],
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
                        x=filtered_swaps_daily.query("Blockchain == @i")['Date'],
                        y=filtered_swaps_daily.query("Blockchain == @i")['Swaps'],
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
                        x=filtered_swaps_daily.query("Blockchain == @i")['Date'],
                        y=filtered_swaps_daily.query("Blockchain == @i")['Swappers'],
                        mode='lines',
                        stackgroup='one',
                        groupnorm='percent'
                    ))
                fig.update_layout(title='Daily Share of Swappers')
                st.plotly_chart(fig, use_container_width=True)
    
    with subtab_heatmap:

            st.subheader("Heatmap of Swaps")

    # with subtab_dexs:
        
    #     st.subheader("Overview of DEXs")

    #     c1, c2, c3 = st.columns(3)

    #     with c1:
    #         fig = px.histogram(filtered_swaps_dexs_overview.sort_values('Volume', ascending=False).head(20), x='DEX', y='Volume', color='Blockchain', title='Swaps Volume of Top DEXs', log_y=True)
    #         fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         fig.update_xaxes(categoryorder='total ascending')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.pie(filtered_swaps_dexs_overview, values='Volume', names='DEX', title='Share of Swaps Volume of Top DEXs')
    #         fig.update_layout(showlegend=False)
    #         fig.update_traces(textinfo='percent+label', textposition='inside')
    #         st.plotly_chart(fig, use_container_width=True)

    #     with c2:
    #         fig = px.histogram(filtered_swaps_dexs_overview.sort_values('Swaps', ascending=False).head(20), x='DEX', y='Swaps', color='Blockchain', title='Swaps of Top DEXs', log_y=True)
    #         fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         fig.update_xaxes(categoryorder='total ascending')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.pie(filtered_swaps_dexs_overview, values='Swaps', names='DEX', title='Share of Swaps of Top DEXs')
    #         fig.update_layout(showlegend=False)
    #         fig.update_traces(textinfo='percent+label', textposition='inside')
    #         st.plotly_chart(fig, use_container_width=True)

    #     with c3:
    #         fig = px.histogram(filtered_swaps_dexs_overview.sort_values('Swappers', ascending=False).head(20), x='DEX', y='Swappers', color='Blockchain', title='Swappers of Top DEXs', log_y=True)
    #         fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         fig.update_xaxes(categoryorder='total ascending')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.pie(filtered_swaps_dexs_overview, values='Swappers', names='DEX', title='Share of Swappers of Top DEXs')
    #         fig.update_layout(showlegend=False)
    #         fig.update_traces(textinfo='percent+label', textposition='inside')
    #         st.plotly_chart(fig, use_container_width=True)

    #     st.subheader("Swaps of DEXs Over Time")

    # with subtap_assets:
        
    #     st.subheader("Overview of Asset Types")

    #     c1, c2, c3 = st.columns(3)

    #     with c1:
    #         fig = px.pie(filtered_swaps_assets_overview, values='Volume', names='Type', title='Share of Total Swaps Volume of Each Asset Type')
    #         fig.update_layout(showlegend=False)
    #         fig.update_traces(textinfo='percent+label', textposition='inside')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.histogram(filtered_swaps_assets_overview, x='Blockchain', y='Volume', color='Type', title='Swaps Volume of Each Asset Type', log_y=True, barmode='group')
    #         fig.update_layout(xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         fig.update_xaxes(categoryorder='total ascending')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.histogram(filtered_swaps_assets_overview, x='Blockchain', y='Volume', color='Type', title='Share of Swaps Volume of Each Asset Type', log_y=True, barnorm='percent')
    #         fig.update_layout(xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         st.plotly_chart(fig, use_container_width=True)

    #     with c2:
    #         fig = px.pie(filtered_swaps_assets_overview, values='Swaps', names='Type', title='Share of Total Swaps of Each Asset Type')
    #         fig.update_layout(showlegend=False)
    #         fig.update_traces(textinfo='percent+label', textposition='inside')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.histogram(filtered_swaps_assets_overview, x='Blockchain', y='Swaps', color='Type', title='Swaps of Each Asset Type', log_y=True, barmode='group')
    #         fig.update_layout(xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         fig.update_xaxes(categoryorder='total ascending')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.histogram(filtered_swaps_assets_overview, x='Blockchain', y='Swaps', color='Type', title='Share of Swaps of Each Asset Type', log_y=True, barnorm='percent')
    #         fig.update_layout(xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         st.plotly_chart(fig, use_container_width=True)

    #     with c3:
    #         fig = px.pie(filtered_swaps_assets_overview, values='Swappers', names='Type', title='Share of Total Swappers of Each Asset Type')
    #         fig.update_layout(showlegend=False)
    #         fig.update_traces(textinfo='percent+label', textposition='inside')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.histogram(filtered_swaps_assets_overview, x='Blockchain', y='Swappers', color='Type', title='Swappers of Each Asset Type', log_y=True, barmode='group')
    #         fig.update_layout(xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         fig.update_xaxes(categoryorder='total ascending')
    #         st.plotly_chart(fig, use_container_width=True)

    #         fig = px.histogram(filtered_swaps_assets_overview, x='Blockchain', y='Swappers', color='Type', title='Share of Swappers of Each Asset Type', log_y=True, barnorm='percent')
    #         fig.update_layout(xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
    #         st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------- NFTs --------------------------------------------------
with tab_nfts:
    st.write(
        """
        Traditionally, trading cryptocurrencies requires the use of a centralized exchange (CEX) which is operated by a private company.
        This implies that there is a third party overseeing every transaction who also gathers and maintains information on all of their clients.
        Another crucial factor is that CEX transactions are custodial, meaning the platform owns the assets that are being traded.
        Decentralized exchanges (DEX) provide non-custodial transactions and, ideally, total anonymity.
        This indicates that the assets being exchanged never passes through the hands of an intermediary.
        """
    )

    # Filter the blockchains
    options = st.multiselect(
        'Select your desired blockchains:',
        options=nfts_overview['Blockchain'].unique(),
        default=nfts_overview['Blockchain'].unique()
    )
    filtered_nfts_overview = nfts_overview.query("Blockchain == @options")
    filtered_nfts_daily = nfts_daily.query("Blockchain == @options")

    # Selected Blockchain
    if len(options) == 1:
        st.subheader(f"Overview")

        c1, c2, c3, c4, c5, c6 = st.columns(6)
        with c1:
            st.metric(label='Volume', value=filtered_nfts_overview['Volume'].round(), help='USD')
            st.metric(label='Volume/Day', value=filtered_nfts_overview['Volume/Day'].round(), help='USD')
            st.metric(label='Volume/Buyer', value=filtered_nfts_overview['Volume/Buyer'].round(), help='USD')
        with c2:
            st.metric(label='Sales', value=filtered_nfts_overview['Sales'])
            st.metric(label='Sales/Day', value=filtered_nfts_overview['Sales/Day'].round())
            st.metric(label='Sales/Buyer', value=filtered_nfts_overview['Sales/Buyer'].round())
        with c3:
            st.metric(label='Buyers', value=filtered_nfts_overview['Buyers'])
            st.metric(label='Buyers/Day', value=filtered_nfts_overview['Buyers/Day'].round())
            st.metric(label='Volume/Collection', value=filtered_nfts_overview['Volume/Collection'].round(), help='USD')
        with c4:
            st.metric(label='NFTs', value=filtered_nfts_overview['NFTs'])
            st.metric(label='NFTs/Day', value=filtered_nfts_overview['NFTs/Day'].round())
            st.metric(label='NFTs/Buyer', value=filtered_nfts_overview['NFTs/Buyer'].round(2))
        with c5:
            st.metric(label='Collections', value=filtered_nfts_overview['Collections'])
            st.metric(label='Collections/Day', value=filtered_nfts_overview['Collections/Day'].round())
            st.metric(label='Collections/Buyer', value=filtered_nfts_overview['Collections/Buyer'].round(2))
        with c6:
            st.metric(label='Marketplaces', value=filtered_nfts_overview['Marketplaces'])
            st.metric(label='NFTs/Sale', value=filtered_nfts_overview['NFTs/Sale'].round(2))
            st.metric(label='NFTs/Collection', value=filtered_nfts_overview['NFTs/Collection'].round())

    # Cross Chain Comparison
    else:
        st.subheader("Overview")

        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Volume', color='Blockchain', title='Total Sales Volume', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Sales', color='Blockchain', title='Total Sales', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Buyers', color='Blockchain', title='Total Buyers', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='NFTs', color='Blockchain', title='Total NFTs', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Collections', color='Blockchain', title='Total Collections', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            fig = px.pie(filtered_nfts_overview, values='Volume', names='Blockchain', title='Share of Total Sales Volume')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(filtered_nfts_overview, values='Sales', names='Blockchain', title='Share of Total Sales')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(filtered_nfts_overview, values='Buyers', names='Blockchain', title='Share of Total Buyers')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(filtered_nfts_overview, values='NFTs', names='Blockchain', title='Share of Total NFTs')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

            fig = px.pie(filtered_nfts_overview, values='Collections', names='Blockchain', title='Share of Total Collections')
            fig.update_layout(showlegend=False)
            fig.update_traces(textinfo='percent+label', textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

        with c3:
            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Volume/Day', color='Blockchain', title='Average Volume/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Sales/Day', color='Blockchain', title='Average Sales/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Buyers/Day', color='Blockchain', title='Average Buyers/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='NFTs/Day', color='Blockchain', title='Average NFTs/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)

            fig = px.bar(filtered_nfts_overview, x='Blockchain', y='Collections/Day', color='Blockchain', title='Average Collections/Day', log_y=True)
            fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None, xaxis={'categoryorder':'category ascending'})
            st.plotly_chart(fig, use_container_width=True)