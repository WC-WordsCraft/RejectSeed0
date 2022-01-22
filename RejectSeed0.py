from mcdreforged.api.all import *

PLUGIN_METADATA = {
     'id': 'rejectseed0',
     'version': '1.0.0',
     'name': 'RejectSeed0 plugin',
     'link':'https://github.com/WC-WordsCraft/RejectSeed0',
     "author": ["话痨de白菜","曲奇Onfree"],
}

NAME = PLUGIN_METADATA['name']
LINK = PLUGIN_METADATA['link']

def seed(server:PluginServerInterface):
     try:
        seed = server.rcon_query('/seed').split('[')[1].split(']')[0]
        return RTextList(
            RTextTranslation('commands.seed.success'),
            '[', RText(seed, RColor.green)
            .c(RAction.copy_to_clipboard, seed)
            .h(RTextTranslation('chat.copy.click')), ']'
        )
     except Exception:
          warning = RText(
               f'§cPlugin {NAME} §lCANNOT§c get server seed by §lRCON§c, please checkout config of §lMCDR§c!').c(RAction.open_url, LINK).h(f'§lDocs§r: §n{LINK}§r')
          server.logger.warning(warning.to_plain_text())
          return RText(warning)

def on_player_joined(server: PluginServerInterface, player: str, info: Info):
     try:
          seed = server.rcon_query('/seed').split('[')[1].split(']')[0]
          if seed == "0":
               server.execute("/kick @a")
               warning = RText("§c种子为0!服务器地图可能出现问题!")
               server.logger.warning(warning.to_plain_text())
     except:
          warning = RText("§c无法读取种子!，服务器可能没有开启rcon!")
          server.logger.warning(warning.to_plain_text())

def on_load(server:PluginServerInterface,info:Info):
     server.logger.info("RejectSeed0")
     server.register_help_message("!!RejectSeed0","获取帮助")
     server.register_command(Literal("!!RejectSeed0").runs(
          lambda src:src.reply(RTextList("此插件是防止地图的种子seed变成0"))))
     server.register_command(
        Literal('!!seed').runs(lambda src: src.reply(seed(server)))
    )