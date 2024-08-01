import requests
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import streamlit as st

# Define the API URL
API_URL = 'https://jsonplaceholder.typicode.com/posts'

# Define the SQLAlchemy database model
Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    title = Column(String(255))
    body = Column(Text)

# Setup database connection
engine = create_engine('sqlite:///posts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []

def store_data(data):
    for item in data:
        existing_post = session.query(Post).filter_by(id=item['id']).first()
        if existing_post:
            # Update existing record
            existing_post.userId = item['userId']
            existing_post.title = item['title']
            existing_post.body = item['body']
        else:
            # Insert new record
            post = Post(id=item['id'], userId=item['userId'], title=item['title'], body=item['body'])
            session.add(post)
    session.commit()

def load_data():
    query = "SELECT * FROM posts"
    df = pd.read_sql(query, engine)
    return df

# Fetch and store data when the script runs
if __name__ == "__main__":
    data = fetch_data()
    store_data(data)
    print("Data has been fetched and stored.")

    # Streamlit Dashboard
    st.title('Project Dashboard')

    st.subheader('Total Number of Entries')
    df = load_data()
    st.write(len(df))

    st.subheader('Distribution by User ID')
    st.bar_chart(df['userId'].value_counts())

    st.subheader('Top 10 Entries')
    st.write(df[['id', 'title']].head(10))

    search_term = st.text_input('Search by Name or ID:')
    if search_term:
        results = df[df['title'].str.contains(search_term, case=False, na=False) | df['id'].astype(str).str.contains(search_term)]
        st.write(results)
