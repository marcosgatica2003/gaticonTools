#!/bin/bash -e
insultos=(
  "Sos más inestable que un bondi en hora pico sin frenos, boludo."
  "Ese código es más trucho que billete de 90 pesos."
  "Programás como un pibe que copia y pega de StackOverflow sin entender nada."
  "Tu .zshrc tiene más quilombos que Boca-River en un superclásico."
  "Ni un 'pacman -Syu' te salva de semejante desastre che."
  "Momo sabes de todo."
  "En un universo paralelo, la Nadia saldría contigo."
  "Gaga"
  "Es más probable que aparezca Messi en tu terminal antes que compile sin error."
  "Tus commits dan más vergüenza que bailar cumbia villera en un casamiento serio."
  "Tomaste la creatina? Seguramente no por boludo."
  "Tus parches son más sucios que los cables de Once."
  "Ese makefile tiene más dependencias rotas que cualquier Coniferal."
  "Tu código es más misterioso que el plan de estudios de la UTN."
)

curiosidades=(
  "El mate infunde más paciencia que debugging de 10 mil líneas."
  "En Argentina hay más taringueros que vacas en el campo."
  "El kernel de Linux se usa en la mayoría de los cajeros automáticos del país."
  "En la UTN te dan mesa de examen antes de que tu PC termine de bootear."
  "En la UTN hay paro antes de que tu miniBestia termine de bootear."
  "Un asado bien hecho requiere tanta precisión como un buen makefile."
  "El 60 es más impredecible que tu scheduler con deadlocks."
  "El Lunfardo es al español lo que Bash es a los lenguajes: puro poder oscuro."
  "El Chamuyo es el framework más usado en Latinoamérica."
  "En Argentina hay más distribuciones de Linux por persona que planes de estudio completos."
)

animos=(
  "Dale viejo, ese segfault se corrige solo si le hablás con acento porteño."
  "Hoy no se te cuelga ni el servidor de AFIP."
  "Mandale un 'git push --force' con toda la furia del Obelisco."
  "Sos más capo que el Diego en el '86, compilá y demostralo."
  "Ni la inflación te detiene: seguí codeando como un verdadero guerrero nacional."
  "Un bug en tu código es como lluvia en la Costanera: molesta, pero pasajera."
  "Si esto falla, blameá al mate, no al script."
  "Compilá con fe, que hasta el Diego jugó lesionado."
  "Hoy sos más estable que systemd corriendo en Gentoo (y eso es mucho decir)."
)

hora_mensaje=(
  "Son las $(date '+%H:%M'), che, ¿no tenés algo mejor que hacer?"
  "¿Mirando la terminal a las $(date '+%H:%M')? Sos un vago con esteroides."
  "Ahora mismo son las $(date '+%H:%M'), aprovechá y andate a tomar un mate."
  "$(date '+%H:%M') y tu PC sigue esperando que aprendas a programar."
  "Son las $(date '+%H:%M'), ¿otra vez sin taxi y te quedaste pegado en la compu?"
  "$(date '+%H:%M') y todavía no te animaste a tocar /etc."
  "Las agujas del reloj marcan $(date '+%H:%M') y tu printf sigue vacío."
  "$(date '+%H:%M')… ni el cron labura a esta hora, ¿qué hacés acá?"
  "$(date '+%H:%M'), seguís conectado… tu PC ya pidió paro docente."
)

# acciones=(
#     "Sos tan vago que ya te hice un ls::ls"
# )

tipo=$(( RANDOM % 4 ))

case $tipo in
    0)
        mensaje="${insultos[RANDOM % ${#insultos[@]}]}"
        ;;
    1)
        mensaje="${hora_mensaje[RANDOM % ${#hora_mensaje[@]}]}"

        ;;
    2)
        mensaje="${curiosidades[RANDOM % ${#curiosidades[@]}]}"
        ;;
    3)
        mensaje="${animos[RANDOM % ${#animos[@]}]}"
        ;;
    # 4)
    #     acciones="${acciones[RANDOM % ${#acciones[@]}]}"
        # ;;
esac

cowsay -f tux "$mensaje"
