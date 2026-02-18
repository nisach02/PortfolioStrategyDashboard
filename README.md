# Portfolio Strategy Dashboard

🚀 **Strategic Liquidity & Portfolio Analysis**

A professional-grade dashboard designed to provide actionable insights into DEX liquidity efficiency and portfolio health. This tool compares Uniswap V2 vs. V3 performance and analyzes live wallet holdings to recommend optimization strategies.

## ✨ Features

- **Live Data Integration**: Fetches real-time wallet balances via Dune's Echo/Sim API.
- **Strategic Simulation**: Models market efficiency trends between concentrated (V3) and standard (V2) liquidity.
- **Interactive Visualizations**: Dynamic charts powered by Plotly and Streamlit.
- **Executive Summaries**: Automated strategic recommendations for liquidity migration and fee optimization.

## 🛠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Visualization**: [Plotly](https://plotly.com/python/)
- **Data Processing**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **API**: [Dune API](https://dune.com/docs/api/)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Dune API Key](https://dune.com/settings/api)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd PortfolioStrategyDashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## 📂 Project Structure

```text
.
├── app.py              # Entry point (Streamlit UI)
├── src/
│   ├── api.py          # API interaction layer
│   └── processing.py   # Data models and strategy logic
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

## 📝 License

This project is licensed under the MIT License.
