# For Wayland, we should NOT set GTK_IM_MODULE and QT_IM_MODULE
# as fcitx5 will use Wayland Input Method Protocol instead
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    # On Wayland, unset these to use native Wayland input method
    unset GTK_IM_MODULE
    unset QT_IM_MODULE
    export XMODIFIERS="@im=fcitx"
    export INPUT_METHOD=fcitx
    export SDL_IM_MODULE=fcitx
    export GLFW_IM_MODULE=ibus
else
    # On X11, use the traditional method
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS="@im=fcitx"
    export INPUT_METHOD=fcitx
    export SDL_IM_MODULE=fcitx
    export GLFW_IM_MODULE=ibus
fi
