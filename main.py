import asyncio
import random
import time
from actions import ACTIONS, ALL_ACTIONS
import os

os.system("cls")

print("""
 __                                    __   ______        _        ___    
[  |  _                               [  | |_   _ `.     / \\     .'   `.  
 | | / ] .---.  _ .--.  _ .--.  .---.  | |   | | `. \\   / _ \\   /  .-.  \\ 
 | '' < / /__\\[ `/'`\\][ `.-. |/ /__\\ | |   | |  | |  / ___ \\  | |   | | 
 | |`\\ \\| \\__.\\ | |     | | | || \\__.\\ | |  _| |_.' /_/ /   \\ \\_\\  `-'  / 
[__|  \\_]'.__.'[___]   [___||__]'.__.'[___]|______.'|____| |____|`.___.'  
                       MEGAETH SOFTWARE
      Open-source and free software made by: t.me/kerneldrops
""")


def get_user_choice():
    print("Choose mode:")
    print("1: User-defined procedure (from actions.py) [once]")
    print("2: Random (infinite loop with all actions)")
    print("3: Infinite loop (user-defined actions in order)")
    
    choice = input("Enter your number: ")
    return choice


async def execute_actions(actions):
    for action_name, action_func, is_async in actions:
        print(f"\n🚀 Executing: {action_name}...")
        try:
            if is_async:
                result = await action_func()
            else:
                result = action_func()

            if isinstance(result, str):
                print(f"✅ {action_name} done! TX: {result}")
        except Exception as e:
            print(f"❌ Error while executing: {action_name}: {e}")

        time.sleep(2)


async def main():
    choice = get_user_choice()

    if choice == "2":
        while True:
            tasks = ALL_ACTIONS.copy()
            random.shuffle(tasks)
            await execute_actions(tasks)
            print("\n🔄 Starting new random cycle.\n")
            time.sleep(5)

    elif choice == "3":
        while True:
            await execute_actions(ACTIONS)
            print("\n🔄 Repeating user-defined actions...\n")
            time.sleep(5)
    else:
        await execute_actions(ACTIONS)

asyncio.run(main())
