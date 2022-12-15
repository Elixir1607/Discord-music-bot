import discord
import os 
from discord.ext import commands
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='%')
bot.remove_command('help')

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

bot.run('MTA1Mjk4NDQ2ODAyMzAyMTY2OA.Gwndpz.a1fi7qP1B1Cc6K4vv_p_bDNJKT2K6z-o_yCgkM')