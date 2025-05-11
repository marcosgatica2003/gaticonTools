#!/bin/bash -e
insultos=(
  "Sos más inestable que un bondi en hora pico sin frenos, boludo."
  "Ese código es más trucho que billete de 90 pesos."
  "Programás como un pibe que copia y pega de StackOverflow sin entender nada."
  "Tu .zshrc tiene más quilombos que Boca-River en un superclásico."
  "Ni un 'pacman -Syu' te salva de semejante desastre, che."
  "Es más probable que aparezca Messi en tu terminal antes que compile sin error."
  "Tus commits dan más vergüenza que bailar cumbia villera en un casamiento serio."
)

curiosidades=(
  "El mate infunde más paciencia que debugging de 10 mil líneas."
  "En Argentina hay más taringueros que vacas en el campo."
  "El kernel de Linux se usa en la mayoría de los cajeros automáticos del país."
  "En la UTN te dan mesa de examen antes de que tu PC termine de bootear."
  "Un asado bien hecho requiere tanta precisión como un buen makefile."
  "El colectivo 60 es más impredecible que tu scheduler con deadlocks."
  "El Lunfardo es al español lo que Bash es a los lenguajes: puro poder oscuro."
)

animos=(
  "Dale viejo, ese segfault se corrige solo si le hablás con acento porteño."
  "Hoy no se te cuelga ni el servidor de AFIP."
  "Mandale un 'git push --force' con toda la furia del Obelisco."
  "Sos más capo que el Diego en el '86, compilá y demostralo."
  "Ni la inflación te detiene: seguí codeando como un verdadero guerrero nacional."
  "Un bug en tu código es como lluvia en la Costanera: molesta, pero pasajera."
  "Si esto falla, blameá al mate, no al script."
)

hora_mensaje=(
  "Son las $(date '+%H:%M'), che, ¿no tenés algo mejor que hacer?"
  "¿Mirando la terminal a las $(date '+%H:%M')? Sos un vago con esteroides."
  "Ahora mismo son las $(date '+%H:%M'), aprovechá y andate a tomar un mate."
  "$(date '+%H:%M') y tu PC sigue esperando que aprendas a programar."
  "Son las $(date '+%H:%M'), ¿otra vez sin taxi y te quedaste pegado en la compu?"
  "$(date '+%H:%M') y todavía no te animaste a tocar /etc."
  "Las agujas del reloj marcan $(date '+%H:%M') y tu printf sigue vacío."
)

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
esac

cowsay -f tux "$mensaje"
