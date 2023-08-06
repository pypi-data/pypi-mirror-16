import json
import os.path
from Tkinter import *
import DynamicView


class AddOptionsView:
    def __init__(self, root, base_dir, plugin_name, config_file_name):
        self.root = root
        self.base_dir = base_dir
        self.config_file_name = config_file_name
        self.file_path = os.path.join(self.base_dir, 'plugins', 'collectors', plugin_name, config_file_name)

        self.plugin_name = plugin_name

        self.top = Toplevel()
        self.top.title("Add Dropdown List")
        self.top.minsize(width=350, height=150)

        key_label = Label(self.top, text="Key Name")
        key_label.grid(sticky="W", row=0)

        value_label = Label(self.top, text="Options (Separated by Comma)")
        value_label.grid(sticky="W", row=1)

        setting_type_label = Label(self.top, text="Setting Type")
        setting_type_label.grid(sticky="W", row=2)

        self.entry_key = Entry(self.top)
        self.entry_key.insert(0, "Key Name")
        self.entry_key.grid(sticky="W", row=0, column=1)

        self.entry_value = Entry(self.top)
        self.entry_value.insert(0, "Option 1, Option 2, Option 3")
        self.entry_value.grid(sticky="W", row=1, column=1)

        self.default_setting_type = StringVar(self.top)
        self.default_setting_type.set('General')
        self.select_setting_type = OptionMenu(self.top, self.default_setting_type, 'General', 'Archiving')
        self.select_setting_type.grid(sticky="W", row=2, column=1)

        button_add = Button(self.top, text="Add", command=self.add_configuration)
        button_add.grid(sticky="W", row=3, column=1)

        button_close = Button(self.top, text="Close", command=self.top.destroy)
        button_close.grid(sticky="W", row=4, column=1)

    def add_configuration(self):
        if os.path.isfile(self.file_path):
            with open(self.file_path) as data_file:
                data = json.load(data_file)

                data[self.default_setting_type.get()][self.entry_key.get()] = {
                    "Values": self.entry_value.get().split(', '),
                    "Selected": self.entry_value.get().split(', ')[0],
                    "Field Type": "Option"
                }

                with open(self.file_path, 'w') as outfile:
                    json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))

        remove_labels_and_entries(self.root)
        DynamicView.MakeView(self.root, self.base_dir, self.plugin_name, self.config_file_name)

        self.top.destroy()


def remove_labels_and_entries(root):
    for label in root.grid_slaves():
        if int(label.grid_info()["column"]) == 1:
            label.grid_forget()
    for field in root.grid_slaves():
        if int(field.grid_info()["column"]) == 1:
            field.grid_forget()
    for label in root.grid_slaves():
        if int(label.grid_info()["column"]) == 2:
            label.grid_forget()
    for field in root.grid_slaves():
        if int(field.grid_info()["column"]) == 2:
            field.grid_forget()
