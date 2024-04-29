import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.mementos = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.mementos.append(memento)
        if len(self.mementos) > 4:
            self.mementos.pop(0)  # Eliminar el más antiguo si hay más de 4 estados almacenados

    def undo(self, num_back):
        if num_back >= len(self.mementos):
            num_back = len(self.mementos) - 1
        memento = self.mementos[-1 - num_back]
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, num_back):
        writer.undo(num_back)


if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar el segundo estado anterior")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar el estado más antiguo")
    caretaker.undo(writer, 3)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
