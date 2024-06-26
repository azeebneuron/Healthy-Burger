from uagents import Agent, Context
 
alice = Agent(name="alice", seed="alice recovery phrase")
 
@alice.on_event("startup")
async def introduce_agent(ctx: Context):
    ctx.logger.info(f"Hello, I'm agent {ctx.name} and my address is {ctx.address}.")
 
if __name__ == "__main__":
    alice.run()

