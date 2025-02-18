#!/bin/bash

cambiarTema() {
	local currectConfig="$1"
	local backupConfig="$2"

	if [[ -f "$currectConfig" && -f "$backupConfig" ]]; then
		mv "$currectConfig" "$currectConfig.tmp"
		mv "$backupConfig" "$currectConfig"
		mv "$currectConfig.tmp" "$backupConfig"

		echo "Tema cambiado loco."
	else
		echo "No funciona loco aguante Ventanas 10."
		exit 1
	fi
}

cambiarTema "$HOME/.config/alacritty/alacritty.toml" "$HOME/.config/alacritty/alacritty.toml.bak"

cambiarTema "$HOME/.tmux.conf" "$HOME/.tmux.conf.bak" && 
tmux source-file "$HOME/.tmux.conf"

cambiarTema "$HOME/.config/gtk-3.0/settings.ini" "$HOME/.config/gtk-3.0/settings.ini.bak"

cambiarTema "$HOME/.config/polybar/config.ini" "$HOME/.config/polybar/config.ini.bak"
polybar-msg cmd restart

cambiarTema "$HOME/.vimrc" "$HOME/.vimrc.bak"

cambiarTema "$HOME/Scripts/configuracionesRofi/temaEjecutables.rasi" "$HOME/Scripts/configuracionesRofi/temaEjecutables.rasi.bak"

cambiarTema "$HOME/Scripts/configuracionesRofi/temaTemperaturas.rasi" "$HOME/Scripts/configuracionesRofi/temaTemperaturas.rasi.bak"
