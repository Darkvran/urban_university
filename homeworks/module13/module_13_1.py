import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")
    for _ in range(5):
        await asyncio.sleep(1/power)
        print(f"Силач {name} поднял {_+1}")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Арнольд Шварценеггер", 5))
    task2 = asyncio.create_task(start_strongman("Ронни Колеман", 7))
    task3 = asyncio.create_task(start_strongman("Настя", 14))
    await task1
    await task2
    await task3
asyncio.run(start_tournament())