import asyncio

async def task1():
    print("Send first Email")
    asyncio.create_task(task2())
    await asyncio.sleep(5) #Simulates that the email reply comes after 2 seconds
    print("First Email reply")


async def task2():
    print("Send Second Email")
    asyncio.create_task(task3())
    await asyncio.sleep(2) #Simulates that the email reply comes after 2 seconds
    print("Second Email reply")


async def task3():
    print("Send third  Email")
    await asyncio.sleep(2) #Simulates that the email reply comes after 2 seconds
    print("third Email reply")

 
asyncio.run(task1())