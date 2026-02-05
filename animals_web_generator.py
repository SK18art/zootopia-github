import json

def read_HTML(file_path):
  """ Reads the data from the HTML file"""
  with open(file_path, "r", encoding="utf-8") as handle:
    return handle.read()


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal(animal):
  """ This function serializes the whole data to be presented in the HTML

  """
  HTML_text = ""
  try:
    # Appending data to the HTML string
    HTML_text += '<li class="cards__item">'
    HTML_text += f'<div class="card__title"> {animal["name"]}<br/></div>\n'
    HTML_text += '<div class="card__text">'
    HTML_text += '<ul>'
    HTML_text += f"<li class = 'card__points' ><strong> Diet: </strong> {animal["characteristics"]["diet"]}</li>\n"

    HTML_text += f"<li class = 'card__points' ><strong>Location: </strong> {animal["locations"][0]}</li>\n"
    if "type" in animal["characteristics"]:
      HTML_text += f"<li class = 'card__points' ><strong>Type: </strong> {animal["characteristics"]["type"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Kingdom: </strong> {animal["taxonomy"]["kingdom"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Scientific Name: </strong> {animal["taxonomy"]["scientific_name"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Life Span: </strong> {animal["characteristics"]["lifespan"]}</li>\n"
    HTML_text += '</ul>'
    HTML_text += '</div>'
    HTML_text += "</li>\n"

  except KeyError:
    HTML_text += "\n"

  return HTML_text

def main():
  """
  This is the main function where the functions will be called and executed.
  """

  # Loading the animal's data from the JSON file
  animals_data = load_data('animals_data.json')

  old_HTML = read_HTML("animals_template.html")

  # to store the HTML text
  HTML_output = ""

  # To generate the display info from the json file
  for animal in animals_data:
    HTML_output += serialize_animal(animal)

  # Replacing the animal info is the old HTML Template
  new_HTML = old_HTML.replace("__REPLACE_ANIMALS_INFO__", HTML_output)

  # Creating a new HTML file with the new HTML text
  with open("animals.html", "w") as animal_HTML:
    animal_HTML.write(new_HTML)


if __name__ == "__main__":
  main()