from openai import OpenAI


response = openai.completions.create(
  model=" ",
  prompt="Dime un numero aleatorio del 1 al 10",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)

"""## Imprimir respuesta"""

response.choices[0].text