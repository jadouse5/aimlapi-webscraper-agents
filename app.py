import streamlit as st
from openai import OpenAI
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file if available
load_dotenv()

# Function to set AI/ML API key dynamically in the session state
def set_aiml_api_key():
    api_key_input = st.text_input("Enter your AI/ML API Key", type="password")
    if api_key_input:
        os.environ['AIMLAPI_API_KEY'] = api_key_input
        st.success("AI/ML API Key set successfully!")
    else:
        st.warning("Please enter your AI/ML API Key to continue.")

# Initialize the OpenAI client
def initialize_openai_client():
    api_key = os.environ.get("AIMLAPI_API_KEY")
    base_url = os.environ.get("AIMLAPI_BASE_URL", "https://api.aimlapi.com/v1")
    return OpenAI(api_key=api_key, base_url=base_url)

# Define the scraping function
def scrape_website(url):
    """Scrapes the content of the website."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()  # Return the text content from the HTML
    except requests.exceptions.RequestException as e:
        return f"Error during scraping: {str(e)}"

# Define the analysis function
def analyze_content(content):
    """Analyzes the scraped content for key points."""
    summary = f"Summary of content: {content[:200]}..."  # A simple placeholder summarization
    return summary

# Define the writing function
def write_summary(analysis):
    """Writes a summary based on the analysis."""
    summary = f"Here's a detailed report based on the research: {analysis}"
    return summary

# Orchestrate the workflow
def orchestrate_workflow(client, url):
    # Step 1: Scrape the website
    scraped_content = scrape_website(url)

    # Check for any error during scraping
    if "Error during scraping" in scraped_content:
        return scraped_content

    # Step 2: Analyze the scraped content
    messages = [
        {"role": "system", "content": "You are an agent that analyzes content and extracts key insights."},
        {"role": "user", "content": f"Analyze the following content: {scraped_content}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=messages
    )
    analysis_summary = response.choices[0].message.content

    # Step 3: Write the summary based on the analysis
    messages = [
        {"role": "system", "content": "You are an agent that writes summaries of research."},
        {"role": "user", "content": f"Write a summary based on this analysis: {analysis_summary}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=messages
    )
    final_summary = response.choices[0].message.content

    return final_summary

# Streamlit App UI
st.title("Multi-Agent System for 🚀 ANY AI/ML Model: 🌐 Web Scraping & 📝 Content Analysis Powered by the 🔗 AI/ML API")
st.caption("This app scrapes a website, analyzes the content, and generates a summary using AI/ML API.")

# Input for AI/ML API Key
st.subheader("AI/ML API Key Setup")
set_aiml_api_key()

# Initialize OpenAI client only after API key is set
if 'AIMLAPI_API_KEY' in os.environ and os.environ['AIMLAPI_API_KEY']:
    # Initialize the OpenAI client after API key is entered
    client = initialize_openai_client()

    # Input field for the website URL
    url = st.text_input("Enter the URL of the website you want to scrape", placeholder="https://example.com")

    # Run Workflow button
    if st.button("Run Workflow"):
        if url:
            # Create a progress bar
            progress_bar = st.progress(0)
            
            # Step 1: Scrape the website
            with st.spinner("Step 1: Scraping the website..."):
                scraped_content = scrape_website(url)
            progress_bar.progress(33)
            st.success("Step 1 complete: Website scraped")
            
            if "Error during scraping" in scraped_content:
                st.error(scraped_content)
                progress_bar.empty()
            else:
                # Step 2: Analyze the scraped content
                with st.spinner("Step 2: Analyzing the content..."):
                    messages = [
                        {"role": "system", "content": "You are an agent that analyzes content and extracts key insights."},
                        {"role": "user", "content": f"Analyze the following content: {scraped_content}"}
                    ]
                    response = client.chat.completions.create(
                        model="gpt-4o-mini-2024-07-18",
                        messages=messages
                    )
                    analysis_summary = response.choices[0].message.content
                progress_bar.progress(66)
                st.success("Step 2 complete: Content analyzed")
                
                # Step 3: Write the summary based on the analysis
                with st.spinner("Step 3: Writing the final summary..."):
                    messages = [
                        {"role": "system", "content": "You are an agent that writes summaries of research."},
                        {"role": "user", "content": f"Write a summary based on this analysis: {analysis_summary}"}
                    ]
                    response = client.chat.completions.create(
                        model="gpt-4o-mini-2024-07-18",
                        messages=messages
                    )
                    final_summary = response.choices[0].message.content
                progress_bar.progress(100)
                st.success("Step 3 complete: Final summary written")
                
                # Display the final report in a more visually appealing way
                st.markdown("### 📊 Final Report")
                st.info(final_summary)
                
                # Add a download button for the report
                st.download_button(
                    label="Download Report",
                    data=final_summary,
                    file_name="web_analysis_report.txt",
                    mime="text/plain"
                )
        else:
            st.error("Please enter a valid URL.")
else:
    st.warning("Please set your AI/ML API Key to proceed.")

# Footer with credits
st.markdown("---")
st.markdown("**Developed by Jad Tounsi El Azzoiani**")
st.markdown("[GitHub Repo](https://github.com/jadouse5) | [LinkedIn](https://www.linkedin.com/in/jad-tounsi-el-azzoiani-87499a21a/)")