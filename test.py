import tui

a = tui.AdvancedWindow([["Ablak1", "Ablak2"], ["Ablak3", "Ablak4"]],[40,20], [10, 11], "ROUNDED")
b = tui.Label("Szia Bobó!", 2, 2)
c = tui.Textbox(0,10,2,6,False)
tui.run([a, b, c])