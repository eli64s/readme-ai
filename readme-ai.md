Thank you for the suggestion @krrishdholakia! Using the OpenAI SDK or a library like LangChain are certainly good options worth considering. Here are some thoughts on the current approach:

The raw REST API calls give us more control over the requests and handling responses. But the SDKs do provide a nicer abstraction.
Initially we wanted the flexibility of switching between different LLMs easily, so went with direct calls. But the SDKs and LangChain support this as well.
For simplicity we started with REST, but integrating with SDKs/LangChain could definitely improve the code.
Litellm in particular looks like a great way to standardize and consolidate the requests. And support more providers easily.
