from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv(".env.local")
DEEPGRAM_API_KEY="dd344d2e280993acfa548378e05b6518a0059bc7"
GOOGLE_API_KEY="AIzaSyDd_A5fKDUkQ02Xz2HGhouWnc-v6bBksNI"
CARTESIA_API_KEY="sk_car_u2nMptvCWgNn4sc71V4m9E"

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi", api_key=DEEPGRAM_API_KEY),
        llm=google.LLM(model="gemini-1.5-flash", api_key=GOOGLE_API_KEY),
        tts=cartesia.TTS(model="sonic-2", voice="f786b574-daa5-4673-aa0c-cbe3e8534c02", api_key=CARTESIA_API_KEY),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
