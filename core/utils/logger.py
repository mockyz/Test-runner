# -*- coding: utf-8 -*-
import time
import os
from utils.config import Config

class Logger():
	'''
	日志处理
	'''
	def __init__(self):
		self.prefix = Config.LOG_PATH + "/" + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
		self.prefixFul = self.prefix
		self.init = False
		self.logfile = None
		self.logpath = ""
		self.filename = ""
		self.collectionfile = None

	def __del__(self):
		if self.init:
			pass

	'''
	设置日志存储路径
	参数:
		path: 日志存储绝对路径; string类型
		
	返回值:    
		
	'''
	def setPath(self, path):
		self.prefixFul = self.prefix + "/" + path

	'''
	获取日志存储路径
	参数:
		
		
	返回值:    
		日志存储路径
	'''
	def logPath(self):
		return self.logpath

	'''
	打开日志文件
	参数:
		filepath: 日志文件路径; string类型
		title: 该条日志标题; string类型
		
	返回值:    
		
	'''
	def open(self, filepath, title = None):
		try:
			self.logpath = self.prefixFul + "/" + filepath
			logdir = self.prefixFul + "/" + os.path.dirname(filepath)
			if not os.path.exists(logdir):
				os.makedirs(logdir)

			if not self.init:
				self.init = True

			self.filename = os.path.basename(self.logpath)
			self.logfile = open(self.logpath, "w")  # 打开文件
			self.logtitle = title if title else os.path.splitext(filepath)[0]
		except Exception as e:
			print("logger open: ", e)
	#write
	'''
	打印正常日志信息, 写入文件
	参数:
		str: 正常日志内容; string类型
		
	返回值:    
		
	'''
	def print(self, str):
		try:
			strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

			strlist = str.split("\n")
			str = ""
			for line in strlist:
				str = str + strtime + ": " + line + "\n"
			
			print(str, end='')
			if self.logfile:
				self.logfile.write(str)
		except Exception as e:
			print("logger print: ", e)

	'''
	打印错误日志信息, 写入文件
	参数:
		str: 错误日志内容; string类型
		
	返回值:    
		
	'''
	def error(self, str):
		try:
			strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			str = "[ ERROR ]  " + str

			strlist = str.split("\n")
			str = ""
			for line in strlist:
				str = str + strtime + ": " + line + "\n"

			print(str, end='')
			if self.logfile:
				self.logfile.write(str)
		except Exception as e:
			print("logger error: ", e)

	'''
	打印正常日志信息, 写入文件
	参数:
		str: 正常日志内容; string类型
		
	返回值:    
		
	'''
	def info(self, str):
		try:
			strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			str = "[ INFO ]  " + str

			strlist = str.split("\n")
			str = ""
			for line in strlist:
				str = str + strtime + ": " + line + "\n"

			print(str, end='')
			if self.logfile:
				self.logfile.write(str)
		except Exception as e:
			print("logger info: ", e)

	'''
	关闭日志文件
	参数:
		result: 执行结果 pass/fail/...; string类型
		msg: 预留参数; string类型
		
	返回值:    
		
	'''
	def close(self, result = None, msg = None):
		try:
			if not result is None:
				if result == "pass":
					self.print("[ OK       ] ")
					self.append_record(self.logtitle, "pass", self.filename)
				elif result == "fail":
					self.print("[ Failed   ] ")
					self.append_record(self.logtitle, "fail", self.filename)
				else:
					self.print("[ Block    ] ")
					self.append_record(self.logtitle, "block", self.filename)
			if self.logfile:
				self.logfile.close()
				self.logfile = None
		except Exception as e:
			print("logger close: ", e)

	'''
	向csv文件中添加记录
	参数:
		name: case 名; string类型
		status: case 结果; int类型
		logpath: case 日志绝对路径; string类型
		retrytimes: case 重试次数, 预留参数; int类型
		
	返回值:    
		
	'''
	def append_record(self, name, status, logpath, retrytimes = 0):
		filename = "collection_log"
		try:
			newfile = False
			if not os.path.exists(os.path.dirname(self.logpath) + "/" + filename + ".csv"):
				newfile = True
			self.collectionfile = open(os.path.dirname(self.logpath) + "/" + filename + ".csv", "a+")  # 打开文件
			
			if newfile:
				self.collectionfile.write("NAME,STATUS,LOG PATH\n")
			self.collectionfile.write(name + "," + status + "," + logpath + "\n")
			self.collectionfile.close()
		except Exception as e:
			print("logger append_record:", e)
			#append_record(name, status, logpath, retrytimes = retrytimes + 1)

LoggerInstance = Logger()