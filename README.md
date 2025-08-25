Chatbot(Voice + Text)
=====================

# Project Setup:
- Install the LiveKit CLI:
  ``` winget install LiveKit.LiveKitCLI```
- Link your LiveKit Cloud project to the CLI:
  ``` lk cloud auth ```
- Project initialization:
  ``` uv init```
- Environment variables:
  ``` DEEPGRAM_API_KEY=<Your Deepgram API Key>
      OPENAI_API_KEY=<Your OpenAI API Key>
      CARTESIA_API_KEY=<Your Cartesia API Key>
      LIVEKIT_API_KEY=<your API Key>
      LIVEKIT_API_SECRET=<your API Secret>
      LIVEKIT_URL=wss://chatbot-ur0wqhe0.livekit.cloud
  ```
- Download model files
  ``` To use the turn-detector, silero, or noise-cancellation plugins, you first need to download the model files:
      uv run filename.py download-files
  ```
- Speak to your agent:
  ``` uv run filename.py console```

