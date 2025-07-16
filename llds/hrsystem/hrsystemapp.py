from emp import Emp
from asyncio import Queue,gather
import asyncio

users_db = {
    1:Emp(1,"ram","inactive"),
    2:Emp(2,"rahul","inactive"),
    3:Emp(3,"raja","inactive"),
    20:Emp(20,"shyam","active")
}



#HR
async def send(ids:list[int],q:Queue):
    for id in ids:
        await q.put(id)
    await q.put(None)

async def security(id:int):
    emp =  users_db[id]
    print(f"user :: {emp.name}, id: {emp.id} set status to :: {emp.status}")


async def worker(q:Queue):
    while(True):
        id = await q.get()
        if id is None:
            q.task_done()
            break
        await security(id)
        q.task_done()

async def main():
    queue = Queue()
    await gather(send([1,2,3],queue),worker(queue))
    await queue.join()
    print("all processing completed")

asyncio.run(main()) 