import pystache

render = pystache.render(
    'Hi {{person}}',
    {'person': 'aa'}

)

print(render)
