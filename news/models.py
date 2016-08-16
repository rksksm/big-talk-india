from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from datetime import datetime



BACK = (('AliceBlue', 'AliceBlue'), ('AntiqueWhite', 'AntiqueWhite'), ('Aqua', 'Aqua'), ('Aquamarine', 'Aquamarine'), ('Azure', 'Azure'), ('Beige', 'Beige'), ('Bisque', 'Bisque'), ('Black', 'Black'), 
('BlanchedAlmond', 'BlanchedAlmond'), ('Blue', 'Blue'), ('BlueViolet', 'BlueViolet'), ('Brown', 'Brown'), ('BurlyWood', 'BurlyWood'), ('CadetBlue', 'CadetBlue'), ('Chartreuse', 'Chartreuse'), 
('Chocolate', 'Chocolate'), ('Coral', 'Coral'), ('CornflowerBlue', 'CornflowerBlue'), ('Cornsilk', 'Cornsilk'), ('Crimson', 'Crimson'), ('Cyan', 'Cyan'), ('DarkBlue', 'DarkBlue'), ('DarkCyan', 'DarkCyan'), 
('DarkGoldenRod', 'DarkGoldenRod'), ('DarkGray', 'DarkGray'), ('DarkGrey', 'DarkGrey'), ('DarkGreen', 'DarkGreen'), ('DarkKhaki', 'DarkKhaki'), ('DarkMagenta', 'DarkMagenta'), ('DarkOliveGreen', 'DarkOliveGreen'), 
('DarkOrange', 'DarkOrange'), ('DarkOrchid', 'DarkOrchid'), ('DarkRed', 'DarkRed'), ('DarkSalmon', 'DarkSalmon'), ('DarkSeaGreen', 'DarkSeaGreen'), ('DarkSlateBlue', 'DarkSlateBlue'), ('DarkSlateGray', 'DarkSlateGray'), 
('DarkSlateGrey', 'DarkSlateGrey'), ('DarkTurquoise', 'DarkTurquoise'), ('DarkViolet', 'DarkViolet'), ('DeepPink', 'DeepPink'), ('DeepSkyBlue', 'DeepSkyBlue'), ('DimGray', 'DimGray'), ('DimGrey', 'DimGrey'), 
('DodgerBlue', 'DodgerBlue'), ('FireBrick', 'FireBrick'), ('FloralWhite', 'FloralWhite'), ('ForestGreen', 'ForestGreen'), ('Fuchsia', 'Fuchsia'), ('Gainsboro', 'Gainsboro'), ('GhostWhite', 'GhostWhite'), 
('Gold', 'Gold'), ('GoldenRod', 'GoldenRod'), ('Gray', 'Gray'), ('Grey', 'Grey'), ('Green', 'Green'), ('GreenYellow', 'GreenYellow'), ('HoneyDew', 'HoneyDew'), ('HotPink', 'HotPink'), ('IndianRed', 'IndianRed'), 
('Indigo ', 'Indigo '), ('Ivory', 'Ivory'), ('Khaki', 'Khaki'), ('Lavender', 'Lavender'), ('LavenderBlush', 'LavenderBlush'), ('LawnGreen', 'LawnGreen'), ('LemonChiffon', 'LemonChiffon'), 
('LightBlue', 'LightBlue'), ('LightCoral', 'LightCoral'), ('LightCyan', 'LightCyan'), ('LightGoldenRodYellow', 'LightGoldenRodYellow'), ('LightGray', 'LightGray'), ('LightGrey', 'LightGrey'), 
('LightGreen', 'LightGreen'), ('LightPink', 'LightPink'), ('LightSalmon', 'LightSalmon'), ('LightSeaGreen', 'LightSeaGreen'), ('LightSkyBlue', 'LightSkyBlue'), ('LightSlateGray', 'LightSlateGray'), 
('LightSlateGrey', 'LightSlateGrey'), ('LightSteelBlue', 'LightSteelBlue'), ('LightYellow', 'LightYellow'), ('Lime', 'Lime'), ('LimeGreen', 'LimeGreen'), ('Linen', 'Linen'), ('Magenta', 'Magenta'), 
('Maroon', 'Maroon'), ('MediumAquaMarine', 'MediumAquaMarine'), ('MediumBlue', 'MediumBlue'), ('MediumOrchid', 'MediumOrchid'), ('MediumPurple', 'MediumPurple'), ('MediumSeaGreen', 'MediumSeaGreen'), 
('MediumSlateBlue', 'MediumSlateBlue'), ('MediumSpringGreen', 'MediumSpringGreen'), ('MediumTurquoise', 'MediumTurquoise'), ('MediumVioletRed', 'MediumVioletRed'), ('MidnightBlue', 'MidnightBlue'), 
('MintCream', 'MintCream'), ('MistyRose', 'MistyRose'), ('Moccasin', 'Moccasin'), ('NavajoWhite', 'NavajoWhite'), ('Navy', 'Navy'), ('OldLace', 'OldLace'), ('Olive', 'Olive'), ('OliveDrab', 'OliveDrab'), 
('Orange', 'Orange'), ('OrangeRed', 'OrangeRed'), ('Orchid', 'Orchid'), ('PaleGoldenRod', 'PaleGoldenRod'), ('PaleGreen', 'PaleGreen'), ('PaleTurquoise', 'PaleTurquoise'), ('PaleVioletRed', 'PaleVioletRed'), 
('PapayaWhip', 'PapayaWhip'), ('PeachPuff', 'PeachPuff'), ('Peru', 'Peru'), ('Pink', 'Pink'), ('Plum', 'Plum'), ('PowderBlue', 'PowderBlue'), ('Purple', 'Purple'), ('RebeccaPurple', 'RebeccaPurple'), 
('Red', 'Red'), ('RosyBrown', 'RosyBrown'), ('RoyalBlue', 'RoyalBlue'), ('SaddleBrown', 'SaddleBrown'), ('Salmon', 'Salmon'), ('SandyBrown', 'SandyBrown'), ('SeaGreen', 'SeaGreen'), 
('SeaShell', 'SeaShell'), ('Sienna', 'Sienna'), ('Silver', 'Silver'), ('SkyBlue', 'SkyBlue'), ('SlateBlue', 'SlateBlue'), ('SlateGray', 'SlateGray'), ('SlateGrey', 'SlateGrey'), 
('Snow', 'Snow'), ('SpringGreen', 'SpringGreen'), ('SteelBlue', 'SteelBlue'), ('Tan', 'Tan'), ('Teal', 'Teal'), ('Thistle', 'Thistle'), ('Tomato', 'Tomato'), 
('Turquoise', 'Turquoise'), ('Violet', 'Violet'), ('Wheat', 'Wheat'), ('White', 'White'), ('WhiteSmoke', 'WhiteSmoke'), ('Yellow', 'Yellow'), ('YellowGreen', 'YellowGreen'))
FONT = (('AliceBlue', 'AliceBlue'), ('AntiqueWhite', 'AntiqueWhite'), ('Aqua', 'Aqua'), ('Aquamarine', 'Aquamarine'), ('Azure', 'Azure'), ('Beige', 'Beige'), ('Bisque', 'Bisque'), ('Black', 'Black'), 
('BlanchedAlmond', 'BlanchedAlmond'), ('Blue', 'Blue'), ('BlueViolet', 'BlueViolet'), ('Brown', 'Brown'), ('BurlyWood', 'BurlyWood'), ('CadetBlue', 'CadetBlue'), ('Chartreuse', 'Chartreuse'), 
('Chocolate', 'Chocolate'), ('Coral', 'Coral'), ('CornflowerBlue', 'CornflowerBlue'), ('Cornsilk', 'Cornsilk'), ('Crimson', 'Crimson'), ('Cyan', 'Cyan'), ('DarkBlue', 'DarkBlue'), ('DarkCyan', 'DarkCyan'), 
('DarkGoldenRod', 'DarkGoldenRod'), ('DarkGray', 'DarkGray'), ('DarkGrey', 'DarkGrey'), ('DarkGreen', 'DarkGreen'), ('DarkKhaki', 'DarkKhaki'), ('DarkMagenta', 'DarkMagenta'), ('DarkOliveGreen', 'DarkOliveGreen'), 
('DarkOrange', 'DarkOrange'), ('DarkOrchid', 'DarkOrchid'), ('DarkRed', 'DarkRed'), ('DarkSalmon', 'DarkSalmon'), ('DarkSeaGreen', 'DarkSeaGreen'), ('DarkSlateBlue', 'DarkSlateBlue'), ('DarkSlateGray', 'DarkSlateGray'), 
('DarkSlateGrey', 'DarkSlateGrey'), ('DarkTurquoise', 'DarkTurquoise'), ('DarkViolet', 'DarkViolet'), ('DeepPink', 'DeepPink'), ('DeepSkyBlue', 'DeepSkyBlue'), ('DimGray', 'DimGray'), ('DimGrey', 'DimGrey'), 
('DodgerBlue', 'DodgerBlue'), ('FireBrick', 'FireBrick'), ('FloralWhite', 'FloralWhite'), ('ForestGreen', 'ForestGreen'), ('Fuchsia', 'Fuchsia'), ('Gainsboro', 'Gainsboro'), ('GhostWhite', 'GhostWhite'), 
('Gold', 'Gold'), ('GoldenRod', 'GoldenRod'), ('Gray', 'Gray'), ('Grey', 'Grey'), ('Green', 'Green'), ('GreenYellow', 'GreenYellow'), ('HoneyDew', 'HoneyDew'), ('HotPink', 'HotPink'), ('IndianRed', 'IndianRed'), 
('Indigo ', 'Indigo '), ('Ivory', 'Ivory'), ('Khaki', 'Khaki'), ('Lavender', 'Lavender'), ('LavenderBlush', 'LavenderBlush'), ('LawnGreen', 'LawnGreen'), ('LemonChiffon', 'LemonChiffon'), 
('LightBlue', 'LightBlue'), ('LightCoral', 'LightCoral'), ('LightCyan', 'LightCyan'), ('LightGoldenRodYellow', 'LightGoldenRodYellow'), ('LightGray', 'LightGray'), ('LightGrey', 'LightGrey'), 
('LightGreen', 'LightGreen'), ('LightPink', 'LightPink'), ('LightSalmon', 'LightSalmon'), ('LightSeaGreen', 'LightSeaGreen'), ('LightSkyBlue', 'LightSkyBlue'), ('LightSlateGray', 'LightSlateGray'), 
('LightSlateGrey', 'LightSlateGrey'), ('LightSteelBlue', 'LightSteelBlue'), ('LightYellow', 'LightYellow'), ('Lime', 'Lime'), ('LimeGreen', 'LimeGreen'), ('Linen', 'Linen'), ('Magenta', 'Magenta'), 
('Maroon', 'Maroon'), ('MediumAquaMarine', 'MediumAquaMarine'), ('MediumBlue', 'MediumBlue'), ('MediumOrchid', 'MediumOrchid'), ('MediumPurple', 'MediumPurple'), ('MediumSeaGreen', 'MediumSeaGreen'), 
('MediumSlateBlue', 'MediumSlateBlue'), ('MediumSpringGreen', 'MediumSpringGreen'), ('MediumTurquoise', 'MediumTurquoise'), ('MediumVioletRed', 'MediumVioletRed'), ('MidnightBlue', 'MidnightBlue'), 
('MintCream', 'MintCream'), ('MistyRose', 'MistyRose'), ('Moccasin', 'Moccasin'), ('NavajoWhite', 'NavajoWhite'), ('Navy', 'Navy'), ('OldLace', 'OldLace'), ('Olive', 'Olive'), ('OliveDrab', 'OliveDrab'), 
('Orange', 'Orange'), ('OrangeRed', 'OrangeRed'), ('Orchid', 'Orchid'), ('PaleGoldenRod', 'PaleGoldenRod'), ('PaleGreen', 'PaleGreen'), ('PaleTurquoise', 'PaleTurquoise'), ('PaleVioletRed', 'PaleVioletRed'), 
('PapayaWhip', 'PapayaWhip'), ('PeachPuff', 'PeachPuff'), ('Peru', 'Peru'), ('Pink', 'Pink'), ('Plum', 'Plum'), ('PowderBlue', 'PowderBlue'), ('Purple', 'Purple'), ('RebeccaPurple', 'RebeccaPurple'), 
('Red', 'Red'), ('RosyBrown', 'RosyBrown'), ('RoyalBlue', 'RoyalBlue'), ('SaddleBrown', 'SaddleBrown'), ('Salmon', 'Salmon'), ('SandyBrown', 'SandyBrown'), ('SeaGreen', 'SeaGreen'), 
('SeaShell', 'SeaShell'), ('Sienna', 'Sienna'), ('Silver', 'Silver'), ('SkyBlue', 'SkyBlue'), ('SlateBlue', 'SlateBlue'), ('SlateGray', 'SlateGray'), ('SlateGrey', 'SlateGrey'), 
('Snow', 'Snow'), ('SpringGreen', 'SpringGreen'), ('SteelBlue', 'SteelBlue'), ('Tan', 'Tan'), ('Teal', 'Teal'), ('Thistle', 'Thistle'), ('Tomato', 'Tomato'), 
('Turquoise', 'Turquoise'), ('Violet', 'Violet'), ('Wheat', 'Wheat'), ('White', 'White'), ('WhiteSmoke', 'WhiteSmoke'), ('Yellow', 'Yellow'), ('YellowGreen', 'YellowGreen'))
TOP = (('Normal', 'Normal'), ('Top - 1', 'Top - 1'), ('Top - 2', 'Top - 2'), ('Top - 3', 'Top - 3'), ('Top - 4', 'Top - 4'), ('Top - 5', 'Top - 5'), ('Top - 6', 'Top - 6'))

