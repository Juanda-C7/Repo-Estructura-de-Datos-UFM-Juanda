from stack import Stack
from memory_profiler import profile

class Browser:
    def __init__(self):
        self.last_page = Stack(10)
        self.next_page = Stack(10)
        self.current_page = "Nueva Pestaña"

    def visit_Page(self, page: str):
        self.last_page.push(self.current_page)
        self.current_page = page
        self.next_page = Stack(10)
        print(f"Buscaste: {self.current_page}")

    def back_Page(self):
        if self.last_page.top == -1:
            print("No hay páginas anteriores")
            
        self.next_page.push(self.current_page)
        self.current_page = self.last_page.pop()
        print(f"Retrocediendo a {self.current_page}")

    def advance_Page(self):
        if self.next_page.top == -1:
            print("No hay páginas siguientes")
            
        self.last_page.push(self.current_page)
        self.current_page = self.next_page.pop()
        print(f"Avanzando a {self.current_page}")

    def show_History(self):
        print("HISTORIAL")
        print(f"La página actual es: {self.current_page}")
        print(f"Las páginas anteriores son <-: {self.last_page}")
        print(f"Las páginas siguientes son ->: {self.next_page}")

@profile
def main():
    browser = Browser()

    # Visitar páginas
    browser.visit_Page("Google")
    browser.visit_Page("YouTube")
    browser.visit_Page("Facebook")

    # Mostrar historial
    browser.show_History()

    # Ir hacia atrás
    browser.back_Page()
    browser.show_History()

    browser.back_Page()
    browser.show_History()

    # Ir hacia adelante
    browser.advance_Page()
    browser.show_History()

if __name__ == "__main__":
    main()

        

    
    
    
#if __name__ == "__main__":
    #navegador = Browser()
    #navegador.visit_Page("www.google.com")
    
    