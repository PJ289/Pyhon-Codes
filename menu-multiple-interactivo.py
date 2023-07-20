import curses

# Opciones del menú
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "", "Aceptar"]

def main(stdscr):
    # Configurar la pantalla
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Variables para el manejo de la selección
    seleccionados = []
    seleccion_actual = 0
    cerrar_ventana = False

    # Ciclo principal del menú
    while True:
        stdscr.clear()

        # Imprimir las opciones del menú
        for i, opcion in enumerate(opciones):
            if i in seleccionados and i == seleccion_actual:
                stdscr.addstr(i, 0, f"(X) {opcion}")
            elif i in seleccionados:
                stdscr.addstr(i, 0, f"[X] {opcion}")
            elif i == seleccion_actual:
                stdscr.addstr(i, 0, f"[*] {opcion}")
            else:
                stdscr.addstr(i, 0, f"   {opcion}")

        # Obtener la entrada del usuario
        key = stdscr.getch()

        # Manejar la entrada del usuario
        if key == ord('q') or key == ord('Q'):
            # Salir del menú
            break
        elif key == curses.KEY_DOWN:
            # Mover hacia abajo en el menú
            seleccion_actual = (seleccion_actual + 1) % len(opciones)
        elif key == curses.KEY_UP:
            # Mover hacia arriba en el menú
            seleccion_actual = (seleccion_actual - 1) % len(opciones)
        elif key == ord(' '):
            # Marcar o desmarcar la casilla actual con una X
            if seleccion_actual in seleccionados:
                seleccionados.remove(seleccion_actual)
            else:
                seleccionados.append(seleccion_actual)
        elif key == ord('\n'):
            # Realizar acción en base a la selección
            if seleccion_actual == len(opciones) - 1:
                # Marcar para cerrar la ventana después de mostrar los resultados
                cerrar_ventana = True
                break

        # Refrescar la pantalla
        stdscr.refresh()

    # Cerrar la ventana si se ha marcado para cerrar
    if cerrar_ventana:
        curses.endwin()

    # Ejecutar acciones con las casillas seleccionadas
    for seleccionado in seleccionados:
        if seleccionado == 0:
            # Acción para la opción 1
            print("Has seleccionado la opción 1")
            # Realizar acciones adicionales para la opción 1

        elif seleccionado == 1:
            # Acción para la opción 2
            print("Has seleccionado la opción 2")
            # Realizar acciones adicionales para la opción 2

        elif seleccionado == 2:
            # Acción para la opción 3
            print("Has seleccionado la opción 3")
            # Realizar acciones adicionales para la opción 3

        elif seleccionado == 3:
            # Acción para la opción 4
            print("Has seleccionado la opción 4")
            # Realizar acciones adicionales para la opción 4

    # Esperar a que el usuario presione una tecla antes de salir
    if cerrar_ventana:
        input("Presiona Enter para salir...")

# Iniciar la aplicación curses
curses.wrapper(main)
