from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Deseamos conocer cuál es el género musical favorito dentro de la comunidad de Ingeniería de Sistemas de la
# Universidad Mariana. Con el fin de lograrlo, se llevó a cabo una encuesta que permitió recopilar las preferencias
# musicales de estudiantes, profesores y personal administrativo. Los resultados arrojaron la siguiente información
# sobre los géneros musicales más apreciados:

administrativos = {"Rock", "Jazz", "Pop", "Metal", "Cumbia", "Salsa", "Vallenato", "Merengue", "Bachata", "R&B",
                   "Blues"}
profesores = {"Rock", "Jazz", "Pop", "Metal", "Cumbia", "Salsa", "Phonk", "Reggae", "Hip-Hop", "Electrónica"}
estudiantes = {"Rock", "Metal", "Salsa", "Phonk", "Reggaeton", "Jazz", "Pop", "Vallenato", "Salsa", "Trap",
               "EDM", "K-Pop", "Rap"}

# Respuestas
# 1.
administrativos_y_profesores = administrativos.intersection(profesores)
print("¿Cuáles son los géneros musicales que son comunes entre administrativos y profesores?",
      administrativos_y_profesores)

print("¿Cuántos géneros musicales diferentes aprecian los administrativos?", len(administrativos))

generos_populares = administrativos_y_profesores.intersection(estudiantes)
print("¿Hay algún género musical que sea apreciado por todos los grupos (administrativos, profesores y estudiantes)?",
      generos_populares)

generos_impopulares = (administrativos.symmetric_difference(profesores)
                       .symmetric_difference(estudiantes)).difference(generos_populares)
print("¿Cuáles son los géneros musicales menos comunes entre los grupos?", generos_impopulares)

solo_administrativos = administrativos.difference(profesores, estudiantes)
print("¿Cuántos géneros musicales son exclusivos de los administrativos?", len(solo_administrativos))

solo_estudiantes_y_profesores = estudiantes.intersection(profesores).difference(generos_populares)
print("¿Cuáles son los géneros musicales que son comunes entre profesores y estudiantes, pero no entre administrativos?"
      , solo_estudiantes_y_profesores)

print("¿Cuántos géneros musicales diferentes en total aprecian los profesores?", len(profesores))

estudiantes_not_profesores = estudiantes.difference(generos_populares, profesores)
print("¿Cuáles géneros musicales están en el conjunto de estudiantes pero no en el conjunto de profesores?",
      estudiantes_not_profesores)

print("¿Cuántos géneros musicales en total aprecian los estudiantes?", len(estudiantes))

administrativos_not_estudiantes = administrativos.difference(generos_populares, estudiantes)
print("¿Cuáles son los géneros musicales que están en el conjunto de administrativos pero no en el conjunto de "
      "estudiantes?", administrativos_not_estudiantes)

profesores_not_estudiantes = profesores.difference(generos_populares, estudiantes)
print("¿Cuáles son los géneros musicales que están en el conjunto de profesores pero no en el conjunto de estudiantes?",
      profesores_not_estudiantes)

print("¿Cuántos géneros musicales diferentes aprecian los administrativos y los profesores juntos?",
      len(administrativos.union(profesores)))

profesores_not_administrativos = profesores.difference(generos_populares, administrativos)
print("¿Cuáles son los géneros musicales que están en el conjunto de profesores pero no en el conjunto de "
      "administrativos?", profesores_not_administrativos)

solo_estudiantes = estudiantes.difference(profesores, administrativos)
print("¿Cuáles son los géneros musicales que están en el conjunto de estudiantes pero no en el conjunto de "
      "administrativos ni en el conjunto de profesores?", solo_estudiantes)

print("¿Cuáles géneros musicales están en el conjunto de administrativos pero no en el conjunto de profesores ni "
      "en el conjunto de estudiantes?", solo_administrativos)

print("¿Cuántos géneros musicales diferentes aprecian los estudiantes y los administrativos juntos?",
      len(estudiantes.union(profesores)))

comun_estudiantes_y_profesores_not_estudiantes_y_administrativos = (estudiantes.intersection(profesores).difference(
    estudiantes.intersection(administrativos)))
print("¿Cuántos géneros musicales son comunes entre estudiantes y profesores, pero no entre estudiantes y "
      "administrativos?", len(comun_estudiantes_y_profesores_not_estudiantes_y_administrativos))

# Diagrame su respuesta

venn3([administrativos, profesores, estudiantes],
      set_labels=('Administrativos', 'profesores', 'estudiantes'), alpha=0.7)
plt.title("Género musical favorito para Programa de Ingeniería de Sistemas - Universidad Mariana")
plt.gcf().set_size_inches(10, 10)
plt.show()

venn_diagram = venn3([administrativos, profesores, estudiantes],
                     set_colors=("#004469", "#5cd278", "#d9b783"),
                     set_labels=('Administrativos', 'Profesores', 'Estudiantes'), alpha=0.8)

# Agregar etiquetas a las áreas de intersección
venn_diagram.get_label_by_id('100').set_text('\n'.join(administrativos - (profesores | estudiantes)))
venn_diagram.get_label_by_id('010').set_text('\n'.join(profesores - (administrativos | estudiantes)))
venn_diagram.get_label_by_id('110').set_text('\n'.join((administrativos & profesores) - estudiantes))
venn_diagram.get_label_by_id('001').set_text('\n'.join(estudiantes - (administrativos | profesores)))
venn_diagram.get_label_by_id('101').set_text('\n'.join((administrativos & estudiantes) - profesores))
venn_diagram.get_label_by_id('011').set_text('\n'.join((profesores & estudiantes) - administrativos))
venn_diagram.get_label_by_id('111').set_text('\n'.join(administrativos & profesores & estudiantes))

plt.title("Género musical favorito para Programa de Ingeniería de Sistemas - Universidad Mariana")
plt.gcf().set_size_inches(10, 10)
plt.show()
