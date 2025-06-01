import asyncio
async def main():
    print("fetching data")
    await asyncio.sleep(2)
    print("Hello  ia m asyio !!")


if __name__=="__main__":
    print(asyncio.__file__)
    asyncio.run(main())