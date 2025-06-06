import sys
import os

# Fix relative imports bs (get path of script and add to sys.path)
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

import json

class PluginRegistry:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_class):
        if name not in self.plugins:
            self.plugins[name] = plugin_class
        else:
            raise ValueError(f"Plugin with name '{name}' is already registered.")

    def unregister_plugin(self, name):
        if name in self.plugins:
            del self.plugins[name]
        else:
            print(f"Plugin with name '{name}' is not registered.")

    def get_plugin(self, name):
        return self.plugins.get(name, None)

    def list_plugins(self):
        return list(self.plugins.keys())

    def register_plugins_from_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)

        for plugin_data in data.get('plugins', []):
            name = plugin_data.get('name')
            module_path = plugin_data.get('module')
            class_name = plugin_data.get('class')

            try:
                module = __import__(module_path, fromlist=[class_name])
                plugin_class = getattr(module, class_name)
                self.register_plugin(name, plugin_class)
            except (ImportError, AttributeError) as e:
                print(f"Error registering plugin '{name}': {e}")


class BasePlugin:
    def perform_action(self):
        raise NotImplementedError("Subclasses must implement this method.")





# Usage example
if __name__ == "__main__":
    registry = PluginRegistry()

    # Register plugins from a JSON file
    json_file_path = path+'\\'+'plugins.json'
    registry.register_plugins_from_json(json_file_path)

    # Get and use a plugin
    plugin_name = "example"
    plugin_instance = registry.get_plugin(plugin_name)

    if plugin_instance:
        plugin_instance.perform_action()
    else:
        print(f"No plugin found with the name '{plugin_name}'.")

    # List all registered plugins
    print("Registered plugins:", registry.list_plugins())

    # Unregister a plugin
    unregister_plugin_name = "example"
    registry.unregister_plugin(unregister_plugin_name)

    # List all registered plugins after unregistering
    print("Registered plugins after unregistering:", registry.list_plugins())
