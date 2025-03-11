import os
from azure.identity import DefaultAzureCredential
from langchain_openai import AzureChatOpenAI

def main():
    # Setup token for Azure Chat OpenAI
    credential = DefaultAzureCredential()
    azure_ad_token = credential.get_token("https://cognitiveservices.azure.com/.default")

    chat = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_DEPLOYMENT"),
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_version="2023-05-15",
        azure_ad_token=azure_ad_token.token,
    )

    response = chat.invoke("What can you tell me about Langchain?")
    print(response)


if __name__ == "__main__":
    main()