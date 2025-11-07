from abc import ABC, abstractmethod


class NamesRepository(ABC):
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


class NamesDict(NamesRepository):
    def __init__(self):
        self.names_dict = {}

    def get_names(self):
        return list(self.names_dict.keys())

    def save(self, name):
        if name not in self.names_dict:
            self.names_dict[name] = name

    def delete(self, name):
        if name in self.names_dict:
            del self.names_dict[name]

    def update(self, old_name, new_name):
        if old_name in self.names_dict:
            del self.names_dict[old_name]
            self.names_dict[new_name] = new_name


class Names(NamesRepository):
    def __init__(self):
        self.names_list = []

    def get_names(self):
        return self.names_list

    def save(self, name):
        self.names_list.append(name)

    def delete(self, name):
        if name in self.names_list:
            self.names_list.remove(name)

    def update(self, old_name, new_name):
        for i in range(len(self.names_list)):
            if self.names_list[i] == old_name:
                self.names_list[i] = new_name
                break


class NameManager:
    def __init__(self, names_repo: NamesRepository):
        self.names_instance = names_repo

    def display_names(self):
        for name in self.names_instance.get_names():
            print(name)

    def add_name(self, name):
        self.names_instance.save(name)

    def remove_name(self, name):
        self.names_instance.delete(name)

    def change_name(self, old_name, new_name):
        self.names_instance.update(old_name, new_name)


class ConsoleController:
    def __init__(self, app: NameManager):
        self.app = app

    def run(self):
        print("Lista de nombres inicial:")
        self.app.display_names()

        while True:
            print("\nOpciones:")
            print("1. Agregar nombre")
            print("2. Eliminar nombre")
            print("3. Actualizar nombre")
            print("4. Mostrar nombres")
            print("5. Salir")

            choice = input("Seleccione una opción (1-5): ")

            if choice == "1":
                name_to_add = input("Ingrese el nombre a agregar: ")
                self.app.add_name(name_to_add)
                print(f"Nombre '{name_to_add}' agregado.")
            elif choice == "2":
                name_to_remove = input("Ingrese el nombre a eliminar: ")
                self.app.remove_name(name_to_remove)
                print(f"Nombre '{name_to_remove}' eliminado.")
            elif choice == "3":
                old_name = input("Ingrese el nombre actual: ")
                new_name = input("Ingrese el nuevo nombre: ")
                self.app.change_name(old_name, new_name)
                print(f"Nombre '{old_name}' actualizado a '{new_name}'.")
            elif choice == "4":
                print("Lista de nombres:")
                self.app.display_names()
            elif choice == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    names = NamesDict()
    app = NameManager(names)

    consoleController = ConsoleController(app)
    consoleController.run()
