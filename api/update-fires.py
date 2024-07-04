#!/usr/bin/env python3

import external.firms as firms
from core.database import get_session
from core.models import Fire
from sqlalchemy.exc import IntegrityError

session = get_session()
session = next(session)
new = 0
duplicates = 0
source = "VIIRS_SNPP_NRT"
country =  "ESP"

for fire in firms.API.get_today_fires_by_source_and_country(source, country):
	fire = Fire(
		latitude = fire.latitude,
		longitude = fire.longitude,
		date = fire.acq_date,
		confidence = fire.confidence)
	
	session.add(fire)

	# Do not create repeated fires (same latitude, longitude and date).
	try:
		session.commit()
		new += 1
	except IntegrityError:
		duplicates += 1
		session.rollback()

print(f"Created {new} new fires (ignored {duplicates} duplicates) in {country} from {source} data source.")
