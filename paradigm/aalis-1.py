
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on November 02, 2017, at 13:47
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, visual, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, uniform, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy import parallel
parallel.setPortAddress(61432) #61432

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'eLearn-new'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\cconrad\\Desktop\\eLearn-new.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1820, 1020), fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You will be presented with an instructional video. Please wait for the video to start.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound_1 = sound.Sound('500', secs=-1)
sound_1.setVolume(0.35)
sound_2 = sound.Sound('1000', secs=-1)
sound_2.setVolume(0.35)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Recording in Progress.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "final_survey_instructions"
final_survey_instructionsClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Which of the following responses best characterizes your mental state JUST BEFORE this screen appeared?\n\na) Completely on task\nb) Mostly on task\nc) Both on task and mind wandering\nd) Mostly mind wandering\ne) Completely mind wandering',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

#rating_1 = visual.RatingScale(win=win, name='rating_1', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u''], scale='I focused my total attention on understanding the lecture content.')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [text, key_resp_2]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['y'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# -------Start Routine "trials"-------
trials = data.TrialHandler(nReps=220, method='random', #n=2448
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)
randHolder = 1 #this is a placeholder to keep track of duplicate oddballs


for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)

    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.250000)
    dingtime = uniform(0.85, 1.10) #store the dingtime every time the routine is started
    randCounter = randint(1,6) #1 in 5 chance
    key_resp_trial = event.BuilderKeyResponse()
    trialComponents = [text_2, sound_1, sound_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 1.25 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        # start/stop sound_1
        if event.getKeys(keyList=["space"]):
            print "space pushed"
            parallel.setData(5)
            core.wait(0.005)
            parallel.setData(0)
        if t >= dingtime and randHolder == 2 and sound_1.status == NOT_STARTED:
            #there was an oddball last time but it didn't get played
            sound_2.tStart = t
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
            sound_1.status = STARTED
            parallel.setData(4)
            core.wait(0.005)
            parallel.setData(0)
            randHolder = 1
        if t >= dingtime and randCounter ==1 and randHolder != 1 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
                #a 1 in 5 chance of sound 2 being played
            sound_2.tStart = t
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
            sound_1.status = STARTED
            parallel.setData(4)
            core.wait(0.005)
            parallel.setData(0)
            randHolder = 1 #lets us know there was an oddball played
        if t >= dingtime and randHolder == 1 and randCounter ==1 and sound_1.status == NOT_STARTED:
            #in case we just had an oddball
            sound_1.tStart = t
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
            parallel.setData(3)
            core.wait(0.005)
            parallel.setData(0)
            randHolder = 2 #this will force the next trial to be an oddball
        if t >= dingtime and sound_1.status == NOT_STARTED:
            #a 4 in 5 chance of sound 1 being played
            sound_1.tStart = t
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
            parallel.setData(3)
            core.wait(0.005)
            parallel.setData(0)
            randholder = 0 #no oddball
        frameRemains = dingtime + 0.1 #length of the sound
        if sound_1.status == STARTED and t >= frameRemains:
            sound_1.stop()  # stop the sound (if longer than duration)
            sound_2.stop()
        if sound_2.status == STARTED and t >= frameRemains:
            sound_2.stop()  # stop the sound (if longer than duration)
            sound_1.stop()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed the repeats of 'trials'

# ------Prepare to start Routine "final_survey_instructions"-------
t = 0
final_survey_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
final_survey_instructionsComponents = [text_3, key_resp_3]
for thisComponent in final_survey_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "final_survey_instructions"-------
while continueRoutine:
    # get current time
    t = final_survey_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)

    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['a','b','c','d','e'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_survey_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_survey_instructions"-------
for thisComponent in final_survey_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "final_survey_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
