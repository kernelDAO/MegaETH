![megaeth_soft](https://github.com/user-attachments/assets/728a8443-c278-43ec-a7d4-0b51874bb4e7)

> [!WARNING]  
> This is my first software using web3.py. I am not an experienced web3 developer. If you find a shitty code, a bug, or a way to make something better - open a pull request.

# MegaETH by kernelDAO

A simple software for swapping, staking, minting on MegaETH testnet.

## Installation

1. Clone the repository:
   
```https://github.com/kernelDAO/MegaETH```

```cd MegaETH```


2. Install dependencies:
```pip install -r requirements.txt```


3. Add your wallet address and private key in .env file.


4. Configure the software by adding/removing actions.


## Configuration
### Modes
This software has three modes.

1 - Will execute **user-defined actions** in order(from actions.py) **once**. 

2 - Will **infinitely** execute **random** actions. 

3 - Will **infinitely** execute **user-defined actions in order** (from actions.py).

### actions.py Configuration

In actions.py file you have array called ```ACTIONS```. Customization of user actions for the first and third modes is performed by changing this array. For example:


```
ACTIONS = [
    ("Mint cUSD", mint_cusd, False),
    ("Send GM", send_gm, True),
    ("Random Swap", swap_tokens, True),
    ("tkUSDC staking", stake_tkusdc, True),
    ("Swap all to ETH", swap_all_tokens_to_eth, True),
]
```

This config will execute actions: Mint cUSD, Send GM, Random Swap, tkUSDC staking and Swap all to ETH once in the first and infinitely in second mode.

To make custom action chains you need to change the ```ACTIONS``` array by adding or removing lines. All lines are available here, or at the bottom of the actions.py file starting from line 27 for Russian and from line 57 for English languages.

**All actions:** 
```
(“tkUSDC staking”, stake_tkusdc, True),
(“tkUSDC unstaking”, unstake_tkusdc, True),
(“Mint cUSD”, mint_cusd, False),
(“Random Swap”, swap_tokens, True),
(“Swap all to ETH”, swap_all_tokens_to_eth, True),
(“Send GM”, send_gm, True),
```
```tkUSDC staking``` = *Staking via Teko*

```tkUSDC unstaking``` = *Unstaking via Teko*

```Mint cUSD``` = *Mint cUSD*

```Random Swap``` = *Random Swaps via gte*

```Swap all to ETH``` = *Swap all tokens to ETH*

```Send GM``` = *Send gm via onchaingm (once every 24 hours)*
