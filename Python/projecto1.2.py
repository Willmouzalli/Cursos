from abc import ABC, abstractmethod


class NamesRepository(ABC):  # Capa 1. Contrato
    @abstractmethod
    def get_names(self) -> list:
        pass

    @abstractmethod
    def save(self, name):
        pass

    @abstractmethod
    def delete(self, name):
        pass

    @abstractmethod
    def update(self, old_name, new_name):
        pass


class Names(NamesRepository):  # Capa 2. Infraestructura
    def __init__(self):
        self.names = []

    def get_names(self) -> list:
        return self.names

    def save(self, name):
        self.names.append(name)

    def delete(self, name):
        if name in self.names:
            self.names.remove(name)

    def update(self, old_name, new_name):
        if old_name in self.names:
            index = self.names.index(old_name)
            self.names[index] = new_name


class Apellidos(NamesRepository):  # Capa 2. Infraestructura alternativa
    def __init__(self):
        self.apellidos = []

    def get_names(self) -> list:
        return self.apellidos

    def save(self, name):
        self.apellidos.append(name)

    def delete(self, name):
        if name in self.apellidos:
            self.apellidos.remove(name)

    def update(self, old_name, new_name):
        if old_name in self.apellidos:
            index = self.apellidos.index(old_name)
            self.apellidos[index] = new_name


class NameManager:  # Capa 3. Lógica de negocio
    def __init__(self, repository: NamesRepository):
        self.repository = repository

    def add_name(self, name):
        self.repository.save(name)

    def remove_name(self, name):
        self.repository.delete(name)

    def change_name(self, old_name, new_name):
        self.repository.update(old_name, new_name)

    def list_names(self) -> list:
        return self.repository.get_names()


class ConsoleController:  # Capa 4. Interfaz de Usuario
    def __init__(self, app: NameManager):
        self.app = app

    def run(self):
        while True:
            print("\nOpciones:")
            print("1. Agregar nombre")
            print("2. Eliminar nombre")
            print("3. Actualizar nombre")
            print("4. Listar nombres")
            print("5. Salir")

            eleccion = input("Seleccione una opción: ")

            if eleccion == "1":
                name = input("Ingrese el nombre a agregar: ")
                self.app.add_name(name)
                print(f"Nombre '{name}' agregado.")
            elif eleccion == "2":
                name = input("Ingrese el nombre a eliminar: ")
                self.app.remove_name(name)
                print(f"Nombre '{name}' eliminado.")
            elif eleccion == "3":
                old_name = input("Ingrese el nombre a actualizar: ")
                new_name = input("Ingrese el nuevo nombre: ")
                self.app.change_name(old_name, new_name)
                print(f"Nombre '{old_name}' actualizado a '{new_name}'.")
            elif eleccion == "4":
                names = self.app.list_names()
                print("Nombres almacenados:")
                for name in names:
                    print(f"- {name}")
            elif eleccion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    names = Apellidos()  # Capa 2. Infraestructura
    app = NameManager(names)  # Capa 3. Lógica de negocio

    consoleController = ConsoleController(app)  # Capa 4. Interfaz de Usuario
    consoleController.run()
