class Noticia:
    def __init__(self, titulo, categoria, texto, palavrasChave1, palavrasChave2, palavrasChave3):
        self.titulo = titulo 
        self.categoria = categoria
        self.texto = texto
        self.palavrasChave = [palavrasChave1, palavrasChave2, palavrasChave3]
    
    def __str__(self):
        print(self.titulo)
        print(self.categoria)
        print(self.texto)
        print(self.palavrasChave[0])
        print(self.palavrasChave[1])
        print(self.palavrasChave[2])
    