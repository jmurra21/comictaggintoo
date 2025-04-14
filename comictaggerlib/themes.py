"""Theme management for ComicTagger"""

# Copyright 2012-2014 ComicTagger Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

# Dark theme stylesheet
DARK_THEME = """
/* Global styles */
QWidget {
    background-color: #2D2D30;
    color: #F0F0F0;
}

/* Menu and toolbar styles */
QMenuBar, QToolBar {
    background-color: #1E1E1E;
    border-bottom: 1px solid #3F3F46;
}

QMenuBar::item:selected, QMenu::item:selected {
    background-color: #3F3F46;
}

QMenu {
    background-color: #2D2D30;
    border: 1px solid #3F3F46;
}

QMenu::item {
    padding: 5px 20px 5px 20px;
}

/* Dropdown styles - important for readability */
QComboBox {
    background-color: #383838;
    color: #F0F0F0;
    border: 1px solid #555555;
    padding: 2px 18px 2px 5px;
    min-height: 20px;
}

QComboBox:focus, QComboBox:on {
    border: 1px solid #007ACC;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left: 1px solid #555555;
}

QComboBox QAbstractItemView {
    background-color: #2D2D30;
    color: #F0F0F0;
    selection-background-color: #3F3F46;
    selection-color: #FFFFFF;
    border: 1px solid #555555;
}

/* Critical: Ensure selected text in dropdowns is always visible in dark mode */
QComboBox QAbstractItemView::item:selected {
    background-color: #264F78;
    color: #FFFFFF;
    border: none;
}

/* Table styles */
QTableView {
    background-color: #252526;
    alternate-background-color: #2D2D30;
    color: #F0F0F0;
    gridline-color: #3F3F46;
}

QTableView::item:selected {
    background-color: #264F78;
    color: #FFFFFF;
}

QHeaderView::section {
    background-color: #1E1E1E;
    color: #F0F0F0;
    padding: 4px;
    border: 1px solid #3F3F46;
}

/* Tabs */
QTabWidget::pane {
    border: 1px solid #3F3F46;
}

QTabBar::tab {
    background-color: #2D2D30;
    border: 1px solid #3F3F46;
    padding: 5px 10px;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background-color: #1E1E1E;
    border-bottom-color: #1E1E1E;
}

/* Buttons */
QPushButton {
    background-color: #383838;
    border: 1px solid #555555;
    color: #F0F0F0;
    padding: 5px 15px;
    border-radius: 2px;
}

QPushButton:hover {
    background-color: #404040;
}

QPushButton:pressed {
    background-color: #505050;
}

QPushButton:disabled {
    background-color: #2D2D30;
    color: #656565;
    border: 1px solid #3F3F46;
}

/* Scrollbars */
QScrollBar:vertical {
    background-color: #2D2D30;
    width: 12px;
    margin: 12px 0px 12px 0px;
    border: none;
}

QScrollBar:horizontal {
    background-color: #2D2D30;
    height: 12px;
    margin: 0px 12px 0px 12px;
    border: none;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #3F3F46;
    border-radius: 3px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background-color: #555555;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    border: none;
}

QScrollBar::add-page, QScrollBar::sub-page {
    background: none;
}

/* Text edits and line edits */
QTextEdit, QLineEdit, QPlainTextEdit {
    background-color: #252526;
    color: #F0F0F0;
    border: 1px solid #3F3F46;
    padding: 2px;
    selection-background-color: #264F78;
    selection-color: #FFFFFF;
}

QTextEdit:focus, QLineEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #007ACC;
}

/* Special Case - Splitter */
QSplitter::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3F3F46, stop:1 #505050);
    border: 1px solid #555555;
    width: 13px;
    margin-top: 2px;
    margin-bottom: 2px;
    border-radius: 4px;
}

/* Group Box */
QGroupBox {
    border: 1px solid #3F3F46;
    border-radius: 4px;
    margin-top: 8px;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 10px;
    padding: 0 3px;
}

/* Checkbox and Radio Button */
QCheckBox, QRadioButton {
    spacing: 5px;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 13px;
    height: 13px;
}

QCheckBox::indicator:unchecked, QRadioButton::indicator:unchecked {
    border: 1px solid #555555;
    background-color: #2D2D30;
}

QCheckBox::indicator:checked, QRadioButton::indicator:checked {
    border: 1px solid #007ACC;
    background-color: #007ACC;
}

/* Status Bar */
QStatusBar {
    background-color: #1E1E1E;
    color: #F0F0F0;
    border-top: 1px solid #3F3F46;
}

/* Tooltips */
QToolTip {
    background-color: #2D2D30;
    color: #F0F0F0;
    border: 1px solid #3F3F46;
}

/* List Views */
QListView {
    background-color: #252526;
    alternate-background-color: #2D2D30;
    color: #F0F0F0;
}

QListView::item:selected {
    background-color: #264F78;
    color: #FFFFFF;
}

/* Progress Bar */
QProgressBar {
    border: 1px solid #3F3F46;
    background-color: #252526;
    text-align: center;
    color: #F0F0F0;
}

QProgressBar::chunk {
    background-color: #007ACC;
}

/* Spin boxes */
QSpinBox, QDoubleSpinBox {
    background-color: #252526;
    color: #F0F0F0;
    border: 1px solid #3F3F46;
    padding: 2px;
}

QSpinBox::up-button, QDoubleSpinBox::up-button,
QSpinBox::down-button, QDoubleSpinBox::down-button {
    border: 1px solid #3F3F46;
    background-color: #383838;
    width: 16px;
    border-width: 1px;
}

QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,
QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {
    background-color: #404040;
}

QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed,
QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed {
    background-color: #505050;
}

/* Sliders */
QSlider::groove:horizontal {
    border: 1px solid #3F3F46;
    height: 4px;
    background: #252526;
}

QSlider::handle:horizontal {
    background: #007ACC;
    border: 1px solid #007ACC;
    width: 12px;
    margin: -4px 0;
    border-radius: 6px;
}

QSlider::add-page:horizontal {
    background: #252526;
}

QSlider::sub-page:horizontal {
    background: #007ACC;
}
"""

# Light theme stylesheet - ensures text doesn't change color when selected
LIGHT_THEME = """
/* Critical style to ensure text doesn't change color when selected in light mode */
QComboBox QAbstractItemView::item:selected {
    background-color: palette(highlight);
    color: palette(text);  /* Keep the same text color when selected */
}

QListView::item:selected, QTableView::item:selected {
    background-color: palette(highlight);
    color: palette(text);  /* Keep the same text color when selected */
}

/* Maintain selection visibility with just a background change */
QComboBox:focus, QComboBox:on {
    border: 1px solid palette(highlight);
}

/* Splitter styling for light mode */
QSplitter::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);
    border: 1px solid #777;
    width: 13px;
    margin-top: 2px;
    margin-bottom: 2px;
    border-radius: 4px;
}
"""

def apply_theme(app, is_dark_mode=True):
    """Apply the selected theme to the application
    
    Args:
        app: The QApplication instance
        is_dark_mode: Whether to apply dark mode (True) or light mode (False)
    """
    logger.info("Applying %s theme", "dark" if is_dark_mode else "light")
    
    if is_dark_mode:
        app.setStyleSheet(DARK_THEME)
    else:
        app.setStyleSheet(LIGHT_THEME)
    
    return True
