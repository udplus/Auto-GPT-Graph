import pynecone as pc

config = pc.Config(
    app_name="Auto-GPT UI",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
