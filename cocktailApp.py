#!/usr/bin/python3
import cocktail
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="MOTHERFUCKING COCKTAILS")
        self.set_size_request(1000,400)
        self.set_border_width(20)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
        self.add(vbox)
        self.entry = Gtk.Entry()
        self.entry.set_text("Enter the cocktail you want to look up here")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing = 6)
        vbox.pack_start(hbox, True, True, 0)
        button = Gtk.Button.new_with_label("Find Recipe")
        button.connect("clicked", self.on_click)
        hbox.pack_start(button, True, True, 0)
        self.labelOne = Gtk.Label()
        hbox.pack_start(self.labelOne, True, True, 0)
        self.labelTwo =  Gtk.Label()
        hbox.pack_start(self.labelTwo, True, True, 0)

    def on_click(self, button):
        thing = cocktail.getCocktail(self.entry.get_text())
        self.labelOne.set_text(thing[0])
        self.labelTwo.set_text(thing[1])


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

