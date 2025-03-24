from Animales import Animal
from Aves import Ave
from Reptiles import Reptil

# Crear un objeto de la clase Animal
mi_animal = Animal("Perro", "Negro", "Pupi", 4)
mi_animal.come("de todo")
mi_animal.se_mueve("caminando")
mi_animal.respira("con los pulmones")
mi_animal.reproduce("sexual")

# Crear un objeto de la clase Ave
mi_ave = Ave("Águila", "Marrón", "Águila Real", 2, "ganchudo")
mi_ave.come("carne")
mi_ave.se_mueve("volando")
mi_ave.respira("con los pulmones")
mi_ave.reproduce("ovíparo")
mi_ave.vuela(120)
mi_ave.crias(2)
mi_ave.pico()

# Crear un objeto de la clase Reptil
mi_reptil = Reptil("Serpiente", "Verde", "Cobra", 0, "lisas")
mi_reptil.come("ratones")
mi_reptil.se_mueve("reptando")
mi_reptil.respira("con los pulmones")
mi_reptil.reproduce("ovíparo")
mi_reptil.muda()
mi_reptil.escamas()