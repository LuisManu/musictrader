# Author Luis Manuel Gutierrez http://luismanu.com
from django.db import models

from ..artists.models import Artist
from ..profiles.models import Profile

class Album(models.Model):

	new = 'new'
	great = 'great'
	okay = 'okay'
	fair = 'fair'
	working = 'working'

	condition_choices = (
		(new, 'new'),
		(great, 'great'),
		(okay, 'okay'),
		(fair, 'fair'),
		(working, 'working')
	)

	sale = 'sale'
	trade = 'trade'
	sale_trade = 'sale/trade'

	market_choices = (
		(sale, 'sale'),
		(trade, 'trade'),
		(sale_trade, 'sale/trade')
	)
	
	name = models.CharField(max_length=40)
	artist = models.ForeignKey(Artist, related_name='albums')
	description = models.TextField()
	owner = models.ForeignKey(Profile, related_name='albums')
	condition = models.CharField(max_length=10, choices=condition_choices)
	image = models.ImageField(upload_to='albums', blank=True, null=True)
	market = models.CharField(max_length=10, choices=market_choices)

	def __unicode__(self):
		return self.name