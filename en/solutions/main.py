emoji = '🍽️😋'.replace('😋', '🤢')

protein = 'TOFU'.replace('FU', 'AD')         # ➝ TOAD
veg_1 = 'CARROT'.replace('CAR', '')          # ➝ ROT
carb = 'RICE'.replace('R', 'L')              # ➝ LICE
veg_2 = 'PEAS'
garnish = 'MINT'
side = 'BOILED EGGS'

print(
    f'{emoji} Start with a scoop of {carb.lower()}',
    f'Top with diced {veg_1.lower()} and {veg_2.lower()}',
    f'Add grilled {protein.title()}',
    f'Garnish with {garnish.lower()}',
    f'Serve with a side of {side.lower()}',
    sep='\n'
)
