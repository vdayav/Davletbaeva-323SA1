colors = { "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "желтый": (255, 255, 0),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0) }

print("Все цвета:")
for name, rgb in colors.items():
    print(f"{name}: {rgb}")

red = colors["красный"]   
blue = colors["синий"]     

mix_r = (red[0] + blue[0]) // 2
mix_g = (red[1] + blue[1]) // 2
mix_b = (red[2] + blue[2]) // 2

mix_color = (mix_r, mix_g, mix_b)
print(f"Красный {red} + Синий {blue} = {mix_color}")

green = colors["зеленый"]  

inv_r = 255 - green[0]
inv_g = 255 - green[1]
inv_b = 255 - green[2]

invert = (inv_r, inv_g, inv_b)
print(f"Зеленый {green}, Инвертированный: {invert}")

yellow = colors["желтый"]
blue = colors["синий"]

mixed2 = ( (yellow[0] + blue[0]) // 2,
    (yellow[1] + blue[1]) // 2,
    (yellow[2] + blue[2]) // 2 )
print(f"Желтый {yellow} + Синий {blue} = {mixed2}")