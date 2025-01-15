import asyncio

list_strongmans = [['Pasha', 3], ['Denis', 4], ['Apollon', 5]]


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнование.")
    for i in range(1, 6):
        await asyncio.sleep(10 / power)
        print(f"Силач {name} поднял {i} шар.")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman(*list_strongmans[0]))
    task2 = asyncio.create_task(start_strongman(*list_strongmans[1]))
    task3 = asyncio.create_task(start_strongman(*list_strongmans[2]))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
