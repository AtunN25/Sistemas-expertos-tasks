import sys

class Nodo():
    def __init__(self, estado, padre, accion,valorHeuristico,costo_camino=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.valorHeuristico = valorHeuristico
        self.costo_camino = costo_camino    
        self.valor = self.costo_camino + self.valorHeuristico  


def Heuristico(estado,meta):
    x1,y1 = estado
    x2,y2 = meta
    return abs(x2-x1) + abs(y2-y1)

#se ordenara de acuerdo al menor valor heuristico ,usando pop para extraer el ultimo valor
class FronteraPrioridad():
    def __init__(self):
        self.frontera = []

    def add(self, nodo):
        self.frontera.append(nodo)
        self.frontera.sort(key=lambda x: (x.valor))

    def contiene_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)

    def empty(self):
        return len(self.frontera) == 0

    def remove(self):
        if self.empty():
            raise Exception("frontera vacia")
        else:
            return self.frontera.pop(0) 


class Laberinto():

    def __init__(self, nombreArchivo):

        self.heuristicas = {} # para mostrar los valores heuristicos en los cuadros

        # Leer el archivo y establecer la altura y la anchura del laberinto
        with open(nombreArchivo) as f:
            contenido = f.read()

        # Validar el inicio y el objetivo
        if contenido.count("A") != 1:
            raise Exception("el laberinto debe tener exactamente un punto de partida")
        if contenido.count("B") != 1:
            raise Exception("el laberinto debe tener exactamente un objetivo")

        # Determinar la altura y la anchura del laberinto
        contenido = contenido.splitlines()
        self.altura = len(contenido)
        self.anchura = max(len(linea) for linea in contenido)

        # Seguimiento de paredes
        self.paredes = []
        for i in range(self.altura):
            fil = []
            for j in range(self.anchura):
                try:
                    if contenido[i][j] == "A":
                        self.inicio = (i, j)
                        fil.append(False)
                    elif contenido[i][j] == "B":
                        self.meta = (i, j)
                        fil.append(False)
                    elif contenido[i][j] == " ":
                        fil.append(False)
                    else:
                        fil.append(True)
                except IndexError:
                    fil.append(False)
            self.paredes.append(fil)

        self.solucion = None


    def print(self):
        solucion = self.solucion[1] if self.solucion is not None else None
        print()
        for i, fil in enumerate(self.paredes):
            for j, col in enumerate(fil):
                if col:
                    print("█", end="")
                elif (i, j) == self.inicio:
                    print("A", end="")
                elif (i, j) == self.meta:
                    print("B", end="")
                elif solucion is not None and (i, j) in solucion:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()


    def vecinos(self, estado):
        fil, col = estado
        candidatos = [
            ("arriba", (fil - 1, col)),
            ("abajo", (fil + 1, col)),
            ("izquierda", (fil, col - 1)),
            ("derecha", (fil, col + 1))
        ]

        resultado = []
        for accion, (r, c) in candidatos:
            if 0 <= r < self.altura and 0 <= c < self.anchura and not self.paredes[r][c]:
                resultado.append((accion, (r, c)))
        return resultado


    def solve(self):
        """Encuentra una solución al laberinto, si existe."""

        # Llevar la cuenta del número de estados explorados
        self.numExplorados = 0

        # Inicializar la frontera sólo a la posición de inicio
        inicio = Nodo(estado=self.inicio, padre=None, accion=None,valorHeuristico=Heuristico(self.inicio, self.meta),costo_camino=0)
        frontera = FronteraPrioridad()
        frontera.add(inicio)

        # Inicializar un conjunto explorado vacío
        self.explorado = set()

        # Mantenga el bucle hasta encontrar la solución
        while True:

            # Si no queda nada en la frontera, entonces no hay camino
            if frontera.empty():
                raise Exception("no solucion")

            # Elige un nodo de la frontera
            nodo = frontera.remove()
            self.numExplorados += 1

            # Si nodo es la meta, entonces tenemos una solucion
            if nodo.estado == self.meta:
                acciones = []
                celdas = []
                while nodo.padre is not None:
                    acciones.append(nodo.accion)
                    celdas.append(nodo.estado)
                    nodo = nodo.padre
                acciones.reverse()
                celdas.reverse()
                self.solucion = (acciones, celdas)
                return

            # Marcar nodo como explorado
            self.explorado.add(nodo.estado)

            # Añadir vecinos a frontera
            for accion, estado in self.vecinos(nodo.estado):
                
                nuevo_costo_camino = nodo.costo_camino + 1

                if not frontera.contiene_estado(estado) and estado not in self.explorado:

                    nuevo_valor_heuristico = Heuristico(estado, self.meta)  # Calcular heurística
                    child = Nodo(estado=estado, padre=nodo, accion=accion,valorHeuristico=nuevo_valor_heuristico,costo_camino=nuevo_costo_camino)
                    frontera.add(child)
                    
                    self.heuristicas[estado] = {
                        'g': nuevo_costo_camino,
                        'h': nuevo_valor_heuristico,
                        'f': nuevo_costo_camino + nuevo_valor_heuristico
                    }


    def imagen_salida(self, nombreArchivo, mostrar_solucion=True, mostrar_explorado=False):
        from PIL import Image, ImageDraw,ImageFont
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.anchura * cell_size, self.altura * cell_size),
            "black"
        )
        dibujo = ImageDraw.Draw(img)

        try:
            font = ImageFont.load_default()
        except:
            font = None

        solucion = self.solucion[1] if self.solucion is not None else None
        for i, fil in enumerate(self.paredes):
            for j, col in enumerate(fil):

                # Paredes
                if col:
                    fill = (40, 40, 40)

                # Inicio
                elif (i, j) == self.inicio:
                    fill = (255, 0, 0)

                # Meta
                elif (i, j) == self.meta:
                    fill = (0, 171, 28)

                # Solución
                elif solucion is not None and mostrar_solucion and (i, j) in solucion:
                    fill = (220, 235, 113)

                # Explorado
                elif solucion is not None and mostrar_explorado and (i, j) in self.explorado:
                    fill = (212, 97, 85)

                # Celda vacía
                else:
                    fill = (237, 240, 252)

                # Dibujar celda
                dibujo.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

                #proceso de agregado de los numeros en los recuadros
                if (i, j) in self.heuristicas:
                    datos = self.heuristicas[(i, j)]
                    text = f"{datos['g']}+{datos['h']}={datos['f']}"  
                    
                    if font:
                        # Calcular tamaño del texto
                        left, top, right, bottom = dibujo.textbbox((0, 0), text, font=font)
                        text_width, text_height = right - left, bottom - top
                        
                        # Dibujar texto centrado
                        dibujo.text(
                            (j * cell_size + cell_size/2 - text_width/2,
                            i * cell_size + cell_size/2 - text_height/2),
                            text,
                            fill=(0, 0, 0),  # Color negro
                            font=font
                        )
                    else:
                        # Fallback sin fuente
                        dibujo.text(
                            (j * cell_size + cell_size/2,
                            i * cell_size + cell_size/2),
                            text,
                            fill=(0, 0, 0)
                        )

        img.save(nombreArchivo)


if len(sys.argv) != 2:
    sys.exit("Usage: python laberinto.py laberinto.txt")

m = Laberinto(sys.argv[1])
print("Laberinto:")
m.print()
print("Resolviendo...")
m.solve()
print("Estados Explorados:", m.numExplorados)
print("Solution:")
m.print()
m.imagen_salida("laberinto.png", mostrar_explorado=True)