WOW = (('Wow - 1', 'Wow - 1'), ('Wow - 2', 'Wow - 2'), ('Wow - 3', 'Wow - 3'), ('Wow - 4', 'Wow - 4'), ('Wow - 5', 'Wow - 5'))
STATUS = (('Active', 'Active'), ('Deactive', 'Deactive'))
# Create your models here.
class Section(models.Model):
	title = models.CharField(max_length=200)
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)
	
	def __unicode__(self):
		return self.title
class Slide(models.Model):
	text = models.TextField()
	image = models.ImageField(upload_to = "slide/")
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)
	

class Card(models.Model):
	section = models.ForeignKey(Section)
	top = models.CharField(max_length=50, choices=TOP)
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	intro_text = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(upload_to = "card/")
	background_color = models.CharField(max_length=50, choices=BACK)
	font_color = models.CharField(max_length=50, choices=FONT)
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)

class Breaking(models.Model):
	text = models.CharField(max_length=100)
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)


class BasicConfiguration(models.Model):
	theme_name = models.CharField(max_length=200)
	header_background = models.CharField(max_length=50, choices=BACK)
	header_text = models.CharField(max_length=50, choices=FONT)
	facebook = models.CharField(max_length=200)
	linkedin = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	google_plus = models.CharField(max_length=200)
	youtube = models.CharField(max_length=200)
	breaking_background = models.CharField(max_length=50, choices=BACK)
	breaking_font = models.CharField(max_length=50, choices=BACK)
	website_background = models.CharField(max_length=50, choices=BACK)
	website_heading = models.CharField(max_length=50, choices=BACK)
	search_heading = models.CharField(max_length=50, choices=BACK)
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)


class SmallSection(models.Model):
	title = models.CharField(max_length=200)
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)


class SmallCard(models.Model):
	section = models.ForeignKey(SmallSection)
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	intro_text = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(upload_to = "small card/")
	background_color = models.CharField(max_length=50, choices=BACK)
	font_color = models.CharField(max_length=50, choices=FONT)
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)
class Advertisement(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to = "advertisement/")
	publish = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=20, choices=STATUS)