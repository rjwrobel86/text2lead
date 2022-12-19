import smtplib


def sendanemail(text):
	server = smtplib.SMTP_SSL("smtp.gmail.com",465)
	server.login([ACCOUNT],[KEY])
	server.sendmail("example@gmail.com","anotherexample@gmail.com",f"Writing Text -- {text} -- Text Written")
	server.quit()
	return "Mail Sent, I think."
