# import the necessary packages
from threading import Thread
import cv2

class WebcamVideoStream:
	def __init__(self, src=0, resolution=(320, 240), name="WebcamVideoStream"):
		# initialize the video camera stream
		if isinstance(src, int):
			self.stream = cv2.VideoCapture(src)
			self.stream.set(3, int(resolution[0]))  # cv2.CAP_PROP_FRAME_WIDTH
			self.stream.set(4, int(resolution[1]))  # cv2.CAP_PROP_FRAME_HEIGHT
		else:
			self.stream = src

		# read the first frame from the stream
		(self.grabbed, self.frame) = self.stream.read()

		# initialize the thread name
		self.name = name

		# initialize the variable used to indicate if the thread should
		# be stopped
		self.stopped = False

	def start(self):
		# start the thread to read frames from the video stream
		t = Thread(target=self.update, name=self.name, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		# keep looping infinitely until the thread is stopped
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				return

			# otherwise, read the next frame from the stream
			(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		# return the frame most recently read
		return self.frame

	def stop(self):
		self.stream.release()
		# indicate that the thread should be stopped
		self.stopped = True
