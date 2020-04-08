from .filterAll import FilterAll
from redbot.core.bot import Red


def setup(bot: Red):
    bot.add_cog(FilterAll(bot))
