import json

#other config
WIDTH : int = 600 #px
HEIGHT : int = 600 #px
WIDTH_TABLET = 300
SIZE_CELL : int = 30 #px
COLUMN_TABLET :int = WIDTH_TABLET//SIZE_CELL
ROW_TABLET :int = HEIGHT//SIZE_CELL

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

DIR_FILENAME_TO_COLORS = "assets\json\list_colors.json"

def getDataonJSON(dir_filename: str) -> dict | None:
    file_json = dir_filename
    
    data : dict = None

    try:

        with open(file_json, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        print(f"Error: El archivo {file_json} no existe.")
    except json.JSONDecodeError:
        print(f"Error: El archivo {file_json} no contiene un JSON válido.")
    except KeyError as e:
        print(f"Error: Falta la clave {e} en los datos del archivo JSON.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return data