# Example plugin
class BasePlugin:
    def perform_action(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
class ExamplePlugin(BasePlugin):
    def perform_action(self):
        print("Example plugin is performing an action!")