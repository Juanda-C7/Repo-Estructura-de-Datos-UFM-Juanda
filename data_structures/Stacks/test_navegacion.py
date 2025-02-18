from Navegacion_browser import Browser


browser = Browser()

# Visitar paginas

browser.visit_Page("Google")
browser.visit_Page("YouTube")
browser.visit_Page("Facebook")

# Mostrar  historial
browser.show_History()

# Ir hacia atras
browser.back_Page()
browser.show_History()

browser.back_Page()
browser.show_History()

# Ir hacia adelante
browser.advance_Page()
browser.show_History()






