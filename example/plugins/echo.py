from kutana import Plugin

plugin = Plugin(name="Grand echo")

@plugin.on_startswith_text("echo")
async def on_echo(message, attachments, env):
    await env.reply("{}".format(env.body))
