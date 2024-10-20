# 🐝 Multi-Agent System for 🚀 ANY AI/ML Model: 🌐 Web Scraping & 📝 Content Analysis Powered by the 🔗 AI/ML API

This project demonstrates a multi-agent system that automates web scraping, content analysis, and summary generation using the AI/ML API. It is built using **Streamlit** for the user interface, **BeautifulSoup** for web scraping, and the **AI/ML API** for text generation and analysis.


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6kf1hkm9emhheo9rxsfd.png)

The app enables you to dynamically change the model and modify any agent in the workflow to suit different use cases. Simply provide your AI/ML API key, and you can use any model supported by the AI/ML API.

# Get your AI/ML API

You can obtain your AI/ML API key by visiting the following link:

[AI/ML API](https://aimlapi.com/?via=jad)

## Features

- **Web Scraping**: Scrapes the content of a given website URL using BeautifulSoup.
- **Content Analysis**: Analyzes the scraped content to extract key insights using the AI/ML API.
- **Summary Generation**: Generates a detailed summary of the analyzed content.
- **Streamlit UI**: Interactive user interface that allows users to enter the website URL and view the generated report.
- **Flexible AI Models**: Supports any model from the AI/ML API. You can change the model used for content analysis and summary generation dynamically.
- **Agent Customization**: Modify the behavior of each agent (scraping, analyzing, summarizing) by changing the instructions, functions, or models.

## How It Works

1. **AI/ML API Key Input**
   - The app dynamically sets the API key using an input field. The key is stored in the environment and used for making API calls to the AI/ML API.

2. **Web Scraping**
   - The app scrapes the provided website URL using BeautifulSoup and extracts the text content from the website's HTML.

3. **Content Analysis**
   - The scraped content is analyzed by the AI/ML API using a chat completion model to extract key insights.

4. **Summary Generation**
   - A detailed summary is generated using the AI/ML API based on the content analysis.

5. **Download Report**
   - The final summary can be downloaded as a text file directly from the Streamlit interface.

## Installation

### Prerequisites

- Python 3.10+
- Streamlit for the interactive web interface.
- BeautifulSoup for web scraping.
- Requests for handling HTTP requests.
- AI/ML API Key for making API calls.

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/jadouse5/aimlapi-webscraper-agents.git
    cd aimlapi-webscraper-agents
    ```

2. **Set Up a Virtual Environment:**

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On macOS/Linux
    myenv\Scripts\activate  # On Windows
    ```

3. **Install Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys**:  
   Create a `.env` file in the project root and add your AI/ML API key:

    ```bash
    echo "AIMLAPI_API_KEY=your-api-key-here" > .env
    ```

5. **Run the Application:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Open the Web Interface**:  
   Once the application is running, it will open in your default browser. If not, go to [http://localhost:8501](http://localhost:8501) manually.

2. **Set Your AI/ML API Key**:  
   Input your AI/ML API Key in the text box to authenticate and allow the app to access the API.

3. **Input Website URL**:  
   Enter the URL of the website you want to scrape in the provided input box.

4. **Run Workflow**:  
   Click the "Run Workflow" button to start scraping the website, analyzing its content, and generating a summary report.

5. **Modify Models or Agents**:  
   You can modify the AI models used in each agent by adjusting the code, allowing you to experiment with different models for scraping, analysis, or summarizing.

6. **Download Report**:  
   Once the workflow completes, you can download the generated report by clicking the "Download Report" button.

## Key Components

1. **Web Scraping**:  
   Scrapes the text content from the provided website URL using BeautifulSoup.

2. **Content Analysis**:  
   The scraped content is analyzed using the AI/ML API, extracting key insights.

3. **Summary Generation**:  
   A detailed summary is generated based on the analysis using another AI model call.

## Code Example

Here’s an example of how the system orchestrates the workflow:

```python
def orchestrate_workflow(client, url):
    # Step 1: Scrape the website
    scraped_content = scrape_website(url)

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
```

## Customization

### Using Different Models

You can change the models used in the agents by modifying the `model` parameter in the `orchestrate_workflow` function. The AI/ML API supports multiple models, allowing you to experiment with different models for each task:

- **Scraping Agent**: Modify the scraping agent to handle different types of content or preprocess the data differently.
- **Analysis Agent**: Choose a model that best suits your analysis needs, such as summarization or topic extraction.
- **Summary Agent**: Use a model that generates detailed, concise, or creative summaries depending on your goal.

### Modify Agents

Each agent is highly customizable. Adjust the instructions or add new functions for more advanced workflows.

## Future Improvements

- **Advanced Scraping**: Improve the scraper to handle dynamic content (e.g., JavaScript-heavy sites).
- **More Detailed Analysis**: Expand the analysis to include sentiment analysis or categorization.
- **Multilingual Support**: Extend the app to support scraping, analyzing, and summarizing content in multiple languages.
- **CAPTCHA Handling**: Add support for bypassing or manually entering CAPTCHAs when scraping protected websites.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Developed by: **Jad Tounsi El Azzoiani**  
GitHub: [Jad Tounsi El Azzoiani](https://github.com/jadouse5)  
LinkedIn: [Jad Tounsi El Azzoiani](https://linkedin.com/in/jad-tounsi-el-azzoiani)
