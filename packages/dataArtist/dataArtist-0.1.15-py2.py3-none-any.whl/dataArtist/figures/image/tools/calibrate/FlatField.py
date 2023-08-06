from imgProcessor.camera.flatField.flatFieldFromCalibration import flatFieldFromCalibration
from imgProcessor.camera.flatField.FlatFieldFromImgFit import FlatFieldFromImgFit

#OWN
from dataArtist.figures.image.ImageWidget import ImageWidget
from dataArtist.figures.image.tools.globals.CalibrationFile import CalibrationFile
from dataArtist.widgets.ImageTool import ImageTool


class FlatField(ImageTool):
    '''
    Create a flat field calibration map from multiple
    input images
    '''
    icon = 'flatField.svg'

    def __init__(self, imageDisplay):
        ImageTool.__init__(self, imageDisplay)
        
        self.outDisplay = None
        self.calFileTool = self.showGlobalTool(CalibrationFile)
        
        self._bg = None

        pa = self.setParameterMenu() 

        pMeasure = pa.addChild({
            'name':'Calculate calibration array ...',
            'type':'empty'})
        
        self.createResultInDisplayParam(pMeasure)

        self.pMethod = pMeasure.addChild({
            'name':'Method',
            'type':'list',
            'value':'from calibration images',
            'limits':['from calibration images','from normal images'],
            'tip': ''''from calibration images'
%s

'from normal images'
%s''' %(flatFieldFromCalibration.__doc__, FlatFieldFromImgFit.__doc__) })

        self.pFitMethod = pMeasure.addChild({
                    'name':'Fit method',
                    'type':'list',
                    'value':'fit vignetting function',
                    'limits':['fit vignetting function','fit polynomial'],
                    'visible':False})
        
        self.pMethod.sigValueChanged.connect(lambda p,v:
                self.pFitMethod.show(p.value()=='from normal images'))

        self.pBg = pMeasure.addChild({
                    'name':'Background image(s)',
                    'value':'-',
                    'type':'menu',
                    'tip':'''either one averaged or multiple RAW 
                    background images of the same exposure time'''})
        self.pBg.aboutToShow.connect(self._buildRefImgMenu)

        pa.addChild({
            'name':'Load calibration array ...',
            'type':'menu',
            'value':'from display'}).aboutToShow.connect(
                lambda m, fn=self._fromDisplay:
                            self.buildOtherDisplayLayersMenu(m,fn, includeThisDisplay=True))

        self.pUpdate = pa.addChild({
                    'name':'Update calibration',
                    'type':'action',
                    'visible':False})
        self.pUpdate.sigActivated.connect(self.updateCalibration)



    def _fromDisplay(self, display, n, layername):
        self.calFileTool.udpateFlatField(display.widget.image[n])


    def _buildRefImgMenu(self, menu):
        '''
        fill the menu with all available images within other displays
        '''
        menu.clear()

        def setRefImg(display):
            self._bg = display
            menu.setTitle(display.name()[:20])

        for d in self.display.workspace.displays():
            if isinstance(d.widget,ImageWidget) and d != self.display: 
                menu.addAction(d.name()).triggered.connect(
                    lambda checked, d=d: setRefImg(d))


    def updateCalibration(self):
        if self.outDisplay is None:
            raise Exception('need to create flat field map first')
        self.calFileTool.udpateFlatField(self.outDisplay.widget.image[0])
     
        
    def _fnImgAvg(self, imgs):
        ff = FlatFieldFromImgFit(imgs)
        if self.pFitMethod.value() == 'fit vignetting function':
            try: 
                out, bglevel = ff.flatFieldFromFunction()[:2]
            except RuntimeError:
                print("couldn't fit vignetting function - fit polynomial instead")
                out, bglevel = ff.flatFieldFromFit()[:2] 
        else:
            out, bglevel = ff.flatFieldFromFit()[:2]
        print 'background level = %s' %bglevel
        return out
    

    def activate(self):        
        #TODO: add standard deviation map
        img = self.getImageOrFilenames()

        if self.pMethod.value() == 'from calibration images':
            if self._bg is None:
                print 'assume images are already background corrected'
                bgimg = 0
            else:
                bgimg = self._bg.widget.image
                if img is None:
                    img = self._bg.filenames
            #try to get noise level function from current calibration
            try:
                nlf = self.calFileTool.getCurrentCoeff('noise')
            except (KeyError, IndexError):
                nlf = None

            self.startThread(lambda b=bgimg, i=img:
                            flatFieldFromCalibration(i, bgImages=b, nlf=nlf), self._done)
        else:
            self.startThread(lambda i=img:self._fnImgAvg(i), self._done)            


    def _done(self, out):
        self.outDisplay = self.handleOutput([out], title='flat field')
        self.pUpdate.show()
