# Restaurant Hunter 🤖🍛
This project scrapes data for the top 10 restaurants from Zomato and allows users to query restaurant details using a chatbot powered by the Grok API. The information scraped includes restaurant names, locations, cuisine types, and more, which is stored in a CSV file. The Grok API is used to provide responses to user queries based on the information in the CSV.

## Features
**Web Scraping:** Scrapes Zomato for the top 10 restaurants.

**Data Storage:** Saves restaurant data in a CSV file.

**Chatbot:** Users can interact with a chatbot to get restaurant details.

**GroAPI Integration:** Uses Grok API to power the chatbot’s responses based on the scraped data.# Zomato_task

## Installation Guide
### Step 1: Clone the Repository
First, clone the repository to your local machine. Open your terminal and run:
```bash
git clone https://github.com/your-username/restaurant-hunter.git
cd restaurant-hunter
```
### Step 2: Install Dependencies
With the virtual environment activated, install the required dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Project
The scraper will scrape restaurant data from Zomato and save it in a restaurants.csv file:
```bash
python scraper.py

```

