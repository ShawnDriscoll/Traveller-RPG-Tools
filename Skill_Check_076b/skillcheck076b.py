
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4 import uic
from PyQt4.phonon import Phonon
import time
from ui_skillcheck import Ui_MainWindow
from ui_about_dialog import Ui_aboutDialog
from diceroll import roll
import sys
import os
import numpy as np
from matplotlib import font_manager
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import skillcheck_rc

#form_class = uic.loadUiType("skillcheck.ui")[0]

class aboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        flags = Qt.Drawer | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.on_acceptOKButtonClicked)
        
    def on_acceptOKButtonClicked(self): 
        self.close()

#class MainWindow(QMainWindow, form_class):
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.rollButton.clicked.connect(self.on_roll2d6_buttonClicked)
        self.rollButton.clicked.connect(self.update_graph)
        self.actionRoll.triggered.connect(self.on_roll2d6_buttonClicked)
        self.actionRoll.triggered.connect(self.update_graph)
        self.clearButton.clicked.connect(self.on_clearall_buttonClicked)
        self.clearButton.clicked.connect(self.update_graph)
        self.actionClear.triggered.connect(self.on_clearall_buttonClicked)
        self.actionClear.triggered.connect(self.update_graph)
        self.actionPlaySample.triggered.connect(self.on_PlaySample_menu)
        self.actionUnMute.triggered.connect(self.on_unMute_menu)
        self.actionMute.triggered.connect(self.on_Mute_menu)
        self.actionVisit_Shonner.triggered.connect(self.on_Visit_Shonner)
        self.actionTech_Support.triggered.connect(self.on_Tech_Support)
        self.actionOverview.triggered.connect(self.on_Overview_menu)
        self.actionAbout_Skill_Check.triggered.connect(self.on_actionAbout_triggered)
        self.actionQuit.triggered.connect(self.quitApp)
        self.muted = True
        self.natural_roll = 0
        self.total_rolled = 0
        self.roll_effect = 0
        self.natural_roll_1 = 0
        self.natural_roll_2 = 0
        self.actionPlaySample.setDisabled(self.muted)
        self.actionMute.setDisabled(self.muted)
        self.actionUnMute.setDisabled(not self.muted)
        self.popAboutDialog=aboutDialog()

    @pyqtSlot(int)
    def on_inputskilllevel_valueChanged(self, value):
        self.totalDM.setText(str(value + self.inputcharmod.value() + self.inputDM.value() + self.diffdial.value()))
        self.die_result.setText('')
        self.die1Label.setPixmap(QPixmap(':/images/die1_0.png'))
        self.die2Label.setPixmap(QPixmap(':/images/die2_0.png'))
        self.effect_result.setText('')

    @pyqtSlot(int)
    def on_inputcharmod_valueChanged(self, value):
        self.totalDM.setText(str(value + self.inputskilllevel.value() + self.inputDM.value() + self.diffdial.value()))
        self.die_result.setText('')
        self.die1Label.setPixmap(QPixmap(':/images/die1_0.png'))
        self.die2Label.setPixmap(QPixmap(':/images/die2_0.png'))
        self.effect_result.setText('')

    @pyqtSlot(int)
    def on_inputDM_valueChanged(self, value):
        self.totalDM.setText(str(value + self.inputskilllevel.value() + self.inputcharmod.value() + self.diffdial.value()))
        self.die_result.setText('')
        self.die1Label.setPixmap(QPixmap(':/images/die1_0.png'))
        self.die2Label.setPixmap(QPixmap(':/images/die2_0.png'))
        self.effect_result.setText('')

    @pyqtSlot(int)
    def on_diffdial_valueChanged(self, value):
        self.totalDM.setText(str(value + self.inputskilllevel.value() + self.inputcharmod.value() + self.inputDM.value()))
        self.totalDiff.setText(str(value))
        self.die_result.setText('')
        self.die1Label.setPixmap(QPixmap(':/images/die1_0.png'))
        self.die2Label.setPixmap(QPixmap(':/images/die2_0.png'))
        self.effect_result.setText('')

    @pyqtSlot(int)
    def on_roll2d6_buttonClicked(self):
        self.natural_roll_1 = roll('1D6')
        self.natural_roll_2 = roll('1D6')
        self.natural_roll = self.natural_roll_1 + self.natural_roll_2
        self.total_rolled = self.natural_roll + self.inputskilllevel.value() + self.inputcharmod.value() + self.inputDM.value() + self.diffdial.value()
        self.die_result.setText(str(self.total_rolled))        
        self.die1Label.setPixmap(QPixmap(':/images/die1_' + str(self.natural_roll_1) + '.png'))
        self.die2Label.setPixmap(QPixmap(':/images/die2_' + str(self.natural_roll_2) + '.png'))
        self.roll_effect = self.total_rolled - 8
        if self.roll_effect <= -6:
            self.effect_result.setText('%d: Exceptional Failure' % self.roll_effect)
            if not self.muted:
                m_media.setCurrentSource(Phonon.MediaSource(":/sounds/exceptional_failure.wav"))
                m_media.play()
        if self.roll_effect >= -5 and self.roll_effect <= -2:
            self.effect_result.setText('%d: Average Failure' % self.roll_effect)
            if not self.muted:
                m_media.setCurrentSource(Phonon.MediaSource(":/sounds/average_failure.wav"))
                m_media.play()
        if self.roll_effect == -1:
            self.effect_result.setText('%d: Marginal Failure' % self.roll_effect)
            if not self.muted:
                m_media.setCurrentSource(Phonon.MediaSource(":/sounds/marginal_failure.wav"))
                m_media.play()
        if self.roll_effect == 0:
            self.effect_result.setText('%d: Marginal Success' % self.roll_effect)
            if not self.muted:
                m_media.setCurrentSource(Phonon.MediaSource(":/sounds/marginal_success.wav"))
                m_media.play()
        if self.roll_effect >= 1 and self.roll_effect <= 5:
            self.effect_result.setText('%d: Average Success' % self.roll_effect)
            if not self.muted:
                m_media.setCurrentSource(Phonon.MediaSource(":/sounds/average_success.wav"))
                m_media.play()
        if self.roll_effect >= 6:
            self.effect_result.setText('%d: Exceptional Success' % self.roll_effect)
            if not self.muted:
                m_media.setCurrentSource(Phonon.MediaSource(":/sounds/exceptional_success.wav"))
                m_media.play()

    @pyqtSlot(int)
    def on_clearall_buttonClicked(self):
        self.inputskilllevel.setValue(0)
        self.inputcharmod.setValue(0)
        self.inputDM.setValue(0)
        self.diffdial.setValue(0)
        self.die_result.setText('')
        self.die1Label.setPixmap(QPixmap(':/images/die1_0.png'))
        self.die2Label.setPixmap(QPixmap(':/images/die2_0.png'))
        self.effect_result.setText('')
        self.natural_roll = 0
        
    @pyqtSlot()
    def on_PlaySample_menu(self):
        m_media.setCurrentSource(Phonon.MediaSource(":/sounds/skill_check.wav"))
        m_media.play()
    
    @pyqtSlot()
    def on_unMute_menu(self):
        m_media.setCurrentSource(Phonon.MediaSource(":/sounds/activated.wav"))
        m_media.play()
        self.muted = False
        self.actionPlaySample.setDisabled(self.muted)
        self.actionMute.setDisabled(self.muted)
        self.actionUnMute.setDisabled(not self.muted)
        
    @pyqtSlot()
    def on_Mute_menu(self):
        m_media.setCurrentSource(Phonon.MediaSource(":/sounds/running_silent.wav"))
        m_media.play()
        self.muted = True
        self.actionPlaySample.setDisabled(self.muted)
        self.actionMute.setDisabled(self.muted)
        self.actionUnMute.setDisabled(not self.muted)
        
    @pyqtSlot()
    def on_Visit_Shonner(self):
        os.startfile('http://www.shonner.com')
        
    @pyqtSlot()
    def on_Tech_Support(self):
        os.startfile('mailto:shawndriscoll@hotmail.com?subject=Tech Support: Skill Check 0.7.6 (Beta) for Mongoose Traveller')
        
    @pyqtSlot()
    def on_Overview_menu(self):
        os.startfile('docs\skill_check_ref.pdf')
        
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        if not self.muted:
            m_media.setCurrentSource(Phonon.MediaSource(":/sounds/traveller_ownership.wav"))
            m_media.play()
        self.popAboutDialog.show()

    def quitApp(self):
        sys.exit(0)
        
    @pyqtSlot(int)
    def update_graph(self):
        
        percent = [2.778419, 5.5540770000000004, 8.3340270000000007, 11.111444000000001, 13.898837, 16.663181999999999, 13.891541999999999, 11.105839, 8.3293949999999999, 5.5563149999999997, 2.776923]

        if self.natural_roll != 0:
            
            die_range = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            per_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
            bar_height = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          
            count_offset = self.total_rolled - self.natural_roll
            
            for i in range(len(die_range)):
                die_range[i] = i + count_offset + 2
            
            for i in range(len(percent)):
                if i + 2 == self.natural_roll:
                    bar_height[i] = percent[i]
            
        else:
            
            die_range = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            per_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
            percent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.ax.bar(np.arange(len(die_range))-0.3, percent, width=0.6, alpha=.3, color='b')
        self.mpl.canvas.ax.set_xlim(xmin=-0.25, xmax=len(die_range)-0.75)
        self.mpl.canvas.ax.set_xticks(range(len(die_range)))
        self.mpl.canvas.ax.set_xticklabels(die_range)
        ticks_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=14, weight='normal', stretch='normal')
        for label in self.mpl.canvas.ax.get_xticklabels():
            label.set_fontproperties(ticks_font)
        title_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=16, weight='normal', stretch='normal')
        label = self.mpl.canvas.ax.set_title('2D6 Die Roll Range + DMs')
        label.set_fontproperties(title_font)
        self.mpl.canvas.ax.set_yticks(range(0,19,1))
        self.mpl.canvas.ax.set_yticklabels(per_range)
        ticks_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=6, weight='normal', stretch='normal')
        for label in self.mpl.canvas.ax.get_yticklabels():
            label.set_fontproperties(ticks_font)
        ylabel_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=14, weight='normal', stretch='normal')
        #self.mpl.canvas.ax.set_ylabel('Percentages')
        label = self.mpl.canvas.ax.set_ylabel('Percentages')
        label.set_fontproperties(ylabel_font)
        #self.mpl.canvas.ax.get_xaxis().grid(True)
        self.mpl.canvas.ax.get_yaxis().grid(True)
        
        #self.mpl.canvas.draw()
        
        if self.natural_roll !=0:        
            if self.roll_effect <= -6:
                self.mpl.canvas.ax.bar(np.arange(len(die_range))-0.3, bar_height, width=0.6, alpha=1.0, color='r')
            if self.roll_effect >= -5 and self.roll_effect <= -2:
                self.mpl.canvas.ax.bar(np.arange(len(die_range))-0.3, bar_height, width=0.6, alpha=.6, color='orange')
            if self.roll_effect == -1:
                self.mpl.canvas.ax.bar(np.arange(len(die_range))-0.3, bar_height, width=0.6, alpha=.4, color='orange')
            if self.roll_effect == 0:
                self.mpl.canvas.ax.bar(np.arange(len(die_range))-0.3, bar_height, width=0.6, alpha=.4, color='g')
            if self.roll_effect >= 1 and self.roll_effect <= 5:
                self.mpl.canvas.ax.bar(np.arange(len(die_range))-0.3, bar_height, width=0.6, alpha=.6, color='g')
            if self.roll_effect >= 6:
                self.mpl.canvas.ax.bar(np.arange(len(die_range))-0.3, bar_height, width=0.6, alpha=1.0, color='c')
                
            self.mpl.canvas.ax.set_xlim(xmin=-0.25, xmax=len(die_range)-0.75)
            self.mpl.canvas.ax.set_xticks(range(len(die_range)))
            self.mpl.canvas.ax.set_xticklabels(die_range)
            ticks_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=14, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_xticklabels():
                label.set_fontproperties(ticks_font)
            title_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=16, weight='normal', stretch='normal')
            label = self.mpl.canvas.ax.set_title('2D6 Die Roll Range + DMs')
            label.set_fontproperties(title_font)
            self.mpl.canvas.ax.set_yticks(range(0,19,1))
            self.mpl.canvas.ax.set_yticklabels(per_range)
            ticks_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=6, weight='normal', stretch='normal')
            for label in self.mpl.canvas.ax.get_yticklabels():
                label.set_fontproperties(ticks_font)
            ylabel_font = font_manager.FontProperties(family='Eras Demi ITC', style='normal', size=14, weight='normal', stretch='normal')
            #self.mpl.canvas.ax.set_ylabel('Percentages')
            label = self.mpl.canvas.ax.set_ylabel('Percentages')
            label.set_fontproperties(ylabel_font)
            #self.mpl.canvas.ax.get_xaxis().grid(True)
            self.mpl.canvas.ax.get_yaxis().grid(True)

        self.mpl.canvas.draw()


if __name__ == '__main__':
    trange = time.localtime()
    if trange[0] > 2014 or trange[1] > 4:
        print
        print "Skill Check 0.7.6 (Beta) EXPIRED."
        print
        s = raw_input('Press ENTER: ')
        print "OK"
    else:
        print
        print 'Thank you for giving Skill Check 0.7.6 (Beta) a try.'
        print
        print '-Shawn Driscoll'
        print
        
        app = QApplication(sys.argv)
        mainApp = MainWindow()
        mainApp.show()
        output = Phonon.AudioOutput(Phonon.MusicCategory)
        m_media = Phonon.MediaObject()
        Phonon.createPath(m_media, output)
        
        sys.exit(app.exec_())
