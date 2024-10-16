from booking.booking import Booking

with Booking(tear_down=True) as bot:
    bot.land_first_page()
    bot.close_popup()
    bot.change_currency(currency='USD')
    bot.close_popup()
    bot.select_destination('New York')
    input("Press Enter to close the browser...")
#     # add tear_down=True if you want
#     # to close the browser after loading