# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Cross Chain Monitoring Tool', page_icon=':bar_chart:', layout='wide')
st.title('Cross Chain Monitoring Tool')

# Content
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

st.write("")
st.write("")
st.write("")
st.write("")

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

c1, c2 = st.columns(2)
with c1:
    st.info('Developer: [@AliTslm](https://twitter.com/AliTslm)', icon="💻")
with c2:
    st.info('Data: [Flipside Crypto](https://flipsidecrypto.xyz/)', icon="🧠")