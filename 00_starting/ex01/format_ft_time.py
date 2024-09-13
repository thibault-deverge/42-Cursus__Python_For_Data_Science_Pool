from datetime import datetime

today = datetime.today()
seconds = datetime.timestamp(today)

print(
    f'Seconds since January 1, 1970: {seconds:,} '
    f'or {seconds:.2e} in scientific notation\n'
    f'{today:%b %d %Y}'
)
