import os
import argparse
import subprocess
import json
import sys
import ctypes
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide2.QtCore import QSettings
from lib.ui.ui_interface import Ui_MainWindow  # Assuming this is the correct import for your UI

# Icon for windows taskbar
myappid = 'danger.octotools.v1.0.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # window button functions:
        self.ui.actionClose.triggered.connect(self.closeWindow)
        self.ui.actionMaximize.triggered.connect(self.maximizeWindow)
        self.ui.actionMinimize.triggered.connect(self.minimizeWindow)

        self.show()
        self.loadLayout()

    def closeEvent(self, event):
        print('Saving Layout...')
        settings = QSettings('Danger', 'OctoTools')
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('windowState', self.saveState())
        super(mainWindow, self).closeEvent(event)

    def loadLayout(self):
        print('Loading Layout...')
        settings = QSettings('Danger', 'OctoTools')
        self.restoreGeometry(settings.value("geometry"))
        self.restoreState(settings.value("windowState"))

def main():
    parser = argparse.ArgumentParser(description="Convert EXR sequence to MP4")
    parser.add_argument('-i', '--input', help="Input EXR sequence", required=True)
    parser.add_argument('-o', '--output', help="Output MP4 file", required=True)
    parser.add_argument('-r', '--framerate', help="Output MP4 file", required=False, default=24)

    args = parser.parse_args()

    input_sequence = args.input
    output_file = args.output
    framerate = args.framerate

    if not os.path.exists(input_sequence):
        print(f"Input sequence not found: {input_sequence}")
        sys.exit(1)

    if not os.path.exists(os.path.dirname(output_file)):
        print(f"Output directory not found: {os.path.dirname(output_file)}")
        sys.exit(1)

    # Get the resolution of the first frame
    first_frame = os.path.join(input_sequence, os.listdir(input_sequence)[0])
    resolution = get_resolution(first_frame)

    # Generate the command
    command = f'ffmpeg -y -r {framerate} -f image2 -s {resolution} -i {input_sequence}\\%04d.exr -vcodec libx264 -crf 25  -pix_fmt yuv420p {output_file}'

    # Run the command
    print(f"Running command: {command}")
    subprocess.run(command, shell=True)

def get_resolution(image_path):
    result = subprocess.run(f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of json {image_path}', shell=True, stdout=subprocess.PIPE)
    data = json.loads(result.stdout)

    width = data['streams'][0]['width']
    height = data['streams'][0]['height']

    return f"{width}x{height}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    main()
    sys.exit(app.exec_())
