# CarbonMarketsHQ Assignment

# Assignment 2 - Custom Carbon Credit Pricing Model

This project aims to create a custom pricing model for carbon credits based on various factors. The model generates a synthetic dataset of carbon credits, implements a custom pricing algorithm, and demonstrates the model using visualizations and user input functions in a Jupyter Notebook.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Factors Influencing Carbon Credit Prices](#factors-influencing-carbon-credit-prices)
- [Pricing Model](#pricing-model)
- [Visualizations](#visualizations)
- [User Input Function](#user-input-function)
- [Limitations and Improvements](#limitations-and-improvements)

## Introduction

Carbon credits are tradable certificates representing the reduction of one metric ton of CO2 emissions. The price of carbon credits can vary based on several factors, such as project type, location, vintage, and co-benefits. This project explores these factors and creates a custom pricing model.

## Installation

1. **Install Python and Jupyter Notebook:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).
   - Install Jupyter Notebook using pip:
     ```bash
     pip install notebook
     ```

2. **Install Required Libraries:**
   - Install `pandas`, `numpy`, `matplotlib`, and `seaborn`:
     ```bash
     pip install pandas numpy matplotlib seaborn
     ```

## Usage

1. **Start Jupyter Notebook:**
   - Launch Jupyter Notebook from the terminal:
     ```bash
     jupyter notebook
     ```
   - Open the provided notebook file `Carbon_Credit_Pricing_Model.ipynb`.

2. **Run the Notebook Cells:**
   - Follow the step-by-step instructions in the notebook to generate the synthetic dataset, implement the pricing model, create visualizations, and use the user input function.

## Factors Influencing Carbon Credit Prices

The following factors influence the pricing of carbon credits:
- **Project Type:** Different types of projects (e.g., reforestation, renewable energy) may have different impacts and costs.
- **Location:** The geographical location can affect the price due to regional regulations, demand, and verification costs.
- **Vintage:** The year the carbon credits were issued may influence their value.
- **Co-benefits:** Additional benefits (e.g., biodiversity, social benefits) can enhance the value of the credits.

## Pricing Model

The custom pricing model uses a weighted scoring system based on the factors identified. The weights are assigned as follows:

- **Project Type Weights:**
  - Reforestation: 1.2
  - Renewable Energy: 1.5
  - Methane Capture: 1.1
  - Energy Efficiency: 1.0

- **Location Weights:**
  - Africa: 0.8
  - Asia: 1.0
  - Europe: 1.2
  - North America: 1.3
  - South America: 1.1

- **Co-benefit Weights:**
  - High: 1.3
  - Medium: 1.1
  - Low: 1.05
  - None: 1.0

## Visualizations

The notebook includes visualizations to demonstrate how different factors impact the price of carbon credits. Examples include box plots showing the price distribution by project type and location.

## User Input Function

The notebook includes a function that allows users to input credit attributes and get a price estimate based on the custom pricing model. Example usage:
```python
estimated_price = estimate_price('Reforestation', 'Africa', 2023, 'High', 15)
print(f"Estimated Price: ${estimated_price:.2f}")
```

## Limitations and Improvements

### Limitations

- The weights assigned to different factors are arbitrary and may not reflect real-world conditions.
- The synthetic dataset may not capture the complexities of actual carbon credit markets.
- Additional factors like market demand, regulatory changes, and economic conditions are not considered.

### Improvements

- Incorporate actual market data to determine more accurate weights.
- Use machine learning techniques to model the pricing based on historical data.
- Include additional factors like project duration, verification standards, and regional policies.

## Conclusion

This project provides a basic framework for understanding and modeling the pricing of carbon credits. With further data and refinement, the model can be enhanced to provide more accurate and reliable price estimates.

# Assignment 3 - API + Database Integration and Dashboard

## Overview

This project demonstrates how to fetch data from the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API, store it in an SQLite database using SQLAlchemy, and create a simple interactive dashboard using Streamlit. The dashboard provides insights into the fetched data, including total entries, distribution by user ID, top 10 entries, and search functionality.

## Features

- **Total Number of Entries:** Displays the count of records in the database.
- **Distribution by User ID:** Shows a bar chart of posts distributed by user ID.
- **Top 10 Entries:** Lists the top 10 posts based on their ID.
- **Search Functionality:** Allows searching for posts by title or ID.

## Setup

### Prerequisites

- Python 3.7 or higher

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Create and Activate a Virtual Environment

```bash
python -m venv venv
```

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Run the Script

To fetch data, store it in the SQLite database, and start the Streamlit server, run:

```bash
python app.py
```

The Streamlit dashboard will open in your default web browser at `http://localhost:8501`. If it doesn’t open automatically, navigate to this URL manually.

## Project Structure

- `app.py`: Main script to fetch data, store it in the database, and run the Streamlit server.
- `posts.db`: SQLite database where the data is stored.
- `requirements.txt`: Lists the dependencies required for the project.

## Troubleshooting

- **IntegrityError:** If you encounter an `IntegrityError` related to unique constraints, ensure your database does not have duplicate entries. The script handles duplicates by updating existing records rather than inserting new ones.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, please reach out to [Your Name](mailto:your.email@example.com).
```

### How to Use This `README.md` on GitHub

1. **Replace placeholders:**
   - Replace `<repository-url>` with the actual URL of your GitHub repository.
   - Replace `<repository-directory>` with the name of your repository’s directory.
   - Update `[Your Name](mailto:your.email@example.com)` with your contact information.

2. **Add to Your Repository:**
   - Save this content as `README.md`.
   - Add and commit this file to your repository:
     ```bash
     git add README.md
     git commit -m "Add README file"
     git push
     ```

This `README.md` file provides a comprehensive overview, setup instructions, and relevant details for users who want to understand and run your project.
