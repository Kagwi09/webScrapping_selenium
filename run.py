from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # add tear_down=True if you want
    # to close the browser after loading
