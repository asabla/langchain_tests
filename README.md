# LangChain Azure OpenAI Tests

This project demonstrates how to use LangChain with Azure OpenAI services.

## Setting Up uv

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. To set it up:

1. Install uv:
   ```bash
   curl -sSf https://install.ultraviolet.rs | sh
   ```

2. Create a virtual environment:
   ```bash
   uv venv
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate   # For Unix/macOS
   # OR
   .venv\Scripts\activate      # For Windows
   ```

4. Install dependencies:
   ```bash
   uv sync
   ```

## Configuration

1. Create a `.env` file with the following variables (already done):
   ```
   AZURE_ENDPOINT=your_azure_openai_endpoint
   AZURE_DEPLOYMENT=your_azure_deployment_name
   ```

2. Azure Authentication:
   - This application uses `DefaultAzureCredential` for authentication
   - Make sure you're logged in with the Azure CLI (`az login`) or have the appropriate environment variables set

## Running the Application

Execute the application with:

```bash
uv python main.py
```

This will connect to Azure OpenAI and ask a question about LangChain.