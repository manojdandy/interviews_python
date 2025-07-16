from asyncio import Queue,gather
import asyncio
async def producer(q:Queue):
    for i in range(10):
       await q.put(i)
       print(f"producer :: {i}")
       await asyncio.sleep(1)


async def consumer(q:Queue):
   while(True):
       item = await q.get()
       print(f"consumer :{item}")
       q.task_done()


async def main():
    q = Queue()
    await gather(producer(q),consumer(q))

asyncio.run(main())