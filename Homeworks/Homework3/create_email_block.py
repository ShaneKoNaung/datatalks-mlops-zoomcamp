from prefect_email import EmailServerCredentials

credentials = EmailServerCredentials(
    username="my_mail@gmail.com",
    password="abcde",  # must be an app password
)
credentials.save("email-block")