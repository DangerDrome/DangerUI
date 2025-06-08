# DangerUI

![image](https://github.com/user-attachments/assets/1fd98563-bbe6-4c79-9394-98cae43456f9)

# Summary

DangerUI is a modular desktop application framework built with Python and PySide2 (Qt for Python). It provides a flexible, dockable UI system designed for technical applications.

## Key Features

1. **Customizable UI Framework**:
   - Dark-themed interface with modern styling
   - Dockable panels system allowing for flexible workspace layouts
   - Custom window management (minimize, maximize, close)
   - Layout persistence between sessions
   - HiDPI support

2. **Plugin Architecture**:
   - Modular design with a plugin registry system
   - JSON-based plugin configuration
   - Inheritance-based plugin structure with BasePlugin class
   - Dynamic loading of plugin modules

3. **Media Processing Capabilities**:
   - Built-in img2mp4 functionality for converting image sequences (e.g., EXR files) to MP4 videos
   - Integration with FFmpeg for media processing

4. **Technical Features**:
   - Supports drag and drop reordering of elements
   - Can be integrated into other applications (like Houdini)
   - Windows taskbar icon integration

## Project Structure

- **Main Application**: Main window setup, UI initialization, and theming
- **UI Layer**: Extensive QT-based interface with docking widgets, toolbars, and menus
- **Plugin System**: Registry and management of plugins with dynamic loading
- **Utility Tools**: Media conversion tools (img2mp4)

## Use Cases

Based on the repository, DangerUI appears to be designed for:
1. Technical applications requiring dockable interfaces (similar to software like Houdini, Blender, etc.)
2. Media processing workflows, particularly for visual effects or animation pipelines
3. Applications requiring a plugin-based architecture for extensibility

The project provides both a standalone application and components that can be integrated into other software, making it versatile for different development scenarios.

# An exe example
The exe is avaialbe in the releases for testing
https://github.com/DangerDrome/DangerUI/releases/tag/Demo

https://github.com/user-attachments/assets/ca3dd715-2d80-455c-b09d-11e4fc2dad97

# In app Example
Houdini

![Animation](https://github.com/user-attachments/assets/17994dc4-18a0-4cb5-b15c-f12f65ca70a8)

# Drag & Drop Reordering

![Animation](https://github.com/user-attachments/assets/0eecef01-27fb-42c2-a715-e412cd2dd305)
